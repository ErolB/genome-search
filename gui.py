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
    genome_list = []  # list of genomes for analysis

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
    pass

layout = Builder.load_file('kv/layout.kv')

class MyApp(App):
    def build(self):
        return layout

if __name__ == '__main__':
    app = MyApp()
    app.run()
