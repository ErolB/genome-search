'''
Created on 1/27/2018
Author: Erol Bahadiroglu

This tool examines a set of genomes to see if certain genes are present
'''

from modules import utils
from modules import file_tools
from modules import search_tools

hmm_path = '/home/erol/hmm_files/PreQ0_HMM'
genome_file = '/home/erol/hmm_files/DataBases_Simonetta/Archaea300.rw.faa'
pssm_path = '/home/erol/Projects/hmm_tool/cdd'

def menu(data_dict):
    print('Found %s entries.' % len(data_dict))
    print('1. Use all \n2. Select from list')
    selection = input()
    selected_entries = {}
    if selection == '1':
        selected_entries = data_dict
    elif selection == '2':
        for index, name in enumerate(data_dict.keys()):
            print('%s. %s' % (index, name))
            if index > 1000:
                print('%s more...' % str(len(data_dict)-1000))
                break
        selection2 = input('Enter index of first entry: ')
        while selection2.isnumeric():
            entry_name = list(data_dict.keys())[int(selection2)]
            selected_entries[entry_name] = data_dict[entry_name]
            selection2 = input('Enter index of next entry (enter a letter to finish): ')
    else:
        print('invalid input')
        return
    return selected_entries

if __name__ == '__main__':
    file_tools.clear_temp()
    # read JSON file for HMM directory
    hmm_dict = file_tools.get_hmms(hmm_path+'/hmm.json')
    # select genomes
    data_source = input('1. Read from file\n2. Retrive from PATRIC')
    if data_source == '1':
        print('Reading genomes...')
        genomes = file_tools.read_genomes(genome_file)
        selected_genomes = menu(genomes)
        selected_genomes = list(selected_genomes.values())
    elif data_source == '2':
        selected_genomes = search_tools.search_genomes()
    scan_method = input('1. HMM\n2. motif\n3. PSSM ')
    if scan_method == '1':
        # select HMMs
        print('Retrieving HMMs...')
        selected_hmms = menu(hmm_dict)
        file_tools.convert_old_hmms(hmm_path, '3.1b2')
        file_tools.compress_hmms(selected_hmms, hmm_path)
        # scan genomes with selected HMMs
        table = {}
        for genome in selected_genomes:
            file_tools.write_fasta(genome.organism, genome.get_genes())
            table[genome.organism] = search_tools.scan_genome(genome.organism)
    elif scan_method == '2':
        # enter motifs
        motifs = {}
        repeat = True
        while repeat:
            pattern = input('Enter motif: ')
            converted = str(utils.pattern_converter(pattern))
            motifs[pattern] = converted
            if input('Continue? (y/n)').lower() != 'y':
                repeat = False
        print(motifs)  # DEBUGGING
        table = {}
        for genome in selected_genomes:
            table[genome.organism] = utils.motif_scan_genome(genome, motifs)
    elif scan_method == '3':
        table = {}
        print("Retieving PSSMs...")
        # select PSSMs
        selected_pssms = menu(file_tools.read_dir(pssm_path))
        for genome in selected_genomes:
            feature_dict = {}
            file_tools.write_fasta(genome.organism, genome.get_genes())
            file_tools.create_db(genome.organism)
            for pssm in selected_pssms:
                file_tools.rescale_pssm(selected_pssms[pssm])
                feature_dict[pssm] = search_tools.search_cdd(genome.organism, selected_pssms[pssm])
            table[genome.organism] = feature_dict
    # visualize data
    print(table)
    utils.show_table(table)
    # clear temp directory
    #file_tools.clear_temp()
