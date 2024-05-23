import sys
import random

import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

# from a tutorial on signals, slots, and events. part 2.
# remember-- decouple / loosely couple; separate effects from what triggers them
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

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("This button has been clicked.")
        new_window_title = random.choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        # update window title:
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == "Something went wrong":  # note: 'something went wrong' is an element in that list
            self.button.setDisabled(True)


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
