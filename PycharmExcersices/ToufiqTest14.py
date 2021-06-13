import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.40.70;'
                      'Database=EMPRESS_5_0_OG_LIVE;'
                      'UID=sa;'
                      'PWD=Orion1234!;'
                      'Trusted_Connection=no;')
c = 60387
sql = f'select * from [EMPRESS_5_0_OG_LIVE].[dbo].[AttendanceLog] where UserId={c} order by AttendanceDate desc OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY'
cursor = conn.cursor()
cursor.execute(
    sql)

for row in cursor:
    print(row)
