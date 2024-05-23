import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)
class MainWindow(QMainWindow):
    def __init__(self):
        pass  # many examples here: https://www.pythonguis.com/tutorials/pyside6-widgets/


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()