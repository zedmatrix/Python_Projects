import psutil
from time import time
from datetime import datetime, timedelta

now = time()
boot_secs = psutil.boot_time()

current_date = datetime.fromtimestamp(now).strftime("%Y-%m-%d %H:%M:%S")
boot_date = datetime.fromtimestamp(boot_secs).strftime("%Y-%m-%d %H:%M:%S")
print(f'Now: {now} Boot_Secs: {boot_secs}')
print(f'Curent Date: {current_date} Boot Date: {boot_date}')

uptime_seconds = now - boot_secs
uptime_duration = timedelta(seconds=uptime_seconds)

days, remainder = divmod(uptime_duration.total_seconds(), 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

print(f'Uptime: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds')
