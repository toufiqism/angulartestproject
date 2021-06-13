import datetime

import PySimpleGUI as sg
import pyodbc

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.


layout = [
    [sg.Multiline(size=(50, 1), key='textbox')],
    [sg.Button('Ok'),
     sg.Button('Close Window')],
    [sg.Text(size=(50, 1), key='textbox2')]
]  # identify the multiline via key option

# Create the Window
random_number = 4
window = sg.Window('Test', layout, size=(640, 480)).Finalize()
# window.Maximize()
# Event Loop to process "events" and get the "values" of the inputs
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-G0K2QDC;'
                      'Database=EMPRESS_5_0_OG_LIVE;'
                      'Trusted_Connection=yes;')
# c = 0
sql = 'select * from [EMPRESS_5_0_OG_LIVE].[dbo].[AttendanceLog] where UserId={0} order by AttendanceDate desc OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY'
cursor = conn.cursor()

while True:
    event, values = window.read()
    if event in (None, 'Close Window'):  # if user closes window or clicks cancel
        break
    if event in (None, 'Ok'):
        c = int(values['textbox'])  # get the content of multiline via its unique key
        cursor.execute(
            sql.format(c))

        for row in cursor:
            sg.popup('Result : ', row)

window.close()
