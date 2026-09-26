from abstracts import Button, Checkbox

class MacOSButton(Button):
    def render(self):
        print("Rendering a MacOS-type button.")

class MacOSCheckbox(Checkbox):
    def render(self):
        print("Rendering a MacOS-type checkbox.")

