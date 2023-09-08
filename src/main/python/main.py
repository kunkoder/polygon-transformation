from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from math import*
import sys

class paint(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 700)
class navigasi(QWidget):
    def __init__(self):
        super().__init__()   
        self.setMinimumSize(800, 700)
        self.buatGrupBoxTranslasi()
        self.buatGrupBoxSkala()
        self.buatGrupBoxRotasi()
        self.buatGrupBoxKordinat()
        self.buatTabMenu()
        self.setGeometry(250, 250, 800, 700)
        self.setWindowTitle("Transformasi 2D")
        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.canvas = paint()
        self.flag_1 = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = False
        self.flag_5 = False
        self.flag_6 = False
        self.flag_7 = False
        self.flag_8 = False
        self.flag_9 = False
        self.flag_10 = False
        gridBox = QGridLayout()
        gridBox.addWidget(self.tabMenu, 0, 0)
        gridBox.addWidget(self.canvas, 0, 1, 2, 2)
        self.setLayout(gridBox)
    def buatGrupBoxTranslasi(self):
        self.grupBoxTranslasi = QGroupBox("Translasi")
        self.tbTransAtas = QPushButton("Atas", self)
        self.tbTransAtas.clicked.connect(self.onTransAtas)
        self.tbTransKiri = QPushButton("Kiri", self)
        self.tbTransKiri.clicked.connect(self.onTransKiri)
        self.tbTransKanan = QPushButton("Kanan", self)
        self.tbTransKanan.clicked.connect(self.onTransKanan)
        self.tbTransBawah = QPushButton("Bawah", self)
        self.tbTransBawah.clicked.connect(self.onTransBawah)
        tbTransAtasHbox = QHBoxLayout()
        tbTransAtasHbox.addWidget(self.tbTransAtas)
        tbTransTengahHbox = QHBoxLayout()
        tbTransTengahHbox.addWidget(self.tbTransKiri)
        tbTransTengahHbox.addWidget(self.tbTransKanan)
        tbTransBawahHbox = QHBoxLayout()
        tbTransBawahHbox.addWidget(self.tbTransBawah)
        tbTransVbox = QVBoxLayout()
        tbTransVbox.addLayout(tbTransAtasHbox)
        tbTransVbox.addLayout(tbTransTengahHbox)
        tbTransVbox.addLayout(tbTransBawahHbox)
        self.grupBoxTranslasi.setLayout(tbTransVbox)
    def buatGrupBoxSkala(self):
        self.grupBoxSkala = QGroupBox("Skala")
        self.tbSkalaKecil = QPushButton("Kecil", self)
        self.tbSkalaKecil.clicked.connect(self.onSkalaKecil)
        self.tbSkalaBesar = QPushButton("Besar", self)
        self.tbSkalaBesar.clicked.connect(self.onSkalaBesar)
        tbSkalaVbox = QVBoxLayout()
        tbSkalaVbox.addWidget(self.tbSkalaKecil)
        tbSkalaVbox.addWidget(self.tbSkalaBesar)
        self.grupBoxSkala.setLayout(tbSkalaVbox)
    def buatGrupBoxRotasi(self):
        self.grupBoxRotasi = QGroupBox("Rotasi")
        self.tbRotasiKiri = QPushButton("Putar Kiri",self)
        self.tbRotasiKiri.clicked.connect(self.onRotasiKiri)
        self.tbRotasiKanan = QPushButton("Putar Kanan", self)
        self.tbRotasiKanan.clicked.connect(self.onRotasiKanan)
        tbRotasiHbox = QHBoxLayout()
        tbRotasiHbox.addWidget(self.tbRotasiKiri)
        tbRotasiHbox.addWidget(self.tbRotasiKanan)
        self.grupBoxRotasi.setLayout(tbRotasiHbox)
    def buatGrupBoxKordinat(self):
        self.grupBoxKordinat = QGroupBox("Titik Kordinat")
        labelKordinatX1 = QLabel("Kordinat X1")
        labelKordinatY1 = QLabel("Kordinat Y1")
        self.listX1 = QListWidget()
        self.listY1 = QListWidget()
        korLabeHbox_1 = QHBoxLayout()
        korLabeHbox_1.addWidget(labelKordinatX1)
        korLabeHbox_1.addWidget(labelKordinatY1)
        korListHbox_1 = QHBoxLayout()
        korListHbox_1.addWidget(self.listX1)
        korListHbox_1.addWidget(self.listY1)
        labelKordinatX2 = QLabel("Kordinat X2")
        labelKordinatY2 = QLabel("Kordinat Y2")
        self.listX2 = QListWidget()
        self.listY2 = QListWidget()
        korLabeHbox_2 = QHBoxLayout()
        korLabeHbox_2.addWidget(labelKordinatX2)
        korLabeHbox_2.addWidget(labelKordinatY2)
        korListHbox_2 = QHBoxLayout()
        korListHbox_2.addWidget(self.listX2)
        korListHbox_2.addWidget(self.listY2)
        labelKordinatX3 = QLabel("Kordinat X3")
        labelKordinatY3 = QLabel("Kordinat Y3")
        self.listX3 = QListWidget()
        self.listY3 = QListWidget()
        korLabeHbox_3 = QHBoxLayout()
        korLabeHbox_3.addWidget(labelKordinatX3)
        korLabeHbox_3.addWidget(labelKordinatY3)
        korListHbox_3 = QHBoxLayout()
        korListHbox_3.addWidget(self.listX3)
        korListHbox_3.addWidget(self.listY3)
        labelKordinatX4 = QLabel("Kordinat X4")
        labelKordinatY4 = QLabel("Kordinat Y4")
        self.listX4 = QListWidget()
        self.listY4 = QListWidget()
        korLabeHbox_4 = QHBoxLayout()
        korLabeHbox_4.addWidget(labelKordinatX4)
        korLabeHbox_4.addWidget(labelKordinatY4)
        korListHbox_4 = QHBoxLayout()
        korListHbox_4.addWidget(self.listX4)
        korListHbox_4.addWidget(self.listY4)
        korVbox = QVBoxLayout()
        korVbox.addLayout(korLabeHbox_1)
        korVbox.addLayout(korListHbox_1)
        korVbox.addLayout(korLabeHbox_2)
        korVbox.addLayout(korListHbox_2)
        korVbox.addLayout(korLabeHbox_3)
        korVbox.addLayout(korListHbox_3)
        korVbox.addLayout(korLabeHbox_4)
        korVbox.addLayout(korListHbox_4)
        self.grupBoxKordinat.setLayout(korVbox)
    def buatTabMenu(self):
        self.tabMenu = QTabWidget()
        tab1 = QWidget()
        self.tbReset = QPushButton("Reset", self)
        self.tbReset.clicked.connect(self.onReset)
        self.gridBoxTrans = QGridLayout()
        self.gridBoxTrans.addWidget(self.grupBoxTranslasi, 0, 0)
        self.gridBoxTrans.addWidget(self.grupBoxSkala, 1, 0)
        self.gridBoxTrans.addWidget(self.grupBoxRotasi, 2, 0)
        self.gridBoxTrans.addWidget(self.tbReset, 3, 0)
        self.gridBoxTrans.addWidget(self.grupBoxKordinat, 4, 0)
        tab1.setLayout(self.gridBoxTrans)
        tab2 = QWidget()
        grupBoxTitikA = QGroupBox("Titik A")
        labelTitikX1 = QLabel("Kordinat X1 : ")
        labelTitikY1 = QLabel("Kordinat Y1 : ")
        self.inputTitikX1 = QLineEdit()
        self.inputTitikX1.setValidator(QIntValidator(self.inputTitikX1))
        self.inputTitikY1 = QLineEdit()
        hboxTitikA_1 = QHBoxLayout()
        hboxTitikA_1.addWidget(labelTitikX1)
        hboxTitikA_1.addWidget(self.inputTitikX1)
        hboxTitikA_2 = QHBoxLayout()
        hboxTitikA_2.addWidget(labelTitikY1)
        hboxTitikA_2.addWidget(self.inputTitikY1)
        vboxTitikA = QVBoxLayout()
        vboxTitikA.addLayout(hboxTitikA_1)
        vboxTitikA.addLayout(hboxTitikA_2)
        grupBoxTitikA.setLayout(vboxTitikA)
        grupBoxTitikB = QGroupBox("Titik B")
        labelTitikX2 = QLabel("Kordinat X2 : ")
        labelTitikY2 = QLabel("Kordinat Y2 : ")
        self.inputTitikX2 = QLineEdit()
        self.inputTitikY2 = QLineEdit()
        hboxTitikB_1 = QHBoxLayout()
        hboxTitikB_1.addWidget(labelTitikX2)
        hboxTitikB_1.addWidget(self.inputTitikX2)
        hboxTitikB_2 = QHBoxLayout()
        hboxTitikB_2.addWidget(labelTitikY2)
        hboxTitikB_2.addWidget(self.inputTitikY2)
        vboxTitikB = QVBoxLayout()
        vboxTitikB.addLayout(hboxTitikB_1)
        vboxTitikB.addLayout(hboxTitikB_2)
        grupBoxTitikB.setLayout(vboxTitikB)
        grupBoxTitikC = QGroupBox("Titik C")
        labelTitikX3 = QLabel("Kordinat X3 : ")
        labelTitikY3 = QLabel("Kordinat Y3 : ")
        self.inputTitikX3 = QLineEdit()
        self.inputTitikY3 = QLineEdit()
        hboxTitikC_1 = QHBoxLayout()
        hboxTitikC_1.addWidget(labelTitikX3)
        hboxTitikC_1.addWidget(self.inputTitikX3)
        hboxTitikC_2 = QHBoxLayout()
        hboxTitikC_2.addWidget(labelTitikY3)
        hboxTitikC_2.addWidget(self.inputTitikY3)
        vboxTitikC = QVBoxLayout()
        vboxTitikC.addLayout(hboxTitikC_1)
        vboxTitikC.addLayout(hboxTitikC_2)
        grupBoxTitikC.setLayout(vboxTitikC)
        grupBoxTitikD = QGroupBox("Titik D")
        labelTitikX4 = QLabel("Kordinat X4 : ")
        labelTitikY4 = QLabel("Kordinat Y4 : ")
        self.inputTitikX4 = QLineEdit()
        self.inputTitikY4 = QLineEdit()
        hboxTitikD_1 = QHBoxLayout()
        hboxTitikD_1.addWidget(labelTitikX4)
        hboxTitikD_1.addWidget(self.inputTitikX4)
        hboxTitikD_2 = QHBoxLayout()
        hboxTitikD_2.addWidget(labelTitikY4)
        hboxTitikD_2.addWidget(self.inputTitikY4)
        vboxTitikD = QVBoxLayout()
        vboxTitikD.addLayout(hboxTitikD_1)
        vboxTitikD.addLayout(hboxTitikD_2)
        grupBoxTitikD.setLayout(vboxTitikD)
        self.okGAmbar = QPushButton("Gambar")
        self.okGAmbar.clicked.connect(self.onOkGambar)
        tab2Vbox = QVBoxLayout()
        tab2Vbox.addWidget(grupBoxTitikA)
        tab2Vbox.addWidget(grupBoxTitikB)
        tab2Vbox.addWidget(grupBoxTitikC)
        tab2Vbox.addWidget(grupBoxTitikD)
        tab2Vbox.addWidget(self.okGAmbar)
        tab2Vbox.addStretch()
        tab2.setLayout(tab2Vbox)
        self.tabMenu.addTab(tab1, "Transformasi")
        self.tabMenu.addTab(tab2, "Polygon")
    def sumbuXY(self, qp):
        pen = QPen(Qt.blue, 0.3, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(550, 0, 550, 700)
        qp.setPen(pen)
        qp.drawLine(300, 350, 800, 350)
    def onOkGambar(self):
        self.flag_1 = True
        self.update()
        self.setX1 = float(self.inputTitikX1.text())
        self.setY1 = float(self.inputTitikY1.text())
        self.setX2 = float(self.inputTitikX2.text())
        self.setY2 = float(self.inputTitikY2.text())
        self.setX3 = float(self.inputTitikX3.text())
        self.setY3 = float(self.inputTitikY3.text())
        self.setX4 = float(self.inputTitikX4.text())
        self.setY4 = float(self.inputTitikY4.text())
    def onTransAtas(self):
        self.flag_2 = True
        self.update()
    def onTransKiri(self):
        self.flag_3 = True
        self.update()
    def onTransKanan(self):
        self.flag_4 = True
        self.update()
    def onTransBawah(self):
        self.flag_5 = True
        self.update()
    def onSkalaKecil(self):
        self.flag_6 = True
        self.update()
    def onSkalaBesar(self):
        self.flag_7 = True
        self.update()
    def onRotasiKiri(self):
        self.flag_8 = True
        self.update()
    def onRotasiKanan(self):
        self.flag_9 = True
        self.update()
    def onReset(self):
        self.flag_10 = True
        self.update()
    def poli(self, qp, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
        qp.setBrush(QColor(200, 0, 0))
        points = [
            QPoint(X1+550,Y1+350),
            QPoint(X2+550,Y2+350),
            QPoint(X3+550,Y3+350),
            QPoint(X4+550,Y4+350)
            ]
        poly = QPolygon(points)
        qp.drawPolygon(poly)
    def paintEvent(self, parameter_buat_apaan_sih_ini):
        qp = QPainter()
        qp.begin(self)
        self.sumbuXY(qp)
        qp.end()
        if self.flag_1:
            try:
                qp = QPainter()
                qp.begin(self)
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_1 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_2:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setY1 -= 5
                self.setY2 -= 5
                self.setY3 -= 5
                self.setY4 -= 5
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_2 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_3:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setX1 -= 5
                self.setX2 -= 5
                self.setX3 -= 5
                self.setX4 -= 5
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_3 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_4:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setX1 += 5
                self.setX2 += 5
                self.setX3 += 5
                self.setX4 += 5
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_4 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_5:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setY1 += 5
                self.setY2 += 5
                self.setY3 += 5
                self.setY4 += 5
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_5 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_6:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setX1 /= 1.2
                self.setY1 /= 1.2
                self.setX2 /= 1.2
                self.setY2 /= 1.2
                self.setX3 /= 1.2
                self.setY3 /= 1.2
                self.setX4 /= 1.2
                self.setY4 /= 1.2
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_6 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_7:
            try:
                qp = QPainter()
                qp.begin(self)
                self.setX1 *= 1.2
                self.setY1 *= 1.2
                self.setX2 *= 1.2
                self.setY2 *= 1.2
                self.setX3 *= 1.2
                self.setY3 *= 1.2
                self.setX4 *= 1.2
                self.setY4 *= 1.2
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_7 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_8:
            try:
                rcos = cos(radians(-10))
                rsin = sin(radians(-10))
                rX1 = (self.setX1*rcos)-(self.setY1*rsin)
                rY1 = (self.setX1*rsin)+(self.setY1*rcos)
                rX2 = (self.setX2*rcos)-(self.setY2*rsin)
                rY2 = (self.setX2*rsin)+(self.setY2*rcos)
                rX3 = (self.setX3*rcos)-(self.setY3*rsin)
                rY3 = (self.setX3*rsin)+(self.setY3*rcos)
                rX4 = (self.setX4*rcos)-(self.setY4*rsin)
                rY4 = (self.setX4*rsin)+(self.setY4*rcos)
                qp = QPainter()
                qp.begin(self)
                self.setX1 = rX1
                self.setY1 = rY1
                self.setX2 = rX2
                self.setY2 = rY2
                self.setX3 = rX3
                self.setY3 = rY3
                self.setX4 = rX4
                self.setY4 = rY4
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_8 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_9:
            try:
                rcos = cos(radians(10))
                rsin = sin(radians(10))
                rX1 = (self.setX1*rcos)-(self.setY1*rsin)
                rY1 = (self.setX1*rsin)+(self.setY1*rcos)
                rX2 = (self.setX2*rcos)-(self.setY2*rsin)
                rY2 = (self.setX2*rsin)+(self.setY2*rcos)
                rX3 = (self.setX3*rcos)-(self.setY3*rsin)
                rY3 = (self.setX3*rsin)+(self.setY3*rcos)
                rX4 = (self.setX4*rcos)-(self.setY4*rsin)
                rY4 = (self.setX4*rsin)+(self.setY4*rcos)
                qp = QPainter()
                qp.begin(self)
                self.setX1 = rX1
                self.setY1 = rY1
                self.setX2 = rX2
                self.setY2 = rY2
                self.setX3 = rX3
                self.setY3 = rY3
                self.setX4 = rX4
                self.setY4 = rY4
                self.poli(qp, self.setX1, self.setY1, self.setX2, self.setY2, self.setX3, self.setY3, self.setX4, self.setY4)
                qp.end()
                self.flag_9 = False
                self.listX1.addItem(str(self.setX1))
                self.listY1.addItem(str(self.setY1))
                self.listX2.addItem(str(self.setX2))
                self.listY2.addItem(str(self.setY2))
                self.listX3.addItem(str(self.setX3))
                self.listY3.addItem(str(self.setY3))
                self.listX4.addItem(str(self.setX4))
                self.listY4.addItem(str(self.setY4))
            except:
                pass
        if self.flag_10:
            try:
                qp = QPainter()
                qp.begin(self)
                self.poli(qp, 0, 0, 0, 0, 0, 0, 0, 0)
                qp.end()
                self.flag_10 = False
                self.listX1.clear()
                self.listY1.clear()
                self.listX2.clear()
                self.listY2.clear()
                self.listX3.clear()
                self.listY3.clear()
                self.listX4.clear()
                self.listY4.clear()
            except:
                pass

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = navigasi()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)