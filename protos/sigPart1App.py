import sys
import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


# from a tutorial on signals, slots, and events.
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("Brian's App")
        self.setFixedSize(psqt_core.QSize(300, 400))  # opens to this size
        self.setMinimumSize(psqt_core.QSize(250, 300))  # specifies smallest size
        self.setMaximumSize(psqt_core.QSize(600, 900))  # specifies largest size

        self.button = psqt_widg.QPushButton("Please press here.")
        self.button.setCheckable(True)
        self.button.released.connect(
            self.the_button_was_released
        )  # this fires when you let go of the mouse button
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print("release status:", self.button_is_checked)

    def the_button_was_clicked(self):
        print("It was clicked.")

    def the_button_was_toggled(self, checked):
        # here's how you store state
        self.button_is_checked = checked
        print("check status:", self.button_is_checked)


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
