# text_wrap_example.py
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        layout = FloatLayout()

        # Create a Label with very large text
        self.label = Label(
            text='This is a test text for testing the program',
            size_hint=(None, None),  # Disable size hints
            width=layout.width * 0.8,  # Set width to 80% of layout width
            height=300,  # Fixed height
            halign='center',  # Horizontal alignment of text
            valign='middle',  # Vertical alignment of text
            font_size='75sp'  # Increase font size
        )

        # Add the label to the layout
        layout.add_widget(self.label)

        # Bind the layout size to center the label
        layout.bind(size=lambda instance, value: self.center_label(instance))

        # Bind the label's size to update text size for wrapping
        self.label.bind(size=self.update_text_size)

        return layout

    def update_text_size(self, instance, value):
        # Update the text_size based on the label's width
        self.label.text_size = (self.label.width, None)  # Allow text to wrap

    def center_label(self, layout):
        # Center the label in the layout
        self.label.size = (layout.width * 0.8, self.label.height)  # Update width
        self.label.center_x = layout.center_x
        self.label.center_y = layout.center_y

if __name__ == '__main__':
    TestApp().run()