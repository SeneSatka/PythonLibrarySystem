from PyQt6.QtWidgets import QWidget,QVBoxLayout,QStackedLayout
from pages.Home import  HomePage
from pages.Users import UsersPage
from pages.Books import BooksPage
class MainPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stackedLayout = QStackedLayout()
        self.home=HomePage()
        self.home.usersButton.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(1))
        self.home.booksButton.clicked.connect(lambda: self.stackedLayout.setCurrentIndex(2))
        self.stackedLayout.addWidget(self.home)
        self.stackedLayout.addWidget(UsersPage())
        self.stackedLayout.addWidget(BooksPage())
        layout = QVBoxLayout()
        layout.addLayout(self.stackedLayout)
        self.setLayout(layout)
        self.show()