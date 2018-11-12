import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide2 import QtCore, QtWidgets

import random
from numpy import arange, sin, pi
import numpy as np

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MplFigure(FigureCanvas):

  #-----------------------------------------------------------------------------
  def __init__(self,
    parent=None,
    width=5,
    height=4,
    dpi=100,
    colors = None,
    lines = None,
    markers = None,
    data = None ):
    """
    Parameters
    ----------
    colors : list
    lines : list
    markers : list
    data : array like
      Initial data
    """

    fig = Figure(figsize=(width, height), dpi=dpi)
    self.axes = fig.add_subplot(111)
    self.colors = colors
    self.lines = lines
    self.markers = markers

    super().__init__(fig)
    self.setParent(parent)

    FigureCanvas.setSizePolicy(self,
      QtWidgets.QSizePolicy.Expanding,
      QtWidgets.QSizePolicy.Expanding )

    FigureCanvas.updateGeometry(self)

    if data is not None:
      self.data(data)

  #-----------------------------------------------------------------------------
  @QtCore.Slot(list)
  def colors( self, colors):
    self.colors = colors

  #-----------------------------------------------------------------------------
  @QtCore.Slot(list)
  def lines( self, lines):
    self.lines = lines

  #-----------------------------------------------------------------------------
  @QtCore.Slot(list)
  def markers( self, markers):
    self.markers = markers

  #-----------------------------------------------------------------------------
  @QtCore.Slot(np.ndarray)
  def data( self, data ):
    data = np.asarray(data)

    self.axes.cla()

    if len(data.shape) == 2:
      x, y = data

      if self.colors is not None and len(self.colors) > 0:
        color = self.colors[0]
      else:
        color = None

      self.axes.plot(x, y, color = color)

    elif len(data.shape) == 3:

      for i, d in enumerate(data):
        if self.colors is not None and len(self.colors) > i:
          color = self.colors[i]
        else:
          color = None

        x, y = d

        self.axes.plot(x, y, color = color)

    self.draw()
