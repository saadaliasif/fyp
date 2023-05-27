from PySide6 import QtWidgets
from main import *
import sys

app = QtWidgets.QApplication(sys.argv)
File=open("stylesheet.qss",'r')
with File:
    qss=File.read()
    app.setStyleSheet(qss)
window=loginrun()
window.show()
sys.exit(app.exec())