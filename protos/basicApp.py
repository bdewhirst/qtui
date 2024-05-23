from PySide6.QtWidgets import QApplication, QWidget

# import sys  # needed only for commandline arguments

# Required: One and only one QApplication instance per app
# Pass sys.argv to use CL args for app
# or, alternatively, `QApplication([]) works too.

# app = QApplication(sys.argv)
app = QApplication([])

window = QWidget()
window.show()  # by default, they're hidden.
app.exec()  # main event loop starts here. "The" QApplication instance.
