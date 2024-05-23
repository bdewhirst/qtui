import sys
import random

import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


# from a tutorial on signals, slots, and events. part 3.
# remember-- decouple / loosely couple; separate effects from what triggers them
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("Brian's App")
        self.setFixedSize(psqt_core.QSize(300, 400))  # opens to this size
        self.setMinimumSize(psqt_core.QSize(250, 300))  # specifies smallest size
        self.setMaximumSize(psqt_core.QSize(600, 900))  # specifies largest size

        self.label = psqt_widg.QLabel()

        self.input = psqt_widg.QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = psqt_widg.QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = psqt_widg.QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
