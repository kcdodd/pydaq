from PySide2 import QtCore, QtGui, QtWidgets

import sys
import numpy as np

from app.widgets.plot import MplFigure
import random

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MplRandomFigure( MplFigure ):

  gen = QtCore.Signal(np.ndarray)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    timer = QtCore.QTimer(self)
    timer.timeout.connect(self.generate_data)
    self.gen.connect(self.data)
    timer.start(100)

    self.gen.emit(np.array(([0, 1, 2, 3], [1, 2, 0, 4])))

  def generate_data(self):

    d = []

    for i in range(2):
      d.append([[0, 1, 2, 3], [random.randint(0, 10) for i in range(4)]])

    self.gen.emit(np.array(d))


class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)


        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MplRandomFigure(self.main_widget, width=5, height=4, dpi=100, colors = ["#05e1ff"])
        dc = MplRandomFigure(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()
