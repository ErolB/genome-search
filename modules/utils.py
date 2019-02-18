from matplotlib import pyplot as plt
from jinja2 import Template

class Gene(object):
    def __init__(self, name, sequence, description=None, patric_id=None):
        self.name = name
        self.sequence = sequence
        if description:
            self.description = description
        if patric_id:
            self.patric_id = patric_id
        else:
            self.patric_id = 'not available'

    def get_sequence(self):
        return self.sequence

class Genome(object):
    def __init__(self, organism, id=None):
        self.organism = organism.replace(' ', '_')
        self.id = id
        self.genes = {}

    def add_gene(self, name, sequence, description=None, patric_id=None):
        self.genes[name] = Gene(name, sequence, description=description, patric_id=patric_id)

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

'''
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
'''

def generate_page(results, headings=[]):
    template_html = open('template.html', 'r').read()
    t = Template(template_html)
    final_html = t.render(results=results, headings=headings)
    with open('result.html', 'w') as final:
        final.write(final_html)
