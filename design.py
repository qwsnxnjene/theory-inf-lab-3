import sys

from PyQt6 import QtWidgets

from main import huffman_encoding
from main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.openFileButton.clicked.connect(self.open_file)
        self.codeTextButton.clicked.connect(self.code_text)
        self.saveCodedTextButton.clicked.connect(self.save_coded_file)

        self.text = ""
        self.codes = None
        self.coded_text = None

    def open_file(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                        'Open File',
                                                        './',
                                                        'Text Files (*.txt)')
        if not file:
            return
        f = open(file, 'r')
        self.text = f.read()
        self.textOriginal.setText(self.text)
        self.codeTextButton.setEnabled(True)

    def code_text(self):
        self.coded_text, self.codes = huffman_encoding(self.text)
        self.textCoded.setText(self.coded_text)
        self.saveCodedTextButton.setEnabled(True)

    def save_coded_file(self):
        try:
            name = QtWidgets.QFileDialog.getSaveFileName(self, 'Сохранить файл')[0]

            dict_str = ""
            for key, value in self.codes.items():
                dict_str += f'{key}: {value}\n'

            with open(f"{name}.txt", "w") as fh:
                fh.write(self.coded_text + ":" + dict_str)
        except Exception as e:
            print(e)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()