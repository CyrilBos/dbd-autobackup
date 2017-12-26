import os
import shutil
from datetime import datetime


backup_root_path = "C:/Users/YOURUSERNAME/Google Drive/Backup/Steam/userdata/YOURSTEAMIDPROFILE/381210/"
steam_userdata_path = "D:/Steam/userdata/YOURSTEAMIDPROFILE/"



os.chdir(backup_root_path)

	
#date time formatted as year-month-day-hour-minute-seconds-microseconds
now_str = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss%fms")


new_backup_path = "{}backup-{}".format(backup_root_path, now_str)

#creates the new save directory with name of format backup-unique-index-date
os.mkdir(new_backup_path)

shutil.copytree(steam_userdata_path + "381210/remote", new_backup_path + '/remote/')