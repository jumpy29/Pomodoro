from stats_dao import StatsDao
from datetime import datetime
def main():
    dao = StatsDao()
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_month = datetime.now().strftime("%Y-%m")
    print(dao.get_focus_on_date(current_date))

if __name__=='__main__':
    main()