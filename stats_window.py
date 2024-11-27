from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt  # For alignment flags

class StatsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stats Dashboard")

        # Main layout contains two sections: Daily stats on the left, Monthly stats on the right
        self.layout = QHBoxLayout()

        # Daily stats section
        self.daily_stats_layout = QVBoxLayout()
        self.setup_daily_stats_layout()

        # Monthly stats section
        self.monthly_stats_layout = QVBoxLayout()
        self.setup_monthly_stats_layout()
    
        # Adding layouts to the main layout
        self.layout.addLayout(self.daily_stats_layout)
        self.layout.addLayout(self.monthly_stats_layout)

        # Center-align the main layout
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

    def setup_daily_stats_layout(self):
        self.today_stats_layout = QVBoxLayout()
        self.monthly_best_layout = QVBoxLayout()

        # Widgets for "Today Stats"
        self.today_focus_label = QLabel("0h0m\nToday Focus")
        self.today_focus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to today stats layout
        self.today_stats_layout.addWidget(self.today_focus_label)

        # Widgets for "Monthly Best"
        self.monthly_best_focus_label = QLabel("5h10m\nMost Focus")
        self.monthly_best_focus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to monthly best layout
        self.monthly_best_layout.addWidget(self.monthly_best_focus_label)


        # Add sub-layouts to the daily stats layout
        self.daily_stats_layout.addLayout(self.today_stats_layout)
        self.daily_stats_layout.addLayout(self.monthly_best_layout)

        # Center-align the entire daily stats layout
        self.daily_stats_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_monthly_stats_layout(self):
        self.monthly_total_layout = QVBoxLayout()

        # Widgets for "Monthly Total"
        self.total_monthly_focus = QLabel("10h10m\nMonth Total")

        self.total_monthly_focus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to the monthly total layout
        self.monthly_total_layout.addWidget(self.total_monthly_focus)

        # Add the monthly total layout to the main monthly stats layout
        self.monthly_stats_layout.addLayout(self.monthly_total_layout)

        # Center-align the entire monthly stats layout
        self.monthly_stats_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

