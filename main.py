from PyQt5 import QtWidgets
import sys
from forms.Autorization import Autorization


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Autorization()
    application.show()
    sys.exit(app.exec())