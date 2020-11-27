import sys
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavToolbar


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setWindowTitle('MatPlotLib Example')
    main_window.setCentralWidget(GraphWidget())
    main_window.show()
    app.exec_()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # add tabs here using addTabs method


class GraphWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._figure = plt.Figure()

        # Widget
        self._canvas = FigureCanvas(self._figure)

        # Widget
        toolbar = NavToolbar(self._canvas, self)

        # Widget
        plot_button = QtWidgets.QPushButton('Plot!')
        plot_button.clicked.connect(self.plot)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self._canvas)
        layout.addWidget(plot_button)

        self.setLayout(layout)
        self.plot()

    def plot(self):
        data = np.random.rand(20)
        ax = self._figure.add_subplot(111)
        ax.plot(data, '*-')
        self.update_canvas()

    def update_canvas(self):
        self._canvas.draw()


if __name__ == '__main__':
    main()
