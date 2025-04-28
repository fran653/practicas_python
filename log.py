#!/bin/env/ python3





import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])





#chmod +x check_cron.py 
#./check_cron.py syslog 