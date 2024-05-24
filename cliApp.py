import sys
import PySide6.QtCore as psqt_core
import PySide6.QtWidgets as psqt_widg


class MainWindow(psqt_widg.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(sys.argv[1])

        self.lineedit = psqt_widg.QLineEdit()
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText(sys.argv[2])

        # widget.setReadOnly(True) # uncomment this to make readonly

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)

        self.setCentralWidget(self.lineedit)

    def return_pressed(self):
        print("Return pressed!")
        self.lineedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_changed(self, text):
        print("Text changed...")
        print(text)

    def text_edited(self, text):
        print("Text edited...")
        print(text)

app = psqt_widg.QApplication(sys.argv)

window = psqt_widg.QMainWindow()
window.show()  # recall, this is invisible by default

app.exec()  # main event loop
# `python cliApp.py "Poser App" "text me to test me"`