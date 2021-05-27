"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
An example application to show how to use this library with pyqtgraph
You need to install pyqtgraph and numpy for this to work
"""
import sys
# pyqt5 style 
#from PyQt5 import QtWidgets
# pyside2 style 
#from PyQt5 import QtWidgets
# sqtui style
from sqtui import QtWidgets
import pyqtgraph as pg
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """Creates a QMainWindow class
        """
        QtWidgets.QMainWindow.__init__(self)
        self.plt = pg.PlotWidget(title="Three plot curves")
        x = np.arange(1000)
        y = np.random.normal(size=(3, 1000))
        for i in range(3):
            self.plt.plot(x, y[i], pen=(i,3))  ## setting pen=(i,3) automaticaly creates three different-colored pens
        self.setCentralWidget(self.plt)
        self.setMinimumWidth(500)
        self.setWindowTitle("Hello PyQtGraph")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app: # sinon on crée une instance de QApplication
        app = QtWidgets.QApplication([])
    ui = MainWindow()
    sys.exit(app.exec_())


