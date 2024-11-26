import sqlite3
from datetime import datetime

class StatsDao:
    def __init__(self):
        self.db_path = "stats.db"
        self.init_db()

    def init_db(self):
        """Initializing db and create new stats table if doesnt exist"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS daily_stats(
                    date TEXT PRIMARY KEY, 
                    focus_count INTEGER DEFAULT 0,
                    break_count INTEGER DEFAULT 0,
                    focus_minutes INTEGER DEFAULT 0,
                    break_minutes INTEGER DEFAULT 0
                )
            ''')
            connection.commit()

    def get_last_entry(self):
        """
        gets the last entered data, useful for getting last day and updating 
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT date, focus_count, break_count, focus_minutes, break_minutes FROM daily_stats ORDER BY date DESC LIMIT 1')
            return cursor.fetchone()
    
    def create_new_day_entry(self, date):
        """
        Insert a new entry for a specific date.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO daily_stats (date, focus_count, break_count, focus_minutes, break_minutes) VALUES (?, ?, ?, ?, ?)
            ''', (date, 0, 0, 0, 0))
            connection.commit()

    def update_focus_stats(self, date, cur_focus_time):
        """
        Increment the focus count and add focus minutes.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET focus_count = focus_count + 1, 
                    focus_minutes = focus_minutes + ?
                WHERE date = ?
            ''', (cur_focus_time, date))
            connection.commit()

    def update_break_stats(self, date, cur_break_time):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET break_count = break_count+1,
                    break_minutes = break_minutes + ?
                WHERE date = ?
            ''', (cur_break_time, date))
            connection.commit()
    
    def get_day_stats(self, date):
        """gets stats for a particular date"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT date, focus_count, break_count, focus_minutes, break_minutes 
                FROM daily_stats 
                WHERE date = ?
            ''', (date,))
            return cursor.fetchone()
        
    def get_all_stats(self):
        """Get all stats from the daily_stats table"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT date, focus_count, break_count, focus_minutes, break_minutes 
                FROM daily_stats
            ''')
            return cursor.fetchall()
        
    def get_latest_date(self):
        """Get the date of the latest entry"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT date FROM daily_stats
                ORDER BY date DESC
                LIMIT 1
            ''')
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the date from the first column of the result
            return None  # returning null if no entry



