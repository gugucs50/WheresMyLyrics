from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TestApp(App):
    def build(self):
        layout = FloatLayout()

        self.label = Label(
            text='This is a test text for testing the program',
            size_hint=(None, None),  
            width=layout.width * 0.8,  
            height=300,  
            halign='center',  
            valign='middle',  
            font_size='75sp'  
        )

        # adding a layout label
        layout.add_widget(self.label)

        # bind the layout size for wrapping text
        layout.bind(size=lambda instance, value: self.center_label(instance))

        # bind the size when wrapping text
        self.label.bind(size=self.update_text_size)

        return layout

    def update_text_size(self, instance, value):
        # wrapping text
        self.label.text_size = (self.label.width, None)  

    def center_label(self, layout):
        # centering the label
        self.label.size = (layout.width * 0.8, self.label.height)  
        self.label.center_x = layout.center_x
        self.label.center_y = layout.center_y

if __name__ == '__main__':
    TestApp().run()