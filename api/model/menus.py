import sqlite3
import os
from definitions import ROOT_DIR

class MenusModel:
    class Menu:
        def __init__(self, **kwargs) -> None:
            self.buttons = []
            self.__dict__.update(kwargs)
        
        def add_button(self, button) -> None:
            self.buttons.append(button)


    class Button:
        def __init__(self, **kwargs) -> None:
            self.__dict__.update(kwargs)


    def __init__(self) -> None:
        conn = sqlite3.connect(os.path.join(ROOT_DIR, 'db', 'menus.db'))
        self.__db_cursor = conn.cursor()

        self.__db_cursor.execute('SELECT * FROM menus')
        columns = [description[0] for description in self.__db_cursor.description]
        rows = self.__db_cursor.fetchall()
        self.__menus = {}

        for menu_row in rows:
            menu = self.Menu(**dict(zip(columns, menu_row)))

            self.__db_cursor.execute(f"""SELECT * FROM buttons
                                        WHERE menuCode = '{menu.charCode}'""")
            btn_columns = [description[0] for description in self.__db_cursor.description]

            buttons = [self.Button(**dict(zip(btn_columns, button))) for button in (self.__db_cursor.fetchall())]
            menu.buttons = sorted(buttons, key=lambda button: button.sort)

            self.__menus[menu.location] = menu


    def get_menu_by_location(self, link):
        if (link in self.__menus):
            return self.__menus[link]
        else:
            return None