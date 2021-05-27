"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
An example application to show how to use this library
"""
import sys
# pyqt5 style 
#from PyQt5 import QtWidgets
# pyside2 style 
#from PyQt5 import QtWidgets
# sqtui style
from sqtui import QtWidgets, QtCore, UIC
from pathlib import Path


class Container():
    def __init__(self):
        """Creates a Container for the window to be loaded from the .ui file
        """
        self.window = UIC.loadUi(Path(__file__).parent/"hello_sqtui.ui", QtWidgets.QMainWindow)
        self.window.btn.clicked.connect(self.helloPressed)
        self.window.show()

    def helloPressed(self):
        """ A slot triggered by pressing the Hello button
        """
        QtWidgets.QMessageBox.information(self.window, "Hello SQTUI", "Hello SQTUI")

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app: # sinon on crée une instance de QApplication
        app = QtWidgets.QApplication([])
    ui = Container()
    sys.exit(app.exec_())


