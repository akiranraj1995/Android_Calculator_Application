from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class CalculatorApp(App):
    def build(self):
        self.operator = ""
        self.last_was_operator = None
        self.last_button = None

        # Create the main layout
        main_layout = BoxLayout(orientation="vertical")

        # Create the input field
        self.text_input = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        main_layout.add_widget(self.text_input)

        # Create a nested layout for buttons
        button_layout = GridLayout(cols=4)
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "<-", "+",  # Changed "⌫" to "<-"
            "="
        ]

        # Create buttons and bind them to the button_click function
        for button_text in buttons:
            button = Button(text=button_text, pos_hint={"center_x": 0.5, "center_y": 0.5})
            button.bind(on_press=self.button_click)
            button_layout.add_widget(button)

        # Add the button layout to the main layout
        main_layout.add_widget(button_layout)

        return main_layout

    def button_click(self, instance):
        current = self.text_input.text
        button_text = instance.text

        # Handle digit buttons
        if button_text in "0123456789":
            if current == "0":
                new_text = button_text
            else:
                new_text = current + button_text
            self.text_input.text = new_text
        elif button_text == "=":
            # Calculate the result when "=" is pressed
            self.on_solution(instance)
        elif button_text == "C":
            # Clear the input field and reset all values
            self.text_input.text = ""
            self.operator = ""
            self.last_was_operator = None
        elif button_text == "<-":
            # Handle backspace
            new_text = current[:-1]
            self.text_input.text = new_text
        else:
            # Handle operator buttons (+, -, *, /)
            if current and (self.last_was_operator and button_text in "+-*/"):
                # If the last button was an operator and a new operator is pressed, replace the old operator with the new one
                new_text = current[:-1] + button_text
                self.text_input.text = new_text
            elif current == "" and button_text == "-":
                # Allow entry of a negative number
                self.text_input.text = button_text
            elif current != "" and not self.last_was_operator:
                # Append the operator to the current text
                new_text = current + button_text
                self.text_input.text = new_text

        self.last_button = instance
        self.last_was_operator = button_text in "+-*/"

    def on_solution(self, instance):
        text = self.text_input.text
        try:
            # Attempt to evaluate the expression
            result = str(eval(text))
            self.text_input.text = result
        except Exception:
            # Handle errors in expression
            self.text_input.text = "Error"


if __name__ == "__main__":
    CalculatorApp().run()
