# This Python file uses the following encoding: utf-8
from PySide6 import QtCore, QtWidgets

import sys

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from widget.py import Widget

#Might want to consider making this a QMainWindow instead of QSStackedWidget
class Main(QtWidgets.QStackedWidget):
    #TODO: All of this
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()   #IDK What this does, look into it
        self.ui.setupUi(self)

        #Create the different screens and add them to the stack
        self.home = Widget(self)
        self.addWidget(self.home)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
