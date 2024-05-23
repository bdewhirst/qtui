import sys
from PySide6.QtWidgets import QApplication, QPushButton  # , QWidget()

app = QApplication(sys.argv)

window = QPushButton("Push Me")
# window = QWidget()
window.show()  # by default, they're hidden.

app.exec()  # main event loop starts here. "The" QApplication instance.
