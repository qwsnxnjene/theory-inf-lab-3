import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from main import huffman_encoding, huffman_decoding
from main_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.openFileButton.clicked.connect(self.open_file)
        self.codeTextButton.clicked.connect(self.code_text)
        self.saveCodedTextButton.clicked.connect(self.save_coded_file)

        self.openCodedFileButton.clicked.connect(self.open_coded_file)
        self.decodeTextButton.clicked.connect(self.decode_text)

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
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        self.textCoded.setText(self.coded_text[:100_000])
        self.textCoded.setText(self.coded_text[100_000:200_000])
        self.textCoded.setText(self.coded_text[200_000:300_000])
        self.saveCodedTextButton.setEnabled(True)
        QApplication.restoreOverrideCursor()

    def save_coded_file(self):
        try:
            binary_data = bytearray()
            for i in range(0, len(self.coded_text), 8):
                chunk = self.coded_text[i:i + 8]
                if chunk:
                    byte_value = int(chunk, 2)
                    binary_data.append(byte_value)

            with open('great.bin', 'wb') as f:
                f.write(binary_data)
        except Exception as e:
            print(e)

    def open_coded_file(self):
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        with open('great.bin', 'rb') as f:
            binary_data = f.read()

        binary_string = ''
        for byte in binary_data:
            binary_string += f'{byte:08b}'
        self.text = binary_string
        self.textOriginal_2.setText(self.text[:100_000])
        self.textOriginal_2.append(self.text[100_000:200_000])
        self.textOriginal_2.append(self.text[200_000:300_000])
        self.decodeTextButton.setEnabled(True)
        QApplication.restoreOverrideCursor()

    def decode_text(self):
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        coded_text = self.text
        code = huffman_decoding(coded_text, self.codes).replace('\\n', '\n').replace('\\xa0', '\xa0')
        self.textCoded_2.setText(code)
        QApplication.restoreOverrideCursor()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()