import sys

import PySide6.QtGui as qt_gui
import PySide6.QtWidgets as qt_wdg


class MainWindow(qt_wdg.QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = qt_wdg.QMenu(self)
        context.addAction(qt_gui.QAction("test 1", self))
        context.addAction(qt_gui.QAction("test 2", self))
        context.addAction(qt_gui.QAction("test 3", self))
        # context.exec(e.globalPos())


app = qt_wdg.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
