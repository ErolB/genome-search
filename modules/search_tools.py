import subprocess
import os
import csv

from modules import utils

def search_genomes():
    proceed = False
    genome_list = []
    while not proceed:
        selection = input('1. search by name\n2. search by taxon ID')
        if selection == '1':
            query = input('Enter organism name: ')
            # look up organism in PATRIC genome database
            output = subprocess.run('p3-all-genomes --eq organism_name,%s --attr organism_name' % query, stdout=subprocess.PIPE, shell=True)
            results = csv.DictReader(output.stdout.decode().split('\n'), delimiter='\t')
            results = list(results)
            if not results: # if no results were found
                print('No results')
                continue
            # if there are search results
            for index, data in enumerate(results):
                print('%s. %s' % (str(index),data['genome.organism_name']))
            genome_index = input('Select organism (by index): ')
            genome_id = results[int(genome_index)]['genome.genome_id']
            organism_name = results[int(genome_index)]['genome.organism_name']
            # get protein sequences
            output = subprocess.run('p3-all-genomes --eq genome_id,%s | p3-get-genome-features --attr feature_id --attr product --attr aa_sequence' %
                                    genome_id, stdout=subprocess.PIPE, shell=True)
            results = csv.DictReader(output.stdout.decode().split('\n'), delimiter='\t')
            genome = utils.Genome(organism_name)
            for gene in results:
                genome.add_gene(gene['feature.feature_id'], gene['feature.aa_sequence'], gene['feature.product'])
        genome_list.append(genome)
        proceed = (input('select another genome? (y/n) ').lower() != 'y')
    return genome_list

# scans using HMMs
def scan_genome(genome_name):
    feature_dict = {}
    os.chdir('temp_files')
    process = subprocess.run('hmmsearch -E 0.000001 all %s' % genome_name,
        stdout=subprocess.PIPE, shell=True)  # E-value cutoff is 10^-6
    os.chdir('..')
    segments = process.stdout.decode().split('\n//')
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

# scans using PSI-BLAST
def search_cdd(genome, pssm_path, threshold=0.000001):
    process = subprocess.run('psiblast -db temp_files/%s -in_pssm %s -evalue %s' %
        (genome,pssm_path,str(threshold)), stdout=subprocess.PIPE, shell=True)
    output = process.stdout.decode()
    # check if no results were found
    if "No hits found" in output:
        return 0
    else:
        return 1
