import sys
from PySide2.QtWidgets import QApplication, QSlider, QLayout, QWidget, QVBoxLayout
from PySide2.QtGui import QPainter, QPaintEvent, QPen
from PySide2 import QtCore

class monPainter (QWidget):
    def __init__ (self, parent=None) :
        super(monPainter, self).__init__(parent)

        self.setMinimumSize(100,100)
        self.valeur=0

    def setValeur (self, val):
        if val<0 : val=0
        if val>100 : val=100
        self.valeur = val
        self.update()

    def paintEvent (self, event:QPaintEvent):
        p = QPainter(self)
        p.setBrush(QtCore.Qt.blue)

        taille = min(self.width(), self.height())

        p.drawRect (10, 10, taille-20, taille-20)
        p.setBrush(QtCore.Qt.yellow)
        p.drawEllipse(20,20,taille-40, taille-40)

        p.save()

        p.translate(taille/2, taille/2)
        p.rotate(135+(self.valeur*270/100))

        pen = QPen(QtCore.Qt.black, 10)
        p.setPen(pen)
        p.drawLine (0,0,(taille-40)/3,0)

        p.restore()

        pen = QPen(QtCore.Qt.black, 5)
        p.setPen(pen)
        p.setBrush(QtCore.Qt.red)
        p.drawEllipse((taille/2)-20, (taille/2)-20,40,40)

class maFenetreprincipale(QWidget):
    def __init__(self, parent=None) :
        super(maFenetreprincipale, self).__init__(parent)

        self.compteur = monPainter()
        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.setMinimumSize(200,200)

        layout = QVBoxLayout()
        layout.addWidget(self.compteur)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self.compteur.setValeur)

if __name__ == '__main__' :
    app=QApplication(sys.argv)
    fen = maFenetreprincipale()
    fen.show()
    sys.exit(app.exec_())