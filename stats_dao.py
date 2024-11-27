import sqlite3
from datetime import datetime

class StatsDao:
    def __init__(self):
        self.db_path = "stats.db"
        self.init_db()
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.current_month = datetime.now().strftime("%Y-%m")

    def init_db(self):
        """Initializing db and create new stats table if doesnt exist"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()

            #creating daily stats table
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

            # Creating monthly_stats table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS monthly_stats (
                    month TEXT PRIMARY KEY,  -- Format: YYYY-MM
                    total_focus_count INTEGER DEFAULT 0,
                    total_break_count INTEGER DEFAULT 0,
                    total_focus_minutes INTEGER DEFAULT 0,
                    total_break_minutes INTEGER DEFAULT 0
                );
            ''')

    def get_last_entry(self):
        """
        gets the last entered data from daily table
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT date, focus_count, break_count, focus_minutes, break_minutes FROM daily_stats ORDER BY date DESC LIMIT 1')
            return cursor.fetchone()
    
    def create_new_day_entry(self):
        """
        Insert a new entry for a specific date.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO daily_stats (date, focus_count, break_count, focus_minutes, break_minutes) VALUES (?, ?, ?, ?, ?)
            ''', (self.current_date, 0, 0, 0, 0))
            connection.commit()

    #for debugging :FIXME:
    def create_new_day_entry2(self, date):
        """
        Insert a new entry for a specific date.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO daily_stats (date, focus_count, break_count, focus_minutes, break_minutes) VALUES (?, ?, ?, ?, ?)
            ''', (date, 0, 0, 0, 0))
            connection.commit()

    def create_new_month_entry(self):
        """
        Insert a new entry for the current month into the monthly_stats table.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO monthly_stats (month, total_focus_count, total_break_count, total_focus_minutes, total_break_minutes)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.current_month, 0, 0, 0, 0))  # Initial values are set to 0
            connection.commit()

    #for debugging only remove after completion :FIXME:
    def create_new_month_entry2(self, month):
        """
        Insert a new entry for the current month into the monthly_stats table.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO monthly_stats (month, total_focus_count, total_break_count, total_focus_minutes, total_break_minutes)
                VALUES (?, ?, ?, ?, ?)
            ''', (month, 0, 0, 0, 0))  # Initial values are set to 0
            connection.commit()

    def update_focus_stats(self, cur_focus_time):
        """
        Increment the focus count and add focus minutes.
        """
        self.update_daily_focus_stats(cur_focus_time)
        self.update_monthly_focus_stats(cur_focus_time)

    #for debugging only remove after completion :FIXME:
    def update_focus_stats2(self, date, month, cur_focus_time):
        self.update_daily_focus_stats2(date, cur_focus_time)
        self.update_monthly_focus_stats2(month, cur_focus_time)

    def update_daily_focus_stats(self, cur_focus_time):
        """increment daily stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET focus_count = focus_count + 1, 
                    focus_minutes = focus_minutes + ?
                WHERE date = ?
            ''', (cur_focus_time, self.current_date))
            connection.commit()

    #for debugging only remove after completion :FIXME:
    def update_daily_focus_stats2(self, date, cur_focus_time):
        """increment daily stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET focus_count = focus_count + 1, 
                    focus_minutes = focus_minutes + ?
                WHERE date = ?
            ''', (cur_focus_time, date))
            connection.commit()

    def update_monthly_focus_stats(self, cur_focus_time):
        """increment monthly stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE monthly_stats
                SET total_focus_count = total_focus_count + 1, 
                    total_focus_minutes = total_focus_minutes + ?
                WHERE month = ?
            ''', (cur_focus_time, self.current_month))
            connection.commit()

    #for debugging only remove after completion :FIXME:
    def update_monthly_focus_stats2(self,month, cur_focus_time):
        """increment monthly stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE monthly_stats
                SET total_focus_count = total_focus_count + 1, 
                    total_focus_minutes = total_focus_minutes + ?
                WHERE month = ?
            ''', (cur_focus_time, month))
            connection.commit()


    def update_break_stats(self, cur_break_time):
        self.update_daily_break_stats(cur_break_time)
        self.update_monthly_break_stats(cur_break_time)

    #for debugging only remove after completion :FIXME:
    def update_break_stats2(self, date, month, cur_break_time):
        self.update_daily_break_stats2(date, cur_break_time)
        self.update_monthly_break_stats2(month, cur_break_time)
    

    def update_daily_break_stats(self, cur_break_time):
        """increment daily break stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET break_count = break_count+1,
                    break_minutes = break_minutes + ?
                WHERE date = ?
            ''', (cur_break_time, self.current_date))
            connection.commit()

    #for debugging only remove after completion :FIXME:
    def update_daily_break_stats2(self,date, cur_break_time):
        """increment daily break stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE daily_stats
                SET break_count = break_count+1,
                    break_minutes = break_minutes + ?
                WHERE date = ?
            ''', (cur_break_time, date))
            connection.commit()

    def update_monthly_break_stats(self, cur_break_time):
        """increment monthly break stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE monthly_stats
                SET total_break_count = total_break_count+1,
                    total_break_minutes = total_break_minutes + ?
                WHERE month = ?
            ''', (cur_break_time, self.current_month))
            connection.commit()
    
    #for debugging only remove after completion :FIXME:
    def update_monthly_break_stats2(self, month, cur_break_time):
        """increment monthly break stats"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                UPDATE monthly_stats
                SET total_break_count = total_break_count+1,
                    total_break_minutes = total_break_minutes + ?
                WHERE month = ?
            ''', (cur_break_time, month))
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
        
    def get_all_daily_stats(self):
        """Get all stats from the daily_stats table"""
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT date, focus_count, break_count, focus_minutes, break_minutes 
                FROM daily_stats
            ''')
            return cursor.fetchall()
        
    def get_last_date(self):
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

    def does_date_entry_exists(self, date):
            """
            Checks if an entry exists for a specific date.
            """
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT 1 FROM daily_stats WHERE date = ? LIMIT 1
                ''', (date,))
                result = cursor.fetchone()
                return result is not None
            
    def does_month_entry_exists(self, month):
            """
            Checks if an entry exists for a specific date.
            """
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT 1 FROM monthly_stats WHERE month = ? LIMIT 1
                ''', (month,))
                result = cursor.fetchone()
                return result is not None



