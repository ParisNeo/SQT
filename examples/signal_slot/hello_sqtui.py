"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
An example application to show how to use this library
"""

# pyqt5 style -------------------------------------------------------------------------
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import pyqtSignal
# -------------------------------------------------------------------------------------

# pyside2 style -----------------------------------------------------------------------
# from PySide2 import QtWidgets
# from PySide2.QtCore import Signal

# -------------------------------------------------------------------------------------

# sqtui style -------------------------------------------------------------------------
# Optional (explicitely select the backend library), if not specified, sqtui will search for available libraries and will coose PyQt5 over PySide2
import os
os.environ['PYQTGRAPH_QT_LIB']="PyQt5" # os.environ['PYQTGRAPH_QT_LIB']="PySide2"
# Now import from the sqtui library
from sqtui import QtWidgets, QtWidgets, Signal
# -------------------------------------------------------------------------------------

import sys

import time

class MainWindow(QtWidgets.QMainWindow):
    thread_sent_count = Signal(int)
    thread_sent_done = Signal()

    def __init__(self):
        """Creates a QMainWindow class
        """
        QtWidgets.QMainWindow.__init__(self)
        self.lbl=QtWidgets.QLabel(f"Counter from another thread : {0}")
        self.lbl.setStyleSheet("font-size:24px;")
        self.setCentralWidget(self.lbl)
        self.setMinimumWidth(500)
        self.setWindowTitle("Signal slot test")
        self.thread_sent_count.connect(self.count)
        self.thread_sent_done.connect(self.done)
        self.some_thread = QtCore.QThread()
        self.some_thread.run=self.run
        self.some_thread.start()
        self.show()
    
    def run(self):
        """Thread funtion
        """
        self.thread_sent_count.emit(5)
        time.sleep(1)
        self.thread_sent_count.emit(4)
        time.sleep(1)
        self.thread_sent_count.emit(3)
        time.sleep(1)
        self.thread_sent_count.emit(2)
        time.sleep(1)
        self.thread_sent_count.emit(1)

        # Send hello to main thread
        self.thread_sent_done.emit()
        # That's it


    def count(self, count:int):
        """ A slot triggered by emitting thread_sent_count signal while sending an integer
        """
        self.lbl.setText(f"Counter from another thread : {count}")


    def done(self):
        """ A slot triggered by emitting thread_sent_hello signal
        """
        QtWidgets.QMessageBox.information(self, "Done", "Countdown is done")

if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app: # sinon on crée une instance de QApplication
        app = QtWidgets.QApplication([])
    ui = MainWindow()
    sys.exit(app.exec_())


