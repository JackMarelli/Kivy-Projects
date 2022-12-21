from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App


class AccordionApp(App):
    def build(self):
        root = Accordion()
        for x in range(5):
            item = AccordionItem(title='Title %d' % x)
            item.add_widget(Label(text='Very big content\n' * 10))
            root.add_widget(item)

        quadrItem = AccordionItem(title="Quadrato")
        quadrItem.add_widget(Label(text="qui si calcolano perimetro e area del quadrato"))
        root.add_widget(quadrItem)

        trianItem = AccordionItem(title="Triangolo")
        trianItem.add_widget(Label(text="qui si calcolano perimetro e area del triangolo"))
        root.add_widget(trianItem)
        return root


if __name__ == '__main__':
    AccordionApp().run()