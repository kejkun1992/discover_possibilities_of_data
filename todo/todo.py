# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'fullscreen', '0')


class ToDoListButton(ListItemButton):
    pass


class ToDoList(GridLayout):
    task = ObjectProperty()
    task_list = ObjectProperty()
    
    def submit_task(self):
        text = self.task.text
        self.task_list.adapter.data.extend([text])
        self.task_list._trigger_reset_populate()
        
    def delete_task(self):
        if self.task_list.adapter.selection:
            selection = self.task_list.adapter.selection[0].text
            self.task_list.adapter.data.remove(selection)
            self.task_list._trigger_reset_populate()
            
    def replace_task(self):
        if self.task_list.adapter.selection:
            selection = self.task_list.adapter.selection[0].text
            self.task_list.adapter.data.remove(selection)
            self.submit_task()


class ToDoApp(App):
    def build(self):
        return ToDoList()

if __name__ == '__main__':
    ToDoApp().run()