from PyQt5.QtWidgets import QWidget, QGridLayout


class SearchFilterWindow(QWidget):
    def __init__(self, parent=None):
        super(SearchFilterWindow, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.setStyleSheet("background-color: red;")

    def init_ui(self):
        grid = QGridLayout()

        btn = None

        grid.addWidget(btn, 0, 0, 1, 1)

        self.setLayout(grid)
