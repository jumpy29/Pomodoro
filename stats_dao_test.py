from stats_dao import StatsDao
from datetime import datetime
def main():
    dao = StatsDao()
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_month = datetime.now().strftime("%Y-%m")
    date = '2024-04-25'
    month = '2024-04'
    dao.create_new_day_entry2(date)
    dao.update_break_stats2(date, month, 10)
    dao.update_focus_stats2(date, month, 25)

    

    
  



    



if __name__=='__main__':
    main()