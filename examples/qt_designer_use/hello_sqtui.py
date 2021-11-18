"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
An example application to show how to use this library
"""
import sys


# pyqt5 style -------------------------------------------------------------------------
# from PyQt5 import QtWidgets, uic
# -------------------------------------------------------------------------------------

# pyside2 style -----------------------------------------------------------------------
# from PySide2 import QtWidgets
# from PySide2.QtUiTools import QUiLoader
# -------------------------------------------------------------------------------------

# sqtui style -------------------------------------------------------------------------
# Optional (explicitely select the backend library), if not specified, sqtui will search for available libraries and will coose PyQt5 over PySide2
import os
os.environ['PYQTGRAPH_QT_LIB']="PyQt5" # os.environ['PYQTGRAPH_QT_LIB']="PySide2"
# Now import from the sqtui library
from sqtui import QtWidgets, UIC
# -------------------------------------------------------------------------------------


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


