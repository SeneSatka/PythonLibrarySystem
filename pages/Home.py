from PyQt6.QtWidgets import QWidget,QVBoxLayout,QPushButton

class HomePage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout()
        self.usersButton= QPushButton("Users")
        layout.addWidget(self.usersButton)
        self.booksButton= QPushButton("Books")
        layout.addWidget(self.booksButton)
        self.setLayout(layout)
        self.show()