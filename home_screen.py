# This Python file uses the following encoding: utf-8
import sys

#from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtWidgets, QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

#I think that this widget will be the main window, and the other screens of the game are all separate widgets that the main window will display as needed
#   I just don't quite know how the sub widgets will be able to "end" themselves to return to the main screen
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   #IDK What this does, look into it
        self.ui.setupUi(self)

        #Layout settings
        self.layout = QtWidgets.QGridLayout(self)

        #Title
        self.title = QtWidgets.QLabel("Queen's Blood Online")
        self.layout.addWidget(self.title, 0, 1, alignment=QtCore.Qt.AlignHCenter)

        #TODO: FIGURE OUT WHAT TO DO HERE
        #Connection Info section
        self.connection_info = QtWidgets.QLabel("Connection info here")
        self.layout.addWidget(self.connection_info, 1, 0, alignment=QtCore.Qt.AlignCenter)

        #TODO: FIGURE OUT WHAT TO DO HERE
        #Selected Deck Display
        self.selected_deck_info = QtWidgets.QLabel("Selected Deck Info here")
        self.layout.addWidget(self.selected_deck_info, 1, 2, alignment=QtCore.Qt.AlignCenter)

        #Create buttons to go to various screens
        #Deck Editor Button
        self.to_deck_editor = QtWidgets.QPushButton("Deck Editor", self)
        self.to_deck_editor.clicked.connect(self.to_deck_screen)
        self.layout.addWidget(self.to_deck_editor, 2, 1, alignment=QtCore.Qt.AlignCenter)

        #Play Button
        self.to_play = QtWidgets.QPushButton("Play", self)
        self.to_play.clicked.connect(self.to_play_screen)
        self.layout.addWidget(self.to_play, 1, 1, alignment = QtCore.Qt.AlignCenter)

    #TODO: Actually go to the deck editor
    def to_deck_screen(self):
        print("Work in Progress")

    #TODO: Actually go to play screen
    def to_play_screen(self):
        print("Work in Progress")

#Ideally this is obsolete and main.py should be run instead
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
