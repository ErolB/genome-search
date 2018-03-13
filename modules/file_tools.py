'''
Created on : 1/27/2018
Author: Erol Bahadiroglu
'''

from modules.utils import Genome
import os
import re
import subprocess
import shutil
import time
import json

# reads the contents of a directory and returns a dictionary mapping file names to full paths
def read_dir(path):
    file_dict = {}
    files = os.listdir(path)
    for item in files:
        file_dict[item] = path + '/' + item
    return file_dict

# reads a FASTA file and creates a list of Genome objects
def read_genomes(file_path):
    genomes = {}
    gene_file = open(file_path, 'r')
    data = gene_file.read()
    genes = data.split('>')
    for gene in genes:
        if not gene:
            continue
        header, sequence = gene.split('\n', 1)
        sequence = sequence.replace('\n', '')  # removes spaces
        title, description = header.split('|')
        organism, locus = title.split('@')
        if organism in list(genomes.keys()):
            genomes[organism].add_gene(locus, sequence, description=description)
        else:
            genomes[organism] = Genome(organism)
            genomes[organism].add_gene(locus, sequence, description=description)
    return genomes

# writes sequences to a FASTA file_path
def write_fasta(file_name, genes):
    with open('temp_files/'+file_name, 'w') as fasta_file:
        for name, seq in genes.items():
            fasta_file.write('>'+name+'\n')
            fasta_file.write(seq+'\n')

# reads the JSON file associated with a set of HMMs
def get_hmms(file_path):
    with open(file_path, 'r') as guide:
        return json.loads(guide.read())

# compresses a single HMM file
def compress_hmm(hmm_name, file_path):
    shutil.copyfile(file_path, './temp_files/'+hmm_name)
    subprocess.call('hmmpress temp_files/%s' % hmm_name)

# compresses a set of HMMs
def compress_hmms(hmm_names, hmm_path):
    all_hmm = []
    for file_name in os.listdir(hmm_path):
        if file_name in hmm_names.values():
            with open(hmm_path+'/'+file_name, 'r') as hmm_file:
                all_hmm.append(hmm_file.read())
    with open('temp_files/all', 'w') as all_hmm_file:  # creates a temporary file containing every hmm
        for hmm in all_hmm:
            all_hmm_file.write(hmm)
    subprocess.call('hmmpress temp_files/all', shell=True)

# searches for HMM files with outdated formats and converts them
def convert_old_hmms(path, latest_version):
    for file_name in os.listdir(path):
        if file_name[-4:] == '.hmm':  # checks for HMM fiels
            with open(path+'/'+file_name, 'r') as hmm_file:
                header = hmm_file.read().split('\n')[0]
                version = re.search('\[\S+', header).group(0).replace('[', '')
                if version != latest_version:
                    os.rename('%s/%s' % (path,file_name), '%s/%s_old' % (path,file_name))
                    subprocess.call('hmmconvert %s/%s_old > %s/%s' % (path,file_name,path,file_name), shell=True)
                    os.remove('%s/%s_old' % (path,file_name))

# read the output file for presence of file_name
def read_output(name):
    feature_dict = {}
    with open('temp_files/%s.out' % name) as output_file:
        segments = output_file.read().split('\n//')
        for block in segments:
            header = block.split('\n')[1]
            if 'Query' not in header:
                continue
            feature = block.split('\n')[1].split(':')[1].strip()
            feature = feature.split()[0]
            if 'No hits detected' in block:
                feature_dict[feature] = 0
            else:
                feature_dict[feature] = 1
    return feature_dict

# clear the temp_files folder
def clear_temp():
    for file_name in os.listdir('temp_files'):
        os.remove('temp_files/'+file_name)

# rescales PSSM file
def rescale_pssm(file_path):
    f = open(file_path, 'r')
    content = f.read()
    f.close()
    # modify contents
    start = content.find("scores {")
    end = content.find("}", start)
    scores = re.sub("([0-9]{2})(?=[\r\n\,])", "", content[start:end])
    scores = re.sub("\ (\-)?,", " 0,", scores)
    # rewrite file
    f = open(file_path, 'w')
    f.write(content[0:start] + scores + content[end:].replace("scalingFactor 100", "scalingFactor 1"))
    f.close()

# creates database for BLAST
def create_db(file_name):
    subprocess.run("makeblastdb -in temp_files/%s -dbtype prot" % file_name, shell=True)
