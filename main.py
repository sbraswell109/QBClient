# This Python file uses the following encoding: utf-8
from PySide6 import QtCore, QtWidgets

import sys

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from home_screen import HomeScreen
from game_ui import GameUI

#Might want to consider making this a QMainWindow instead of QSStackedWidget
class Main(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   #IDK What this does, look into it
        self.ui.setupUi(self)

        #Create the different screens and add them to the stack
        self.child_widgets = dict() #Key:value is objectName:index in stack
        self.add_to_stack(HomeScreen(self))
        self.add_to_stack(GameUI(self))




    #Helper function to make adding a little easier in case things need to change
    def add_to_stack(self, widget: str):
        self.child_widgets[widget.objectName()] = self.addWidget(widget)


    #Changes the current widget referred to by name
    def change_screen(self, name):
        widget_index = self.child_widgets[name]
        self.setCurrentWidget(self.widget(widget_index))
        self.setCurrentIndex(widget_index)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
