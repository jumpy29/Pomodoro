from PyQt6.QtCore import QCoreApplication, Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
import sys
from timer import Timer  # Your Timer class from earlier

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 300, 200)
        
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
        
        # Time Label
        self.time_label = QLabel(f"{self.timer.format_time(self.timer.focus_time)}", self)
        self.layout.addWidget(self.time_label)

        #font for time
        self.time_label.setFont(QFont("Courier New", 48, QFont.Weight.Bold))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter) #aligning to center
        
        # Start Button
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)
        
        # Stop Button
        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.layout.addWidget(self.stop_button)
        
        # Reset Button
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_timer)
        self.layout.addWidget(self.reset_button)
        
        # Set layout
        self.setLayout(self.layout)
    
    def update_time_label(self, time):
        # Update the label text with the formatted time
        self.time_label.setText(f"{time}")
    
    def start_timer(self):
        self.timer.start_timer()
    
    def stop_timer(self):
        self.timer.stop_timer()

    def reset_timer(self):
        self.timer.stop_timer()
        self.timer.time_left = self.timer.focus_time  # Reset to initial time
        formatted_time = self.timer.format_time(self.timer.time_left)
        self.time_label.setText(f"{formatted_time}") 
    
    def on_timer_finished(self):
        self.time_label.setText("00:00")

def main():
    app = QApplication(sys.argv)  # PyQt's event loop for signals/slots
    window = TimerApp()
    window.show()  # Display the window
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
