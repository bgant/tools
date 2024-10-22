#!/usr/bin/python
#
# pip install pyqt  <-- DO NOT USE brew install pyqt

from sys import exit
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from vitals_python_check import Check

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.check = Check()
        self.check.init()
        self.tests = {'link':self.check.link,
                 'router':self.check.router,
                 'dhcp':self.check.dhcp,
                 'internet':self.check.traceroute,
                 'dns':self.check.dns}
        self.UI()

    def UI(self):
        self.internet_image = QLabel(self)
        self.internet_image.setPixmap(QPixmap('vitals_internet_grey.png'))
        self.internet_image.move(15,10)

        self.dns_image = QLabel(self)
        self.dns_image.setPixmap(QPixmap('vitals_dns_grey.png'))
        self.dns_image.move(125,13)

        self.router_image = QLabel(self)
        self.router_image.setPixmap(QPixmap('vitals_router_grey.png'))
        self.router_image.move(5,140)

        self.dhcp_image = QLabel(self)
        self.dhcp_image.setPixmap(QPixmap('vitals_dhcp_grey.png'))
        self.dhcp_image.move(115,130)

        self.link_image = QLabel(self)
        self.link_image.setPixmap(QPixmap('vitals_link_grey.png'))
        self.link_image.move(75,225)

        button_run = QPushButton('Run Test', self)
        button_run.clicked.connect(self.on_button_run_click)
        #button_run.setFixedSize(120,100)
        button_run.move(70,330)

        button_close = QPushButton("Quit", self)
        button_close.clicked.connect(self.close)
        #button_close.resize(120,60)
        button_close.move(70, 365)

        self.setGeometry(300,300,220,400)
        self.setWindowTitle('Networking')
        self.show()

    def on_button_run_click(self):
        print('---Re-initializing Check module---')
        self.check.init() 
        for device,test in self.tests.items():
            self.change_image(device,'grey') # Reset Images
        for device,test in self.tests.items():
            print(f'Running check.{device}')
            if test():
                self.change_image(device,'green')
            else:
                self.change_image(device,'red')
                if device in ['link','router']:
                    break
        print('---Done---')

    def change_image(self, device, color):
        image    = f'vitals_{device}_{color}.png'
        function = f'self.{device}_image.setPixmap(QPixmap(\'{image}\'))'
        exec(f'x={function}')
        self.x()

def main():
    app = QApplication([])
    window = Window()
    exit(app.exec())

if __name__ == '__main__':
    main()

