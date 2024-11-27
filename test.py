import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Page Example")
        self.setGeometry(100, 100, 800, 600)

        # Main container: QStackedWidget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Pages
        self.main_page = self.create_main_page()
        self.second_page = self.create_second_page()

        # Add pages to QStackedWidget
        self.central_widget.addWidget(self.main_page)  # Index 0
        self.central_widget.addWidget(self.second_page)  # Index 1

    def create_main_page(self):
        """Create the main page with a button to open the second page."""
        page = QWidget()
        layout = QVBoxLayout()

        title_label = QLabel("Welcome to the Main Page!")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Button to go to the second page
        open_button = QPushButton("Go to Second Page")
        open_button.setFont(QFont("Arial", 14))
        open_button.clicked.connect(self.show_second_page)

        layout.addWidget(title_label)
        layout.addWidget(open_button)
        page.setLayout(layout)
        return page

    def create_second_page(self):
        """Create the second page with a button to return to the main page."""
        page = QWidget()
        layout = QVBoxLayout()

        title_label = QLabel("Welcome to the Second Page!")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Button to go back to the main page
        close_button = QPushButton("Go Back to Main Page")
        close_button.setFont(QFont("Arial", 14))
        close_button.clicked.connect(self.show_main_page)

        layout.addWidget(title_label)
        layout.addWidget(close_button)
        page.setLayout(layout)
        return page

    def show_second_page(self):
        """Switch to the second page."""
        self.central_widget.setCurrentIndex(1)  # Show page at index 1

    def show_main_page(self):
        """Switch back to the main page."""
        self.central_widget.setCurrentIndex(0)  # Show page at index 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
