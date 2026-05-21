# This Python file uses the following encoding: utf-8
import sys

#from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtWidgets, QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class HomeScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   #IDK What this does, look into it
        self.ui.setupUi(self)

        self.parent = parent
        self.setObjectName("Home")


        #Layout settings
        self.layout = QtWidgets.QGridLayout(self)

        #Populating the home screen
        self.title = QtWidgets.QLabel("Queen's Blood Online")
        self.layout.addWidget(self.title, 0, 1, alignment=QtCore.Qt.AlignHCenter)

        self.connection_info()
        self.deck_display()
        self.create_deck_editor_button()
        self.create_play_button()

    #Helpers to create various buttons
    def create_deck_editor_button(self):
        self.to_deck_editor = QtWidgets.QPushButton("Deck Editor", self)
        self.to_deck_editor.clicked.connect(self.to_deck_screen)
        self.layout.addWidget(self.to_deck_editor, 2, 1, alignment=QtCore.Qt.AlignCenter)

    def create_play_button(self):
        self.to_play = QtWidgets.QPushButton("Play", self)
        self.to_play.clicked.connect(self.to_play_screen)
        self.layout.addWidget(self.to_play, 1, 1, alignment = QtCore.Qt.AlignCenter)

    #TODO: Deal with connection information
    def connection_info(self):
        self.connection_info = QtWidgets.QLabel("Connection info here")
        self.layout.addWidget(self.connection_info, 1, 0, alignment=QtCore.Qt.AlignCenter)

    #TODO: Display the currently selected deck
    def deck_display(self):
        self.selected_deck_info = QtWidgets.QLabel("Selected Deck Info here")
        self.layout.addWidget(self.selected_deck_info, 1, 2, alignment=QtCore.Qt.AlignCenter)

    #TODO: Actually go to the deck editor.  The deck editor widget needs to be created
    def to_deck_screen(self):
        print("Work in Progress")

    #TODO: This is also probably where the game should start, but it feels kinda weird to have the home_screen UI start the game.  Main or GameUI should probably start running the game engine
    def to_play_screen(self):
        self.parent.change_screen("Game")


#Ideally this is obsolete and main.py should be run instead
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = HomeScreen()
    widget.show()
    sys.exit(app.exec())
