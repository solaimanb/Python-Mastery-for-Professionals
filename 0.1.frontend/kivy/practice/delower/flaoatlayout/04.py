from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image 

class MyApp(App):
    def build(self):
        layout = FloatLayout()

        label = Label(text="Enter your name", size_hint=(.2, .1), pos_hint={ "x":.2, "y":.5})
        textinput = TextInput(size_hint=(.4, .1), pos_hint={ "x":.2, "y":.4})
        button = Button(text="verify", size_hint=(.2, .1), pos_hint={"x":.6, "y":.4})
        label2 = Label(text="Welcom   to   Maktabun", size_hint=(.4 , .1), pos_hint ={"x":.3, "y":.6})
        label1 = Label(text="Enter your email Id", size_hint=(.2, .1), pos_hint={"x":.2, "y":.3})
        textinput1 = TextInput(size_hint=(.4, .1), pos_hint={ "x":.2, "y":.2})
        button1 = Button(text="verify", size_hint=(.2, .1), pos_hint={"x":.6, "y":.2})
        img1 = Image(source="data:image/jpeg;base64,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", size_hint=(.2, .2), pos_hint={"x":.4, "y":.78955})

        layout.add_widget(label1)
        layout.add_widget(label)
        layout.add_widget(textinput)
        layout.add_widget(button)
        layout.add_widget(label2)
        layout.add_widget(textinput1)
        layout.add_widget(button1)
        layout.add_widget(img1)

        return layout
if __name__ =="__main__":
    MyApp().run()