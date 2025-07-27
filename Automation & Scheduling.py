# 21. Automate Excel report
import openpyxl
wb = openpyxl.load_workbook('report.xlsx')
sheet = wb.active
sheet['A1'] = 'Updated'
wb.save('report.xlsx')

# 22. Schedule task
import schedule
import time
schedule.every().day.at("09:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

# 23. Rename files
import os
for f in os.listdir():
    os.rename(f, f.lower())

# 24. Email automation
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg.set_content("Hello!")
msg['Subject'] = "Report"
msg['To'] = 'user@company.com'
msg['From'] = 'sender@company.com'
s = smtplib.SMTP('smtp.company.com')
s.send_message(msg)
s.quit()

# 25. Move files
import shutil
shutil.move('report.txt', 'archive/')

# 26. ZIP files
shutil.make_archive('archive', 'zip', 'folder/')

# 27. Log automation
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# 28. Date range generator
from datetime import datetime, timedelta
dates = [datetime.today() - timedelta(days=i) for i in range(30)]

# 29. Task timer
import time
start = time.time()
# do something
print("Elapsed:", time.time() - start)

# 30. Parallel tasks
from multiprocessing import Pool
def square(n): return n * n
print(Pool().map(square, [1, 2, 3, 4]))
