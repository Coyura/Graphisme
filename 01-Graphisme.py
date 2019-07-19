import sys
from PySide2.QtWidgets import (QApplication, QWidget)
from PySide2.QtGui import QPainter, QPaintEvent
from PySide2 import QtCore

class monPainter (QWidget):
    def __init__ (self, parent=None) :
        super(monPainter, self).__init__(parent)

    def paintEvent (self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.blue)
        p.drawRect (10, 10, self.width()-20, self.height()-20)
        p.setBrush(QtCore.Qt.yellow)
        p.drawEllipse(20,20,self.width()-40, self.height()-40)
        p.setBrush(QtCore.Qt.green)
        p.drawEllipse(30,30,self.width()-60, self.height()-60 )

if __name__ == '__main__':
    app=QApplication(sys.argv)
    monP = monPainter()
    monP.show()
    sys.exit(app.exec_())