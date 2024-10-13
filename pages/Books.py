from PyQt6.QtWidgets import QWidget,QLabel,QVBoxLayout


class BooksPage(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout=QVBoxLayout()
        layout.addWidget(QLabel("Books"))
        self.setLayout(layout)
        self.show()
        