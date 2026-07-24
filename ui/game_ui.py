# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

#This file controlls what the player sees, as well as input from the player from buttons and such
class GameUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   #IDK What this does, look into it
        self.ui.setupUi(self)

        self.parent = parent
        self.setObjectName("Game")
        #TODO: Create the game's UI


