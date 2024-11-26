from PyQt6.QtCore import QObject, QTimer, pyqtSignal

class Timer(QObject):
    time_updated = pyqtSignal(str) #signal for updated time in "minutes:secord" format
    timer_finished = pyqtSignal() #signal when the timer finished

    def __init__(self, focus_time = 25):
        """
        takes time in minutes and initialize timer Object
        """
        super().__init__()
        focus_time *= 60 #converting to seconds
        self.focus_time = focus_time
        self.time_left = focus_time
        self.timer_running = False

        #creating timer
        self.timer = QTimer()
        self.timer.setInterval(1000) #timer times out every 1000ms(1s)
        self.timer.timeout.connect(self.update_time) #update_time runs at 1s interval when timer runs

    def format_time(self, time_in_seconds):
        """
        useful to convert time to readable format which is later displayed
        """
        minutes = time_in_seconds//60 
        seconds = time_in_seconds%60
        return f"{minutes:02}:{seconds:02}"
    
    def start_timer(self):
        """
        starting timer
        """
        if not self.timer_running:
            self.timer.start()
            self.timer_running = True

    def update_time(self):
        """
        updates the remaining time every second
        """
        if self.time_left>0:
            self.time_left-=1 
            formatted_time = self.format_time(self.time_left)
            self.time_updated.emit(formatted_time) #emits the updated time
        else:
            self.timer.stop()
            self.timer_running = False
            self.timer_finished.emit() #emits signal when timer finished


    def stop_timer(self):
        """
        stops the countdown timer.
        """
        if self.timer_running:
            self.timer.stop()
            self.timer_running = False
            self.time_updated.emit(self.format_time(self.time_left))

    def reset_timer(self):
        """
        reset the timer to the initial focus time
        """
        self.stop_timer()
        self.time_left = self.focus_time
        formatted_time = self.format_time(self.time_left)
        self.time_updated.emit(formatted_time) #signals the new updated time

    def set_time(self, new_time):
        self.focus_time = new_time*60
        self.reset_timer()

