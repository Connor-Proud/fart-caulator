from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
import random

# This application and code was created by Connor Kennedy Proudlock 08/08/2024 at 20:26
# all image assets were created by me using the gimp program
# all sound assets were heavily changed and edited using audacity


fart_array = [
    "assets/Fart sound effect normal.wav",
    "assets/Fart sound effect1.wav",
    "assets/Fart sound effect2.wav",
    "assets/Fart sound effect3.wav",
    "assets/Fart sound effect4.wav"]


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.button_sound = SoundLoader.load(random.choice(fart_array))

    def play_sound(self):
        selected_sound = random.choice(fart_array)
        sound = SoundLoader.load(selected_sound)
        if sound:
            sound.play()

    def calculate(self, expression):
        self.play_sound()
        try:
            self.display.text = str(eval(expression))
        except Exception:
            self.display.text = "Error"

    def clear(self):
        self.play_sound()
        self.display.text = ""

    def append_expression(self, value):
        self.play_sound()
        self.display.text += str(value)


class CalculatorApp(App):
    def build(self):
        self.title = "Shit Calculator"
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
