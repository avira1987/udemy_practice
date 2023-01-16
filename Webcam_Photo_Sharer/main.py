from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser
from FileSharer import FileShare

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play =False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        self.filepath = f"files/{ current_time }.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):
    """ Access the photo filepath uploads it to the web,
    and insert the link in the lable widget"""
    def create_link(self):
        try:
            file_path = App.get_running_app().root.ids.camera_screen.filepath
            fileshare = FileShare(filepath=file_path)
            self.url = fileshare.share()
            self.ids.Link.text = self.url
        except:
            self.ids.Link.text = 'Cannot connect to proxy.'
    def copy_link(self):
        """Copy link to clipboard avalble for pasting"""
        try:
            Clipboard.copy(self.url)
            self.ids.Link.text = 'Copyed on your clipboard'
        except:
            self.ids.Link.text = "Create a link First"
        """open link on defual web browser"""
    def open_link(self):
        try:
            webbrowser.open(self.url)
            self.ids.Link.text = 'Opened on browser'
        except:
            self.ids.Link.text = 'First press create share link'

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()