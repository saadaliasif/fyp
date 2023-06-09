from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor, QFont, QPixmap
from main import *
import sys
from qt_material import apply_stylesheet

app = QtWidgets.QApplication(sys.argv)
apply_stylesheet(app, theme='light_blue.xml')
window=loginrun()
window.show()
sys.exit(app.exec())