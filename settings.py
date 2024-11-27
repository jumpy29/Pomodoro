from PyQt6.QtWidgets import (
    QDialog, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from colors import PRIMARY, SECONDARY


class SettingsWindow(QDialog):
    #theme changed signals
    blue_theme_signal = pyqtSignal()
    pink_theme_signal = pyqtSignal()
    purple_theme_signal = pyqtSignal()
    red_theme_signal = pyqtSignal()
    wood_theme_signal = pyqtSignal()
    time_changed_signal = pyqtSignal(int, int) #signal when new time is saved, useful to display on main window
    def __init__(self, parent=None, focus_time=25, break_time=5):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        self.setGeometry(0, 0, 350, 250)

        #TODO:
        # self.setStyleSheet(f"""
        #     background: {PRIMARY};
        #     border-radius: 5px;
        #     color: {SECONDARY};
        # """)

        # Main layout
        self.main_layout = QVBoxLayout(self)

        # Pomodoro Section
        self.pomodoro_layout = QVBoxLayout()
        self.pomodoro_label = QLabel("Focus time")
        self.pomodoro_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pomodoro_input = QSpinBox()
        self.pomodoro_input.setRange(1, 60)
        self.pomodoro_input.setValue(focus_time)  
        self.pomodoro_layout.addWidget(self.pomodoro_label)
        self.pomodoro_layout.addWidget(self.pomodoro_input)
        self.pomodoro_layout.setSpacing(0)  # Reduce spacing between label and spin box

        # Short Break Section
        self.break_layout = QVBoxLayout()
        self.break_label = QLabel("Short Break")
        self.break_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.break_input = QSpinBox()
        self.break_input.setRange(1, 30)
        self.break_input.setValue(break_time)
        self.break_layout.addWidget(self.break_label)
        self.break_layout.addWidget(self.break_input)
        self.break_layout.setSpacing(0)  # Reduce spacing between label and spin box

        # Combine Pomodoro and Short Break layouts
        self.time_settings_layout = QHBoxLayout()
        self.time_settings_layout.addLayout(self.pomodoro_layout)
        self.time_settings_layout.addLayout(self.break_layout)

        # Add the time settings layout to the main layout
        self.main_layout.addLayout(self.time_settings_layout)

        #THEMES
        self.themes = QHBoxLayout()

        self.blue_theme = QPushButton()
        self.pink_theme = QPushButton()
        self.purple_theme = QPushButton()
        self.red_theme = QPushButton()
        self.wood_theme = QPushButton()

        self.themes.addWidget(self.blue_theme)
        self.themes.addWidget(self.pink_theme)
        self.themes.addWidget(self.purple_theme)
        self.themes.addWidget(self.red_theme)
        self.themes.addWidget(self.wood_theme)

        self.themes.setSpacing(0)
        self.themes.setContentsMargins(0, 0, 0, 0)

        self.blue_theme.setStyleSheet("background-color: #189AB4; border-radius: 5px;")
        self.pink_theme.setStyleSheet("background-color: #F2C5E0; border-radius: 5px;")
        self.purple_theme.setStyleSheet("background-color: #D4BBDD; border-radius: 5px;")
        self.red_theme.setStyleSheet("background-color: #FFA384; border-radius: 5px;")
        self.wood_theme.setStyleSheet("background-color: #875F59; border-radius: 5px;")

        self.blue_theme.clicked.connect(self.blue_theme_clicked)
        self.pink_theme.clicked.connect(self.pink_theme_clicked)
        self.purple_theme.clicked.connect(self.purple_theme_clicked)
        self.red_theme.clicked.connect(self.red_theme_clicked)
        self.wood_theme.clicked.connect(self.wood_theme_clicked)


        box_size = 25
        self.blue_theme.setFixedSize(box_size, box_size)
        self.pink_theme.setFixedSize(box_size, box_size)
        self.purple_theme.setFixedSize(box_size, box_size)
        self.red_theme.setFixedSize(box_size, box_size)
        self.wood_theme.setFixedSize(box_size, box_size)

        self.main_layout.addLayout(self.themes)

        # Save Button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_settings)
        self.main_layout.addWidget(self.save_button)

        # Adjust layout spacing
        self.main_layout.setSpacing(15)  # Space between sections
        self.main_layout.setAlignment(self.save_button, Qt.AlignmentFlag.AlignCenter)

    def save_settings(self):
        focus_time = int(self.pomodoro_input.text())
        break_time = int(self.break_input.text())
        with open("time_settings.txt", "w") as f:
            f.write(f"{focus_time},{break_time}")
        self.time_changed_signal.emit(focus_time, break_time)
        self.close()

    def blue_theme_clicked(self):
        self.blue_theme_signal.emit()
    def pink_theme_clicked(self):
        self.pink_theme_signal.emit()
    def purple_theme_clicked(self):
        self.purple_theme_signal.emit()
    def red_theme_clicked(self):
        self.red_theme_signal.emit()
    def wood_theme_clicked(self):
        self.wood_theme_signal.emit()


