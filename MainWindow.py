from PyQt6.QtWidgets import QMainWindow,QStatusBar
from PyQt6.QtGui import QIcon
from pages.MainPage import  MainPage

from utils.Action import Action
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('./assets/icon.png'))
        self.setWindowTitle('Library System')
        self.setGeometry(100, 100, 500, 300)
        self.mainPage=MainPage()
        self.setCentralWidget(self.mainPage)
        menuBar=self.menuBar()
        menuBar.addAction(Action(menuBar,QIcon(),"Home","Go Home",self.openHome).QAction)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Library System v0.1')
        self.show()
    def openHome(self):
        self.mainPage.stackedLayout.setCurrentIndex(0)