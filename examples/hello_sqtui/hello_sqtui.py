"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
An example application to show how to use this library
"""
# pyqt5 style -------------------------------------------------------------------------
# from PyQt5 import QtWidgets
# -------------------------------------------------------------------------------------

# pyside2 style -----------------------------------------------------------------------
# from PySide2 import QtWidgets
# -------------------------------------------------------------------------------------

# sqtui style -------------------------------------------------------------------------
# Optional (explicitely select the backend library), if not specified, sqtui will search for available libraries and will coose PyQt5 over PySide2
import os
os.environ['PYQTGRAPH_QT_LIB']="PyQt5" # os.environ['PYQTGRAPH_QT_LIB']="PySide2"
# Now import from the sqtui library
from sqtui import QtWidgets
# -------------------------------------------------------------------------------------

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Creates a QMainWindow class
        """
        QtWidgets.QMainWindow.__init__(self)
        self.btn = QtWidgets.QPushButton("Hello")
        self.setCentralWidget(self.btn)
        self.setMinimumWidth(500)
        self.setWindowTitle("Hello SQTUI")
        self.btn.clicked.connect(self.helloPressed)
        self.show()

    def helloPressed(self):
        """ A slot triggered by pressing the Hello button
        """
        QtWidgets.QMessageBox.information(self, "Hello SQTUI", "Hello SQTUI")

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app: # sinon on crée une instance de QApplication
        app = QtWidgets.QApplication([])
    ui = MainWindow()
    sys.exit(app.exec_())


