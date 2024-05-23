import sys
import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


# stuff here

app = psqt_widg.QApplication(sys.argv)

window = psqt_widg.QMainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
