import sys
import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


# from a tutorial on signals, slots, and events.
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Brian's App")
        self.setFixedSize(psqt_core.QSize(300, 400))  # opens to this size
        self.setMinimumSize(psqt_core.QSize(250, 300))  # specifies smallest size
        self.setMaximumSize(psqt_core.QSize(600, 900))  # specifies largest size

        button = psqt_widg.QPushButton("Please press here.")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("It was clicked.")


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
