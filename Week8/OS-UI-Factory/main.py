from factory import GUIFactory, WindowsFactory, MacFactory

def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()

render_ui(WindowsFactory())
render_ui(MacFactory())