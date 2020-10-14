
"""
Created on Mon Oct  5 12:03:13 2020

@author: hazac
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import kivy.core.window as window
from kivy.base import EventLoop
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.screenmanager import FadeTransition




class MainWindow(Screen):
    def btn(self):
        show_popup()
        allow_stretch: True
        
    

  

class SecondWindow(Screen):
    pass

class Images(Screen):
    text_changed =StringProperty()
    
    def change_bluetext(self):
        self.text_changed = "Are you sure you want to choose Blue?"
       
    def change_redtext(self):
        self.text_changed = "Are you sure you want to choose Red?"
       
    def btn(self):
        show_choicepopup()
    
class RedPill(Screen):
    pass
    
    
class BluePill(Screen):
    pass
            
class WindowManager (ScreenManager):
    pass



class P(FloatLayout):
    pass



kv = Builder.load_file("myyy.kv")
 # app.attempt_login(Username.text, Password.text)

class MyyyMainApp(App):
    
    
    def build(self):
        self.title = 'Login Screen'
        allow_stretch: True
        
        return kv
    
    def attempt_login(self, username, password):
        if username == 'haza' and password == 'harry':
            self.root.current = 'second'
        else: 
            show_popup()
    
    def selection(self, text_changed, root):
        if root.text_changed == 'Are you sure you want to choose Blue?' :
            self.root.current = 'BluePill'
        elif root.text_changed == 'Are you sure you want to choose Red?' :
            self.root.current = 'RedPill'
        else: 
            show_choicepopup()
         
    
def show_popup():
    show = P()
    
    popupWindow = Popup(title= "Wrong Password", content=show, 
                       
                  size_hint=(None, None), size=(300, 200))
    
    
    popupWindow.open()
    
def show_choicepopup():
    
    popupWindow = Popup(title= "You Need to Make A Choice",
                       
                  size_hint=(None, None), size=(300, 200))
    
    
    popupWindow.open()
def reset():

    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
    
if __name__ == "__main__":
    reset()
    MyyyMainApp().run()
