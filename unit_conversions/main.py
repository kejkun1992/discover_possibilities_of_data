# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'fullscreen', '0')


class UnitConversions(GridLayout):
    pass
                
       
class MyApp(App):
    def build(self):
        return UnitConversions()

if __name__ == '__main__':
    MyApp().run()
