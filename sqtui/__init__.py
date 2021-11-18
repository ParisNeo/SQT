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

# Import Qt stuff (either PyQt5 or PySide2)
import importlib
def module_exist(module_name:str)->bool:
    """Verifies if a module exists

    Args:
        module_name (str): The name of the module to be verified

    Returns:
        bool: True if the module exists False else
    """
    module_spec = importlib.util.find_spec(module_name)
    try:
        m = importlib.import_module(module_name+".QtCore")
        return module_spec is not None
    except:
        return False

#Used to force using one libray or the other        
if 'PYQTGRAPH_QT_LIB' in os.environ.keys():
    qtlib = os.environ['PYQTGRAPH_QT_LIB']
else:
    qtlib = None
 
if qtlib is None and module_exist("PyQt5") or qtlib=="PyQt5":
    from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
    from PyQt5 import uic

    # If we reached this place, then PyQt is installed and will be used
    # Add this library environment variable to tell pyqtgraph to use PyQt5 as bachend
    os.environ['PYQTGRAPH_QT_LIB']="PyQt5"    
    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name:str, main_class:object)->QtWidgets.QWidget:
            """Loads a QtDesigner ui file and returns an object containing the widget or window loaded from the file
            you may access all UI components using their names
            Parameters
            ----------
            ui_file_name str or Path: The name of the file to be loaded
            main_class Qt class: A class type to put the loaded file in, for example QtWidgets.QWidget (required in pyqt but not in pyside2)
            """  
            obj = main_class()
            uic.loadUi(ui_file_name, obj)
            return obj

elif module_exist("PySide2"):
    from PySide2 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PySide2.QtCore import Signal, Slot
    from PySide2.QtUiTools import QUiLoader
    # If we reached this place, then PySide2 is installed and will be used
    # Add this library environment variable to tell pyqtgraph to use PySide2 as bachend
    os.environ['PYQTGRAPH_QT_LIB']="PySide2"

    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name:str, main_class:object)->QtWidgets.QWidget:
            """Loads a QtDesigner ui file and returns an object containing the widget or window loaded from the file
            you may access all UI components using their names
            Parameters
            ----------
            ui_file_name str or Path: The name of the file to be loaded
            main_class Qt class: A class type to put the loaded file in, for example QtWidgets.QWidget (required in pyqt but not in pyside2)
            """              
            ui_file = QtCore.QFile(ui_file_name)
            ui_file.open(QtCore.QFile.ReadOnly)

            loader = QUiLoader()
            obj = loader.load(ui_file)
            return obj
else:
    raise Exception("No compatible QT library detected")

# If none of these is found, you'll get an error in your code.
# You have to install one of the two libraries

