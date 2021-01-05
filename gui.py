import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ui import *
import encrypt
import decrypt


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Messafge()
        self.ui.setupUi(self)

        self.ui.encrypt.clicked.connect(self.encrypt)
        self.ui.decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        try:
            text = self.ui.encrypt_input.toPlainText()
            crypt = encrypt.crypt(text)
            self.ui.encrypt_out.setText(crypt)
            self.ui.encrypt_out.update()
        except Exception as e:
            self.ui.encrypt_out.setText(f"ERROR: {e}")
            self.ui.encrypt_out.update()

    def decrypt(self):
        try:
            text = self.ui.decrypt_input.toPlainText()
            crypt = decrypt.encrypt(str(text))
            self.ui.decrypt_out.setText(crypt)
            self.ui.decrypt_out.update()
        except Exception as e:
            self.ui.decrypt_out.setText(f"ERROR: {e}")
            self.ui.decrypt_out.update()


if __name__ == '__main__':
    app = QApplication([])
    client = App()
    client.show()
    app.setWindowIcon(QIcon("icon.png"))
    sys.exit(app.exec())
