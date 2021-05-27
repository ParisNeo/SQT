"""
Environment : SQT
Author : Saifeddine ALOUI
Description :
A SQT environment for building UI applications
"""

from Environments.Environment import Environment

from pathlib import Path

# Import Qt stuff (either PyQt5 or PySide2)
import importlib
def module_exist(module_name):
    module_spec = importlib.util.find_spec(module_name)
    return module_spec is not None

if module_exist("PyQt5"):
    from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5 import uic
    
    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name, main_class):
            obj = main_class()
            uic.loadUi(ui_file_name, obj)
            return obj

elif module_exist("PySide2"):
    from PySide2 import QtCore, QtGui, QtWidgets, QtOpenGL
    from PySide2.QtCore import Signal
    from PySide2.QtUiTools import QUiLoader
    class UIC():
        def __init__(self):
            pass
        @staticmethod
        def loadUi(ui_file_name, main_class):
            ui_file = QtCore.QFile(ui_file_name)
            ui_file.open(QtCore.QFile.ReadOnly)

            loader = QUiLoader()
            obj = loader.load(ui_file)
            return obj

