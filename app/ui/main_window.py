from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.resize(800, 600)

        central_widget = QWidget()
        layout = QVBoxLayout()

        title = QLabel("Task Manager")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        layout.addWidget(title)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

