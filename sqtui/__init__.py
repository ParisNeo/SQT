"""
Library     : SQTUI
Author      : Saifeddine ALOUI aka ParisNeo
Description :
A QT libraries wrapper for building UI applications
"""


# Import Qt stuff (either PyQt5 or PySide2)
from pathlib import Path
import importlib
import os

def module_exist(module_name):
    """Detects if a module exists
    """
    module_spec = importlib.util.find_spec(module_name)
    return module_spec is not None

# Detect PyQt5
if module_exist("PyQt5"):
    from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5 import uic
    
    # If we reached this place, then PyQt is installed and will be used
    # Add this library environment variable to tell pyqtgraph to use PyQt5 as bachend
    os.environ['PYQTGRAPH_QT_LIB']="PyQt5"

    # UIC is a wrapper to load QTDesigner UI files in the same way independently on the backend library
    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name, main_class):
            """Loads a QtDesigner ui file and returns an object containing the widget or window loaded from the file
            you may access all UI components using their names
            Parameters
            ----------
            ui_file_name str or Path: The name of the file to be loaded
            main_class Qt class: A class type to put the loaded file in, for example QtWidgets.QWidget
            """
            obj = main_class()
            uic.loadUi(str(ui_file_name), obj)
            return obj

# Detect PySide2
elif module_exist("PySide2"):
    from PySide2 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PySide2.QtCore import Signal
    from PySide2.QtUiTools import QUiLoader

    # If we reached this place, then PySide2 is installed and will be used
    # Add this library environment variable to tell pyqtgraph to use PySide2 as bachend
    os.environ['PYQTGRAPH_QT_LIB']="PySide2"

    # UIC is a wrapper to load QTDesigner UI files in the same way independently on the backend library
    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name, main_class=None):
            """Loads a QtDesigner ui file and returns an object containing the widget or window loaded from the file
            you may access all UI components using their names
            Parameters
            ----------
            ui_file_name str or Path: The name of the file to be loaded
            main_class Qt class: A class type to put the loaded file in, for example QtWidgets.QWidget (required in pyqt but not in pyside2)
            """            
            ui_file = QtCore.QFile(str(ui_file_name))
            ui_file.open(QtCore.QFile.ReadOnly)

            loader = QUiLoader()
            obj = loader.load(ui_file)
            return obj

# If none of these is found, you'll get an error in your code.
# You have to install one of the two libraries

