from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
class hello(App):

    def __init__(self):
        self.names=["ryan","john","david"]

    def build(self):
        self.title="hello"
        self.root=Builder.load_file('names.kv')
        self.add_labels()
        return self.root

    def add_labels(self):
        for i in self.names:
            temp_label= Label(text=i)
            self.root.ids.entries_box.add_widget(temp_label)



hello().run()