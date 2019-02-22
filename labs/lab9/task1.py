import sys
#HELLOO
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
my_qt_app = QApplication(sys.argv)
my_window = QWidget()
my_window.setGeometry(0,0,400,300)
my_window.setWindowTitle('Denize Ignacio')
my_label = QLabel(my_window)
my_label.setText('Hi!')
#label = QLabel(self)
pixmap = QPixmap('pineapples.jpeg')
label.setPixmap(pixmap)
self.resize(pixmap.width(), pixmap.height())
my_window.show()
sys.exit(my_qt_app.exec_())

