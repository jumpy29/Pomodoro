from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QMainWindow
import sys
from timer import Timer  # Your Timer class from earlier
from pygame import mixer
from settings import SettingsWindow
from stats_dao import StatsDao
from datetime import datetime

# File data index
FOCUS_TIME = 0 
BREAK_TIME = 1

FOCUS_MODE = True
BREAK_MODE = False

# Widget indexes
MAIN_PAGE = 0
SETTINGS_PAGE = 1

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        mixer.init()

        self.bell_sound_filename = "timer_end.mp3"
        self.toggle_sound_filename = "toggle_sound.mp3"
        self.settings_icon = "settings.png"
        self.time_settings_filename = "time_settings.txt"
        
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(0, 0, 350, 250)

        self.load_custom_times()  # Loading custom times if they exist

        self.timer = Timer(self.focus_time)
        self.mode = FOCUS_MODE  

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Set up the Timer page (Pomodoro Timer)
        self.timer_page = self.create_timer_page()
        
        # Set up the Settings page
        self.settings_page = self.create_settings_page()

        # Add pages to the StackedWidget
        self.central_widget.addWidget(self.timer_page)        # Index 0
        self.central_widget.addWidget(self.settings_page)     # Index 1
        
        # Connect signals to functions
        self.timer.time_updated.connect(self.update_time_label)
        self.timer.timer_finished.connect(self.on_timer_finished)

    def create_timer_page(self):
        timer_page = QWidget()
        layout = QVBoxLayout(timer_page)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        timer_page.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #fae1dd, stop:1 #f8edeb);
            border-radius: 5px;
            color: #495057;
        """)

        # Mode switch (Focus/Break)
        mode_switch_layout = QHBoxLayout()
        mode_switch_layout.setSpacing(0)
        mode_switch_layout.setContentsMargins(0, 0, 0, 0)

        self.focus_button = QPushButton("Focus", self)
        self.focus_button.setFixedWidth(100)
        self.focus_button.clicked.connect(self.focus_button_clicked)
        self.focus_button.setStyleSheet("""
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)
        mode_switch_layout.addWidget(self.focus_button)

        self.break_button = QPushButton("Break", self)
        self.break_button.setFixedWidth(100)
        self.break_button.clicked.connect(self.break_button_clicked)
        mode_switch_layout.addWidget(self.break_button)

        layout.addLayout(mode_switch_layout)    

        # Time Label
        self.time_label = QLabel(f"{self.timer.format_time(self.timer.focus_time)}", self)
        layout.addWidget(self.time_label)

        # Font for time
        self.time_label.setFont(QFont("Courier New", 48, QFont.Weight.Bold))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Aligning to center
        
        # Start/Stop Button
        self.start_stop_button = QPushButton("Start", self)
        self.start_stop_button.clicked.connect(self.start_stop_clicked)
        layout.addWidget(self.start_stop_button, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.start_stop_button.setFixedSize(100, 40)
        self.start_stop_button.setStyleSheet("""
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)

        # Settings Button
        self.settings_button = QPushButton()
        self.settings_button.setIcon(QIcon(self.settings_icon))
        self.settings_button.clicked.connect(self.settings_clicked)
        layout.addWidget(self.settings_button)

        return timer_page

    def create_settings_page(self):
        settings_window = SettingsWindow(self, self.focus_time, self.break_time)
        settings_window.time_changed_signal.connect(self.update_timer_after_save)
        return settings_window

    def start_stop_clicked(self):
        if self.timer.timer_running:
            self.stop_timer()
        else: 
            self.start_timer()
        self.play_toggle_sound()

    def focus_button_clicked(self):
        self.mode = FOCUS_MODE
        self.timer.set_time(self.focus_time)
        self.play_toggle_sound()
        self.update_button_after_stopped()  # Updating text and size of button
        self.break_button.setStyleSheet("""
            QPushButton{
                background: #fae1dd;
                color: #495057            
            }
        """)
        self.focus_button.setStyleSheet("""
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)

    def break_button_clicked(self):
        self.mode = BREAK_MODE
        self.timer.set_time(self.break_time)
        self.play_toggle_sound()
        self.update_button_after_stopped()  # Updating text and size of button
        self.focus_button.setStyleSheet("""
            QPushButton{
                background: #fae1dd;
                color: #495057            
            }
        """)
        self.break_button.setStyleSheet("""
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)
        
    def settings_clicked(self):
        self.central_widget.setCurrentIndex(SETTINGS_PAGE)

    def update_timer_after_save(self):
        self.load_custom_times()
        self.update_time_label(self.timer.format_time(self.focus_time))
        if self.mode == FOCUS_MODE:
            self.focus_button_clicked()
        else:
            self.break_button_clicked()
        self.central_widget.setCurrentIndex(MAIN_PAGE)
    
    def update_time_label(self, time):
        self.time_label.setText(f"{time}")
    
    def start_timer(self):
        mixer.music.stop()
        self.timer.start_timer()
        self.update_button_after_started()  # Updating button
    
    def stop_timer(self):
        self.timer.stop_timer()
        self.update_button_after_stopped()  # Updating button

    def reset_timer(self):
        self.timer.reset_timer()

    def update_button_after_stopped(self):
        self.start_stop_button.setText("Start")
        self.start_stop_button.setFixedSize(100, 40)

    def update_button_after_started(self):
        self.start_stop_button.setText("Stop")
        self.start_stop_button.setFixedSize(95, 35)

    def on_timer_finished(self):
        self.stats_dao = StatsDao()
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_month = datetime.now().strftime("%Y-%m")
        if not self.stats_dao.does_date_entry_exists(current_date):  # If day entry does not exist, make a new entry
            self.stats_dao.current_date = current_date
            self.stats_dao.create_new_day_entry()
        if not self.stats_dao.does_month_entry_exists(current_month):  # Creating a new month entry when a new month starts
            self.stats_dao.current_month = current_month
            self.stats_dao.create_new_month_entry()
        self.stop_timer()  
        self.reset_timer() 
        formatted_time = self.timer.format_time(self.timer.time_left)
        self.time_label.setText(f"{formatted_time}")  # Updating time
        if self.mode == FOCUS_MODE:
            self.stats_dao.update_focus_stats(self.focus_time)  # Update database
            self.break_button_clicked()
        else:
            self.stats_dao.update_break_stats(self.break_time)  # Update database
            self.focus_button_clicked()
        self.play_bell_sound()

    def play_bell_sound(self):
        mixer.music.load(self.bell_sound_filename)
        mixer.music.play()
    
    def play_toggle_sound(self):
        mixer.music.load(self.toggle_sound_filename)
        mixer.music.play()

    def load_custom_times(self):
        try:
            with open(self.time_settings_filename, "r") as f:
                custom_times = f.read().strip()
                custom_times = custom_times.split(",")
                self.focus_time = int(custom_times[FOCUS_TIME])
                self.break_time = int(custom_times[BREAK_TIME])
        except:
            self.focus_time = 25
            self.break_time = 5

def main():
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
