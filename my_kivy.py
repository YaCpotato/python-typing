from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def on_enter(instance, value = ''):
    print('User pressed enter in', instance)

def on_text(instance, value):
    print('The widget', instance, 'have:', value)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        textinput = TextInput(text='Hello world', multiline=False)
        textinput.bind(on_text_validate=on_enter, text=on_text)
        self.add_widget(textinput)

class MainApp(App):
    def build(self):
        MS = MainScreen()
        return MS

if __name__=="__main__":
    MainApp().run()