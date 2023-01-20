from kivy.app import App
from kivy.core.text import LabelBase, Label
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.image import Image


Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '812')

Builder.load_file("main.kv")
LabelBase.register(name='Montserrat', fn_regular='fonts/Montserrat.ttf')
LabelBase.register(name='Montserrat_Italic', fn_regular='fonts/Montserrat-Italic.ttf')
LabelBase.register(name='Montserrat_Bold', fn_regular='fonts/Montserrat-Bold.ttf')

class Task():
    deadline = None
    title = ""
    _desc = ""
    starred = False
    subtasks = []
    completed = False

class ImageButton(ButtonBehavior, Image):
    pass

class NewTaskPopUp(Popup):
    def addTask(self):
        print("test")

class ToDoList(BoxLayout): #ALL METHODS HERE

    tasks = ()

    def newTaskPopUp(self):
        newTaskPopUp = NewTaskPopUp()
        newTaskPopUp.open()

    def fillTaskList(self, category = None):
        for t in self.tasks:
            l = Label(text = t.title)
            self.ids["homeTaskList"].add(l)

    def addTask(self):
        t = Task()
        t.title = self.ids["titleInput"]
        t.desc = self.ids["descInput"]
        self.tasks.append(t)

class ToDoListApp(App): #DO NOT ALTERATE

    def build(self):
        return ToDoList()

if __name__ == '__main__':
    ToDoListApp().run()

