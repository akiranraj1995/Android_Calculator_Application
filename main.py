from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

# Set Kivy window size and title
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 600)
Config.set('graphics', 'minimum_width', 400)
Config.set('graphics', 'minimum_height', 600)

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        # Add a Backspace button
        backspace_button = Button(text="<-")
        backspace_button.bind(on_press=self.on_backspace)
        layout.add_widget(backspace_button)

        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        elif button_text == "<-":
            self.result.text = current[:-1]  # Remove the last character
        else:
            new_text = current + button_text
            self.result.text = new_text

    def on_backspace(self, instance):
        current = self.result.text
        if current:
            self.result.text = current[:-1]  # Remove the last character

    def on_solution(self, instance):
        text = self.result.text
        try:
            result = str(eval(self.result.text))
            self.result.text = result
        except Exception:
            self.result.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
