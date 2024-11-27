from stats_dao import StatsDao
from datetime import datetime
def main():
    dao = StatsDao()
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_month = datetime.now().strftime("%Y-%m")
    dao.create_new_day_entry(current_date)
    dao.create_new_month_entry()
    
  



    



if __name__=='__main__':
    main()