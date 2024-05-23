import sys

import PySide6.QtWidgets as psqt_widg


# from a tutorial on signals, slots, and events. part 4. (on events)
# remember-- decouple / loosely couple; separate effects from what triggers them
class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = psqt_widg.QLabel("Click in this window, please")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    # more complex events are possible, such as labels by which button (left, middle, right) was pressed, etc.


app = psqt_widg.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
