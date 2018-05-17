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

class Manager(ScreenManager):
    candidate_genomes = []  # list of genomes to select from
    genome_list = ObjectProperty(None)

    # ensures that genome_list_obj contains the latest genome list
    def update(self, genome_list_obj, genomes):
        genome_list_obj.adapter.data = [item["genome.organism_name"] for item in genomes]
        genome_list_obj._trigger_reset_populate()

    # adds the selected item from one list to another
    def add(self, genome_list_obj, selection_list_obj):
        if not genome_list_obj.adapter.selection:  # stop if nothing is selected
            return
        selection = genome_list_obj.adapter.selection[0].text
        if selection in selection_list_obj.adapter.data:  # stop if item is already in the list
            return
        selection_list_obj.adapter.data.append(selection)
        genome_list_obj._trigger_reset_populate()  # update UI
        selection_list_obj._trigger_reset_populate()

    # removes an entry from a list
    def remove(self, genome_list_obj):
        if not genome_list_obj.adapter.selection:  # stop if nothing is selected
            return
        selection = genome_list_obj.adapter.selection[0].text
        genome_list_obj.adapter.data.remove(selection)
        genome_list_obj._trigger_reset_populate()


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

class GenomeListItem(ListItemButton):
    pass

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

layout = Builder.load_file('kv/layout.kv')

class MyApp(App):
    def build(self):
        return layout

if __name__ == '__main__':
    app = MyApp()
    app.run()
