from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

Builder.load_file("main.kv")

class Task():
    deadline = None

class ToDoList(BoxLayout):

    def tmp(self):
        pass

class ToDoListApp(App):

    def build(self):
        return ToDoList()

if __name__ == '__main__':
    ToDoListApp().run()