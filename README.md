# SQTUI
Safe QT User Interface.

This is a little library I've developed in order to wrap arount Qt for python libraries.
This librarty enables the user to seemlessly develop Qt applications with PyQt5 or PySide or in future versions other libraries without the need to change the coding.

## Motivation

PyQt5 is one of the best libraries I've worked with, it is opensource and enables fast and easy to use graphical interface developement.

The problem with PyQt is its licence. The licence of PyQt is GPL 3.0 which is a contaminating licence. This translates to a contamination of your own code with the GPL licence obliging you to apply all GPL details on your code, includig full access to your software code in all cases. The only way to get around this is to buy a comercial licence from [https://riverbankcomputing.com/commercial/pyqt](https://riverbankcomputing.com/commercial/pyqt).

While this is a good thing in some sense, sometimes, you want to keep your application licence separate from the libraries licence. For example, I do like the MIT licence and use it in all my opensource code because it is opensource but gives the liberty to reuse my code without imposing any restrictions on the apps that may use my library.

Other liraries such as PySide, have a little different syntax for example to load UI files or to to declare the signals. In the other hand PySide2 is under L-GPL licence, which is not as contaminating as the GPL, but still have some constraints. For example you must give your user the possibility to change the library and even use another one.

SQTUI is the answer i propose to all this. First, it has a unified coding style independently from the library behind. It enables you to code in a consistant way, and automatically select the library you want to use. This has multiple advantages:
- First, you get to choose if you want to have the GPL licence or no
- You are complient with the L-GPL requirements if you opt with using PySide
- You can compile your code using pyinstaller and hide some portions that may be protected with patents or simply you want to keep secret while respecting the licences requirements
- You can easily switch the library whenever you want.
- You code the same way. You just need to install the backend library of your choice and everything is done automatically

I hope that this library help others who loves using python but want to have more freedom on their licence. I encourage people to use opensource and share their code as much as possible.

**For those working in comercial companies, please consider buying the comercial Qt licence as it gives you more support and rewards the developers who created this wonderful tool.**

Consider using this library especially for keeping your licence free of GPL 3 contamination and give yourself the choice to use one library or another.

## Licence

This library is distributed under MIT licence since we do not distribute the backend libraries with it. If you opt in using pyqt5 as backend then your app is GPL 3.0 and everything gets contaminated. If you opt to use PySide, you get to keep your licence and you'll notice no difference as SQT does the translation between the two libraries seemlessly.

## How to install
Simply install it from pypi :
```
pip install sqtui
```
Please notice that we didn't add neither PyQt5 nor PySide to our requirements, so when you install sqtui, you need then to install one of the two supported libraries.

1- for pyqt5 :
```
pip install pyqt5
```

2- for pyside2 :
```
pip install pyside2
```

## Usage
### Classical Way (code)
Just import the classical pyqt5 or pyside2 libraries from sqtui instead of importing them from one or the other.

For example, here is an example of importing the most used modules :
```python
from sqtui import QtCore, QtGui, QtWidgets, QtOpenGL
```

Then use them normally for example :

```python
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
```

Advice : Only import the modules you need

### Qt designer Way
Designing the UI using a graphical interface speeds up the developement and saves time. If you have access to QtDesigner software, then you may use PyQt5 or PySide to load the file and use it directly. Unfortunately, the two libraries have different approaches to doing this.

To make this operation simple and transparent for users, SQTUI provides a wrapper class called UIC. UIC has a static method loadUi that can be used to load the ui files using the same syntax. No need to learn how PyQt5 is doing it or how PySide2 is doing it :

```python
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
```

Here for example, we have a QMainWindow interface with a button called btn. you can access any object inside the window using self.window.<the name of the object>. You can connect some slots to the signals and so. Check out the examples directory for more details.

## Building custom signals

One difference between pyqt5 and pyside2 is the signal naming. in pyqt5 signals are of type pyqtSignal found in qtcore package. In pyside, it is named Signal in QtCore package.

As Signal seems more neutral, I've chosen to go with that naming. Now whether you use PyQT5 or PySide, the naming is the same (Signal).
You can use signals to communicate between threads and the main thread that manages the UI.

In the following example, we create a thread that sends a count down message to the ui which displays it on the QLabel object, then when it is done, it emits another signal. The slot shows a messagebox telling the user that the countdown is done.

While this is not a very useful example, it illustrates how signals and slots come in handy when using multi threading. And having a single 

```python
from sqtui import QtCore, QtWidgets, Signal
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

```

## PyQtGraph 

pyqtgraph is a powerful scientific graphs plotter tool. It is more useful when it comes to plotting fast realtime data than matplotlib.
You can use pyqtgraph along with sqtui as pyqtgraph actually support using either of pyqt5 and pyside.

pyqtgraph needs this environment variable to be set correctly to select the right backend:
- PYQTGRAPH_QT_LIB

SQTUI, does this automatically, when it identifies the installed library, it sets this variable. So all you have to do is first import sqtui then import pyqtgraph.


In the following example, you'll need to install pyqtgraph and numpy. (use pip as shown for other libraries in How to install section)

```python
import sys
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

```
# Changelog

## V0.0.2 : 28/05/2021
- Added examples
- Added pyqtgraph integration
- Updated README

## V0.0.1 : 28/05/2021
- Initial code
