from kivy.app import App
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

Builder.load_file("main.kv")
LabelBase.register(name='Montserrat', fn_regular='fonts/Montserrat.ttf')
LabelBase.register(name='Montserrat_Italic', fn_regular='fonts/Montserrat-Italic.ttf')
LabelBase.register(name='Montserrat_Bold', fn_regular='fonts/Montserrat-Bold.ttf')

class Task():
    deadline = None
    title = ""
    desc = ""


class ToDoList(BoxLayout):

    def tmp(self):
        pass

class ToDoListApp(App):

    def build(self):
        return ToDoList()

if __name__ == '__main__':
    ToDoListApp().run()