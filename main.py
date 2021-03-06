from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from modules.persons import Persons


class BMIScreen(Screen):
    pass


class DatabaseScreen(Screen):
    pass


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        builder = Builder.load_file('main.kv')
        self.persons = Persons()
        builder.ids.navigation.ids.tab_manager.screens[0].add_widget(self.persons)
        return builder


Test().run()