# functions for retrieving genomic data

import subprocess
import os
import csv

from modules.utils import *

# search PATRIC by organism name
def search_by_name(organism_name):
    output = subprocess.check_output('p3-all-genomes --eq organism_name,%s --attr organism_name' % organism_name, shell=True)
    results = csv.DictReader(output.decode().split('\n'), delimiter='\t')
    results = list(results)
    genomes = []
    for item in results:
        new_genome = Genome(item['genome.organism_name'], id=item['genome.genome_id'])
        genomes.append(new_genome)
    return genomes

# search PATRIC by taxon ID
def search_by_id(organism_name):
    output = subprocess.check_output('p3-all-genomes --eq genome_id,%s --attr organism_name' % organism_name, shell=True)
    results = csv.DictReader(output.decode().split('\n'), delimiter='\t')
    results = list(results)
    genomes = []
    for item in results:
        new_genome = Genome(item['genome.organism_name'], id=item['genome.genome_id'])
        genomes.append(new_genome)
    return genomes

# retrieve gene sequences from PATRIC (if genome was obtained there)
def retrieve_sequences(genomes):
    for entry in genomes:
        if entry.id is None:
            continue  # continue if genome was obtained locally
        output = subprocess.check_output(
            'p3-all-genomes --eq genome_id,%s | p3-get-genome-features --attr feature_id --attr product --attr aa_sequence --attr patric_id' %
            entry.id, shell=True)
        results = csv.DictReader(output.decode().split('\n'), delimiter='\t')
        for gene in results:
            entry.add_gene(gene['feature.feature_id'], gene['feature.aa_sequence'], gene['feature.product'], gene['feature.patric_id'])
    return genomes

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
    return list(genomes.values())

# reads the contents of a directory and returns a dictionary mapping file names to full paths
def read_dir(path):
    file_dict = {}
    files = os.listdir(path)
    for item in files:
        file_dict[item] = path + '/' + item
    return file_dict