from kivy.app import App
from kivy.uix.label import Label

class AntiTheftApp(App):
    def build(self):
        return Label(text="Anti-Theft App Running Successfully!")

if __name__ == '__main__':
    AntiTheftApp().run()
  
