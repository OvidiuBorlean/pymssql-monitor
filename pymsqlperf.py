import mysql.connector
from mysql.connector import errorcode
import os
import time
#import datetime
from datetime import datetime
#from datetime import datetime
from timeit import default_timer as timer

def checkMySql():
  try:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    conn = mysql.connector.connect(**config)
    print(dt_string + " " + "Connection established to MySQL Server")
    conn.close()
    file1= open("mysqltest.log","a")
    content = dt_string + " " + "Connection established to MySQL Server"
    file1.write(content)
    file1.write("\n")
    file1.close()
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
     print("Something is wrong with the user name or password")
     file1= open("mysqltest.log","a")
     content = dt_string + " " + "Something is wrong with the user name or password"
     file1.write(content)
     file1.write("\n")
     file1.close()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
      file1= open("mysqltest.log","a")
      content = dt_string + " " + "Database does not exist"
      file1.write(content)
      file1.write("\n")
      file1.close()
    else:
      print(err)
      file1= open("mysqltest.log","a")
      content = dt_string + " " + str(err)
      file1.write(content)
      file1.write("\n")
      file1.close()

if __name__ == '__main__':
  myHostname = os.getenv('SQLSERVER')
  mySQLUser = os.getenv("SQLUSER")
  myPassword = os.environ.get('SQLPASS')
  myDB = os.environ.get('SQLDB')
  interval = os.environ.get('TIMEINTERVAL')
  print("test")
  config = {
  'host':myHostname,
  'user':mySQLUser,
  'password':myPassword,
  'database':myDB
  }
  print("Starting MySQL Connectivity Check:...")
  while True:
    start = timer()
    checkMySql()
    end = timer()
    print("Latency to RDS DB:", end - start)
    time.sleep(10)
