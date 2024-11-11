import psutil
import platform
from time import time
from datetime import datetime, timedelta

now = time()
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

def system_info():
    uname = platform.uname()
    node = platform.node()
    machine = platform.machine()
    processor = platform.processor()

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    memory = psutil.virtual_memory()
    boot_secs = psutil.boot_time()
    boot_date = datetime.fromtimestamp(boot_secs).strftime("%Y-%m-%d %H:%M:%S")
    info = platform.freedesktop_os_release()

    uptime_seconds = now - boot_secs
    uptime_duration = timedelta(seconds=uptime_seconds)

    days, remainder = divmod(uptime_duration.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    time_components = [
        f"{int(days)} days" if days else "",
        f"{int(hours)} hours" if hours else "",
        f"{int(minutes)} minutes" if minutes else "",
        f"{int(seconds)} seconds" if seconds else ""
    ]
    formatted_uptime = ', '.join(filter(bool, time_components))
    system_info = (
        f"{BOLD}System:{END} {uname.system} {uname.release} ({uname.version})\n"
        f"{BOLD}Processor:{END} {processor} {BOLD}Machine:{END} {machine} {BOLD}Node:{END} {node}\n"
        f"{BOLD}Machine:{END} {uname.machine} "
        f"{BOLD}CPU:{END} {cpu_count} cores {BOLD}Usage:{END} {cpu_usage}% "
        f"{BOLD}Memory:{END} {memory.percent}% used of {memory.total // (1024 ** 3)} GB\n"
        f"{BOLD}Boot Date:{END} {boot_date} ({boot_secs})\n"
        f"{BOLD}Uptime:{END} {formatted_uptime}\n"
        f"{BOLD}Info:{END} {info}\n"
    )
    
    return system_info

print(f'System Info: {system_info()}')
