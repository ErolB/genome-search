from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.adapters.listadapter import ListAdapter
from modules import file_tools
from modules import search_tools

import shutil

class Manager(ScreenManager):
    candidate_genomes = []  # list of genomes to select from
    genome_list = ObjectProperty(None)  # list of genome objects for analysis
    hmm_list = []

    # ensures that genome_list_obj contains the latest genome list
    def update(self, data_list_obj, data):
        data_list_obj.adapter.data = data
        data_list_obj._trigger_reset_populate()

    # adds the selected item from one list to another
    def add(self, data_list_obj, selection_list_obj):
        if not data_list_obj.adapter.selection:  # stop if nothing is selected
            return
        selection = data_list_obj.adapter.selection[0].text
        if selection in selection_list_obj.adapter.data:  # stop if item is already in the list
            return
        selection_list_obj.adapter.data.append(selection)
        data_list_obj._trigger_reset_populate()  # update UI
        selection_list_obj._trigger_reset_populate()

    # removes an entry from a list
    def remove(self, data_list_obj):
        if not data_list_obj.adapter.selection:  # stop if nothing is selected
            return
        selection = data_list_obj.adapter.selection[0].text
        data_list_obj.adapter.data.remove(selection)
        data_list_obj._trigger_reset_populate()


class FileButton(Button):
    pass

class PatricButton(Button):
    pass

class StartScreen(Screen):
    pass

class ListItem(GridLayout):
    def __init__(self, name, id, **kwargs):
        super.__init__(ListItem, self, **kwargs)
        self.cols = 2
        self.add_widget(Label(text=name))
        self.box = Checkbox()
        self.add_widget(self.box)

class GenomeList(GridLayout):
    genomes = ObjectProperty()

class FileScreen(Screen):
    file_name = ObjectProperty(None)
    selection = ObjectProperty(None)
    def load(obj, path):
        return file_tools.read_genomes(path)

class PatricScreen(Screen):
    species = ObjectProperty(None)

    def name_search(self, name):
        return search_tools.search_by_name(name.text)

class SelectGenomesScreen(Screen):
    selected_genomes = ObjectProperty()

    def get_genes(self, genomes):  # fills in genes from PATRIC genomes
        return search_tools.retrieve_sequences(genomes)

class StartSearchScreen(Screen):
    pass

class SelectHMMScreen(Screen):
    pass

class SelectHMMScreen2(Screen):
    select_hmm = ObjectProperty()

    def hmm_search(self, hmm_list, genome_list):
        # copy HMM files to temp
        for hmm_file in hmm_list:
            shutil.copy(hmm_file, './temp_files')
        # prepare for search
        file_tools.convert_old_hmms('./temp', '3.1b2')
        file_tools.compress_hmms('./temp')
        # perform search


layout = Builder.load_file('kv/layout.kv')

class MyApp(App):
    def build(self):
        return layout

if __name__ == '__main__':
    app = MyApp()
    app.run()
