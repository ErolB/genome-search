import re
from matplotlib import pyplot as plt

class Gene(object):
    def __init__(self, name, sequence, description=None):
        self.name = name
        self.sequence = sequence
        if description:
            self.description = description

    def get_sequence(self):
        return self.sequence


class Genome(object):
    def __init__(self, organism):
        self.organism = organism.replace(' ', '_')
        self.genes = {}

    def add_gene(self, name, sequence, description=None):
        self.genes[name] = Gene(name, sequence, description=description)

    def get_sequence(self, name):
        return self.genes[name].get_sequence()

    # returns a list of sequences
    def get_all_sequences(self):
        return [gene.get_sequence() for gene in self.genes.values()]

    # returns a dictionary mapping gene names to sequences
    def get_genes(self):
         gene_dict = {}
         for gene in self.genes.items():
             name = gene[0]
             seq = gene[1].get_sequence()
             gene_dict[name] = seq
         return gene_dict

def show_table(table):
    image = []
    genome_list = list(table.keys())
    hmm_list = list(table[genome_list[0]].keys())
    for genome in genome_list:
        row = []
        for hmm in hmm_list:
            row.append(table[genome][hmm])
        image.append(row)
    plt.imshow(image, vmin=0, vmax=1)
    plt.xticks(range(len(hmm_list)), hmm_list, rotation=45)
    plt.yticks(range(len(genome_list)), genome_list)
    plt.show()

# converts a pattern in PROSITE format to standard regualar expression format
def pattern_converter(prosite_pattern):
    segments = prosite_pattern.split('-')
    output_pattern = ''
    for item in segments:
        # handle a set of possible values
        possible_chars = re.findall('\[\w+\]', item)
        excluded_chars = re.findall('\{\w+\}', item)
        if possible_chars:
            possible_chars = re.sub('(\[|\])', '', possible_chars[0])
            aa_list = [aa for aa in possible_chars]
            output_pattern += ('(' + '|'.join(aa_list) + ')')
        # handle a set of excluded values
        elif excluded_chars:
            excluded_chars = re.sub('(\{|\})', '', excluded_chars[0])
            aa_list = [aa for aa in excluded_chars]
            output_pattern += '[^(' + '|'.join(aa_list) + ')]'
        # handle single values
        else:
            aa = re.findall('(?=\(?)\w', item)[0]
            if aa == 'x':  # check for wildcarda
                output_pattern += "\w"
            else:
                output_pattern += aa
        # handle multiplier
        multiplier = re.findall('\(\d\-?\d?\)', item)
        if multiplier:
            multiplier = re.sub('(\(|\))', '', multiplier[0])
            output_pattern += '{' + multiplier + '}'
    return output_pattern

def motif_scan_genome(genome_obj, patterns):
    feature_dict = {}
    for motif in patterns:
        for gene in genome_obj.genes.values():
            seq = gene.get_sequence()
            if re.findall(patterns[motif], seq):
                feature_dict[motif] = 1
                break
            else:
                feature_dict[motif] = 0
    print(feature_dict)
    return feature_dict
