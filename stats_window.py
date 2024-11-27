from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt  # For alignment flags
from colors import PRIMARY, SECONDARY, STAT_COLOR

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
        self.today_focus_label = QLabel("0h0m")
        #dark pink
        #F79489
        self.today_focus_label.setStyleSheet(f'''
            color: {STAT_COLOR};
            font-family: 'Courier New';
            font-size: 26px;
            font-weight: bold;
        ''')
        self.today_focus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.today_label = QLabel("TODAY")
        self.today_label.setStyleSheet('''
            padding-bottom: 15px;
            margin-bottom: 15px;
        ''')

        self.today_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to today stats layout
        self.today_stats_layout.addWidget(self.today_focus_label)
        self.today_stats_layout.addWidget(self.today_label)

        # Widgets for "Monthly Best"
        self.monthly_best_focus_label = QLabel("5h10m")
        self.monthly_best_focus_label.setStyleSheet(f'''
            color: {STAT_COLOR};
            font-family: 'Courier New';
            font-size: 26px;
            font-weight: bold;
        ''')
        self.monthly_best_focus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.monthly_best_label = QLabel("MONTHLY BEST")


        self.monthly_best_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to monthly best layout
        self.monthly_best_layout.addWidget(self.monthly_best_focus_label)
        self.monthly_best_layout.addWidget(self.monthly_best_label)


        # Add sub-layouts to the daily stats layout
        self.daily_stats_layout.addLayout(self.today_stats_layout)
        self.daily_stats_layout.addLayout(self.monthly_best_layout)

        # Center-align the entire daily stats layout
        self.daily_stats_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_monthly_stats_layout(self):
        self.monthly_total_layout = QVBoxLayout()

        # Widgets for "Monthly Total"
        self.total_monthly_focus = QLabel("10h10m")
        self.total_monthly_focus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.total_monthly_label = QLabel("MONTH TOTAL")
        self.total_monthly_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.total_monthly_focus.setStyleSheet(f'''
            color: {STAT_COLOR};
            font-size: 26px;
            font-weight: bold;
        ''')


        # Add widgets to the monthly total layout
        self.monthly_total_layout.addWidget(self.total_monthly_focus)        
        self.monthly_total_layout.addWidget(self.total_monthly_label)        


        # Add the monthly total layout to the main monthly stats layout
        self.monthly_stats_layout.addLayout(self.monthly_total_layout)

        # Center-align the entire monthly stats layout
        self.monthly_stats_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

