#
#count down timer plugin for Displayotron 3000
#
from dot3k.menu import MenuOption
import os,time, datetime
from datetime import timedelta
class countDown(MenuOption):
  def redraw(self, menu):
    # enter target time and date here
    day=28
    month=2
    year=2015
    hour=16
    minutes=30
    sec=0
    targetTime = datetime.datetime(year, month, day, hour, minutes) # sets up target time
    timeNow =datetime.datetime.now() # the time now!
    if timeNow < targetTime:
        timeNow =datetime.datetime.now()
        remainingTime=(targetTime-timeNow)
        days = remainingTime.days
        secs = remainingTime.seconds
        hrs, secs = divmod(secs, 3600)
        mins, secs = divmod(secs, 60) 
        menu.write_row(0,'%dd %dh %dm %ds' % (days, hrs, mins, secs))
        menu.write_row(1,'to Raspberry Pi')
        menu.write_row(2,'   Party!!!!!!!')
        time.sleep(1)
    else:    
        menu.clear_row(0)
        menu.write_option( 
            row=1,
            text="what time is it? It's Party Time",
            scroll=True
        )
        menu.clear_row(2)
