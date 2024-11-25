from PyQt6.QtCore import QCoreApplication, Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys
from timer import Timer  # Your Timer class from earlier
from pygame import mixer

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        mixer.init()

        self.sound_filename = "timer_end.mp3"
        
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(0, 0, 350, 250)
        
        # Create a Timer instance with 10 seconds for testing
        self.timer = Timer(1)
        
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
        # Time Label
        self.time_label = QLabel(f"{self.timer.format_time(self.timer.focus_time)}", self)
        self.layout.addWidget(self.time_label)

        # Font for time
        self.time_label.setFont(QFont("Courier New", 48, QFont.Weight.Bold))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Aligning to center
        
        # Start Button
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.start_button.setFixedSize(100, 40)
        self.start_button.setStyleSheet(
            """
            QPushButton{
            background: #495057;
            color: #fae1dd
            }
        """)
        
        # Stop Button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button)
        
        # Set layout
        self.setLayout(self.layout)
    
    def update_time_label(self, time):
        # Update the label text with the formatted time
        self.time_label.setText(f"{time}")
    
    def start_timer(self):
        mixer.music.stop()
        self.timer.start_timer()
    
    def stop_timer(self):
        self.timer.stop_timer()

    def on_timer_finished(self):
        self.timer.stop_timer()  # Stop the timer when finished
        self.timer.time_left = self.timer.focus_time  # Reset to initial time
        formatted_time = self.timer.format_time(self.timer.time_left)
        self.time_label.setText(f"{formatted_time}")
        self.play_sound()

    def play_sound(self):
        mixer.music.load(self.sound_filename)
        mixer.music.play()


def main():
    app = QApplication(sys.argv)  # PyQt's event loop for signals/slots
    window = TimerApp()
    window.show()  # Display the window
    sys.exit(app.exec())

if __name__ == "__main__":
    main()