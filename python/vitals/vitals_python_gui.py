import sys
from PyQt6.QtGui import QPixmap, QImage, QImageReader
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from random import choice

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):

        self.images = ['vitals_dns_red.png',
                 'vitals_wifi_red.png',
                 'vitals_dns_green.png',
                 'vitals_wifi_green.png']

        self.dns_image = QLabel(self)
        self.dns_image.setPixmap(QPixmap('vitals_dns_grey.png'))
        self.dns_image.move(60,10)

        self.wifi_image = QLabel(self)
        self.wifi_image.setPixmap(QPixmap('vitals_wifi_grey.png'))
        self.wifi_image.move(50,110)

        button = QPushButton('Push Me', self)
        button.clicked.connect(self.on_button_click)
        #button.setFixedSize(120,100)
        button.move(10,300)

        self.setGeometry(300, 300, 200, 400)
        self.setWindowTitle('PyQt6')
        self.show()

    def on_button_click(self):
        self.wifi_image.setPixmap(QPixmap(choice(self.images)))

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

