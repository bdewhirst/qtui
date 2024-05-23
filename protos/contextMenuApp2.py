import sys

import PySide6.QtGui as qt_gui
import PySide6.QtWidgets as qt_wdg


class MainWindow(qt_wdg.QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(
            Qt.CustomContextMenu
        )  # bugged-- possibly reliant on commercial-version features?
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = qt_wdg.QMenu(self)
        context.addAction(qt_gui.QAction("test 1", self))
        context.addAction(qt_gui.QAction("test 2", self))
        context.addAction(qt_gui.QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

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
