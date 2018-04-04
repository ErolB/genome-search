from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
    pass

class FileButton(Button):
    pass

class PatricButton(Button):
    pass

class StartScreen(Screen):
    pass

class FileScreen(Screen):
    file_name = ObjectProperty(None)
    data_file = None
    def load(obj, path):
        data_file = open(path, 'r')
        print(path)

class PatricScreen(Screen):
    pass

layout = Builder.load_file('kv/layout.kv')

class MyApp(App):
    def build(self):
        return layout

if __name__ == '__main__':
    app = MyApp()
    app.run()
