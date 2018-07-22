# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'fullscreen', '0')


class UnitConversions(GridLayout):
    def in_to_cm(self, number):
        try:
            self.display.text = str(2.54 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def cm_to_in(self, number):
        try:
            self.display.text = str(0.393700787 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def ft_to_m(self, number):
        try:
            self.display.text = str(0.3048 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def m_to_ft(self, number):
        try:
            self.display.text = str(3.2808399 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def yd_to_m(self, number):
        try:
            self.display.text = str(0.9144 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def m_to_yd(self, number):
        try:
            self.display.text = str(1.0936133 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def kmh_to_ms(self, number):
        try:
            self.display.text = str(0.277777778 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
    def ms_to_kmh(self, number):
        try:
            self.display.text = str(3.6 * float(number))
        except ValueError:
            self.display.text = 'Error'
            
       
class MyApp(App):
    def build(self):
        return UnitConversions()

if __name__ == '__main__':
    MyApp().run()
