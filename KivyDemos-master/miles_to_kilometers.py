from kivy.app import App
from kivy.lang import Builder

class convert(App):
    def build(self):
        self.title="Convert miles to km"
        self.root=Builder.load_file('miles_to_km.kv')
        return self.root

    def change(self,increment):
        hello=int(self.root.ids.input.text)
        hello+=increment
        self.root.ids.input.text=hello

    def convert(self,num):
        x=num*1.609344
        x=str(x)
        self.root.ids.output.text=x


convert().run()