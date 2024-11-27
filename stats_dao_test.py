from stats_dao import StatsDao
from datetime import datetime
def main():
    dao = StatsDao()
    date = '2024-11'
    dao.update_monthly_focus_stats2(date, 170)
    month_total_time = dao.get_focus_on_month(datetime.now().strftime("%Y-%m"))
    print(month_total_time)

if __name__=='__main__':
    main()