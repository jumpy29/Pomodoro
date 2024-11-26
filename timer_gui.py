from PyQt6.QtCore import QCoreApplication, Qt, QTimer
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
import sys
from timer import Timer  # Your Timer class from earlier
from pygame import mixer
from settings import SettingsWindow

FOCUS_TIME = 0
BREAK_TIME = 1

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        mixer.init()

        self.bell_sound_filename = "timer_end.mp3"
        self.toggle_sound_filename = "toggle_sound.mp3"
        self.settings_icon = "settings.png"
        self.time_settings_filename = "time_settings.txt"
        
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(0, 0, 350, 250)

        self.load_custom_times() #loading custom times if they exist

        self.timer = Timer(self.focus_time)
        
        # Set up UI components
        self.init_ui()
        
        # Connect signals to functions
        self.timer.time_updated.connect(self.update_time_label)
        self.timer.timer_finished.connect(self.on_timer_finished)

    def init_ui(self):
        # Layout
        self.layout = QVBoxLayout()
        self.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #fae1dd, stop:1 #f8edeb);
            border-radius: 5px;
            color: #495057;
        """)

        #mode switch (focus/break)
        self.mode_switch_layout = QHBoxLayout()
        self.mode_switch_layout.setSpacing(0)  #bcs i want no space bw buttons
        self.mode_switch_layout.setContentsMargins(0, 0, 0, 0)  #same reason as above

        self.focus_button = QPushButton("Focus", self)
        self.focus_button.setFixedWidth(100)
        self.focus_button.clicked.connect(self.focus_button_clicked)
        self.focus_button.setStyleSheet(
            """
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)
        self.mode_switch_layout.addWidget(self.focus_button)

        self.break_button = QPushButton("Break", self)
        self.break_button.setFixedWidth(100)
        self.break_button.clicked.connect(self.break_button_clicked)
        self.break_button.setStyleSheet(
            """
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)
        self.mode_switch_layout.addWidget(self.break_button)

        self.layout.addLayout(self.mode_switch_layout)    

        # Time Label
        self.time_label = QLabel(f"{self.timer.format_time(self.timer.focus_time)}", self)
        self.layout.addWidget(self.time_label)

        # Font for time
        self.time_label.setFont(QFont("Courier New", 48, QFont.Weight.Bold))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Aligning to center
        
        # Start and stop Button
        self.start_stop_button = QPushButton("Start", self)
        self.start_stop_button.clicked.connect(self.start_stop_clicked)
        self.layout.addWidget(self.start_stop_button, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.start_stop_button.setFixedSize(100, 40)
        self.start_stop_button.setStyleSheet(
            """
            QPushButton{
            background: #495057;
            color: #fae1dd;
            }
        """)

        #settings button
        self.settings_button = QPushButton()
        self.settings_button.setIcon(QIcon(self.settings_icon))
        self.settings_button.clicked.connect(self.settings_clicked)
        self.layout.addWidget(self.settings_button)
        
        # Set layout
        self.setLayout(self.layout)

    def start_stop_clicked(self):
        if self.timer.timer_running:
            self.stop_timer()
        else: 
            self.start_timer()
        self.play_toggle_sound()

    def focus_button_clicked(self):
        self.timer.set_time(self.focus_time)
        self.play_toggle_sound()
        self.update_button_after_stopped() #updating text and size of button

    def break_button_clicked(self):
        self.timer.set_time(self.break_time)
        self.play_toggle_sound()
        self.update_button_after_stopped() #updating text and size of button
    
    def settings_clicked(self):
        self.settings_window = SettingsWindow(self, self.focus_time, self.break_time)
        self.settings_window.time_changed_signal.connect(self.update_timer_after_save)
        self.settings_window.show()

    def update_timer_after_save(self):
        self.load_custom_times()
        self.update_time_label(self.timer.format_time(self.focus_time))
        self.timer.set_time(self.focus_time)
    
    def update_time_label(self, time):
        # Update the label text with the formatted time
        self.time_label.setText(f"{time}")
    
    def start_timer(self):
        mixer.music.stop()
        self.timer.start_timer()
        self.update_button_after_started() #updateing button
    
    def stop_timer(self):
        self.timer.stop_timer()
        self.update_button_after_stopped() #updating button

    def reset_timer(self):
        self.timer.reset_timer()

    def update_button_after_stopped(self):
        #updates button after timer stops
        self.start_stop_button.setText("Start")
        self.start_stop_button.setFixedSize(100, 40)

    def update_button_after_started(self):
        #updates button after timer starts
        self.start_stop_button.setText("Stop")
        self.start_stop_button.setFixedSize(95, 35)

    def on_timer_finished(self):
        self.stop_timer()  
        self.reset_timer() 
        formatted_time = self.timer.format_time(self.timer.time_left)
        self.time_label.setText(f"{formatted_time}") #updating time
        self.play_bell_sound()

    def play_bell_sound(self):
        mixer.music.load(self.bell_sound_filename)
        mixer.music.play()
    
    def play_toggle_sound(self):
        mixer.music.load(self.toggle_sound_filename)
        mixer.music.play()

    def load_custom_times(self):
        try:
            #reading custom times from file, if exists
            with open(self.time_settings_filename, "r") as f:
                #focustime and breaktime stored in focus:break format
                custom_times = f.read().strip()
                custom_times = custom_times.split(",")
                self.focus_time = int(custom_times[FOCUS_TIME])
                self.break_time = int(custom_times[BREAK_TIME])
        except:
            #setting defaults
            self.focus_time = 25
            self.break_time = 5

def main():
    app = QApplication(sys.argv)  # PyQt's event loop for signals/slots
    window = TimerApp()
    window.show()  # Display the window
    sys.exit(app.exec())

if __name__ == "__main__":
    main()