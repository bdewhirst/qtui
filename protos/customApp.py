import sys
import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


# theme: to customize main window, subclass QMainWindow
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Brian's Test App")
        button = psqt_widg.QPushButton("Please press here.")

        # n.b.: THE FOLLOWING APPLIES TO ANY WIDGET:
        # self.setFixedSize(psqt_core.QSize( 500, 700)  # note: prevents users from resizing
        # to specify without requiring fixed dimensions, there's also .setMinimumSize(), .setMaximumSize()
        self.setFixedSize(psqt_core.QSize(300, 400))  # opens to this size
        self.setMinimumSize(psqt_core.QSize(250, 300))  # specifies smallest size
        self.setMaximumSize(psqt_core.QSize(600, 900))  # specifies largest size

        self.setCentralWidget(button)  # add button as center widget


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
