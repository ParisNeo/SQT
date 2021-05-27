# SQTUI
Safe QT User Interface.

This is a little library I've developed in order to wrap arount Qt for python libraries.
This librarty enables the user to seemlessly develop Qt applications with PyQt5 or PySide or in future versions other libraries without the need to change the coding.

## Motivation

PyQt5 is one of the best libraries I've worked with, it is opensource and enables fast and easy to use graphical interface developement.

The problem with PyQt is its licence. The licence of PyQt is GPL 3.0 which is a contaminating licence. This translates to a contamination of your own code with the GPL licence obliging you to apply all GPL details on your code, includig full access to your software code.

While this is a good thing in some sense, sometimes, you want to keep your application licence separate from the libraries licence. For example, I do like the MIT licence and use it in all my opensource code because it is opensource but gives the liberty to reuse my code without imposing any restrictions on the apps that may use my library.

Other liraries such as PySide, have a little different syntax for example to load UI files or to to declare the signals. In the other hand PySide2 is under L-GPL licence, which is not as contaminating as the GPL, but still sonstrains the fact that you must give your user the possibility to change the library and even use another one.

SQT is the answer to all this. First, it has a unified coding style independently from the library behind. It enables you to code in a consistant way, and automatically select the library you want to use. This has multiple advantages:
- First, you get to choose if you want to have the GPL licence or no
- You are complient with the L-GPL requirements if you opt with using PySide
- You can compile your code using pyinstaller and hide some portions that may be protected with patents or simply you want to keep secret while respecting the licences requirements
- You can easily switch the library whenever you want.
- You code the same way. You just need to install the backbone library of your choice and everything is done automatically

I hope that this library help others who loves using python but want to have more freedom on their licence.

## Licence

This library is distributed under MIT licence since we do not distribute the backend libraries with it. If you opt in using pyqt then your app is GPL and everything gets contaminated. If you opt to use PySide, you get to keep your licence and you'll notice no difference as SQT does the translation between the two libraries seemlessly.

## Use

<TODO>
