from PyQt6.QtCore import QObject
from PyQt6.QtGui import QIcon, QAction
class Action():
    def __init__(self,parent: QObject | None,icon:QIcon,text:str|None,tip: str | None,slot: None):
        self.QAction=QAction()
        self.QAction.setIcon(icon)
        self.QAction.setText(text)
        self.QAction.setParent(parent)
        self.QAction.setToolTip(tip)
        self.QAction.triggered.connect(slot)
    


    