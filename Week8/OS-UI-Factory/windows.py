from abstracts import Checkbox, Button

class WindowsButton(Button):
    def render(self):
        print("Rendering a window-style button.")

class WindowsCheckbox(Checkbox):
    def render(self):
        print("Rendering a window-style checkbox.")

