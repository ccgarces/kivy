from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class SimpleKivy5(App):
    def build(self):
        return Widgets()

if __name__ == "__main__":
    SimpleKivy5().run()
    
    
