import pymssql  
import os
import time
import datetime
#from datetime import datetime
import prometheus_client as prom


Threshold=0.12
Count=0
alertValue=5
def checkAzureSql(server, user, password, database):
  try:
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    conn = pymssql.connect(server=server, user=user, password=password, database=database)
    cursor = conn.cursor()
    #print("Successfull Connected to Azure SQL")
    conn.close()
    file1= open("azsqltest.log","a")
    content = dt_string + " " + "Successfull Connected to Azure SQL"
    file1.write(content)
    file1.write("\n")
    file1.close()
  except:
    print(dt_string + " " + "A MSSQLDriverException has been caught.")
    file1= open("azsqltest.log","a")
    content = dt_string + " " + "A MSSQLDriverException has been caught."
    file1.write(content)
    file1.write("\n")
    file1.close()
if __name__ == '__main__':
  counter = prom.Counter('python_my_counter', 'This is my counter')
  gauge = prom.Gauge('python_my_gauge', 'This is my gauge')
  print("Starting AzureSQL Connectivity Check:...")
  #myHostname = os.getenv('SQLSERVER')
  #myPGUser = os.getenv("SQLUSER")
  #myPassword = os.environ.get('SQLPASS')
  #myDB = os.environ.get('SQLDB')
  #interval = os.environ.get('TIMEINTERVAL')
  myHostname = ""
  myPGUser = ""
  myPassword = ""
  myDB = ""
  interval = 5
  prom.start_http_server(8080)
  while True:
    now = datetime.datetime.now()
    time_formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    t = time.process_time()
    checkAzureSql(myHostname, myPGUser, myPassword, myDB)
    elapsed_time = time.process_time() - t
    t_value = float(elapsed_time)
    gauge.set(t_value)
    if checkAzureSql:
      print("Ok", time_formatted, "Connection Time:", t, "sec")
      #print(t_value)
      if t_value > Threshold:
        Count = Count + 1
        print(Count)
      else:
        Count = 0
        #print("---> Alert count: " ,Alert, time_formatted, "Connection Time:", t, "sec", "Count: ", Count)
      if Count == 5:
          print("Bang")
          #Alert = 0
    time.sleep(int(interval))
    
