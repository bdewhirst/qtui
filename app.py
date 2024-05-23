import sys
import random

import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


window_titles = [
    "An App",
    "The App",
    "Some App",
    "This App",
]

# from a tutorial on signals, slots, and events. part 2.
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("Brian's App")
        self.setFixedSize(psqt_core.QSize(300, 400))  # opens to this size
        self.setMinimumSize(psqt_core.QSize(250, 300))  # specifies smallest size
        self.setMaximumSize(psqt_core.QSize(600, 900))  # specifies largest size

        self.button = psqt_widg.QPushButton("Please press here.")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("This button has been clicked.")
        new_window_title = random.choice(window_titles)
        print("Setting title:  %s" % window_title)
        if window_title == "Something went wrong":
            self.button.setDisabled(True)

        # update window title:
        self.setWindowTitle("A oneshot app based on a tutorial")


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
