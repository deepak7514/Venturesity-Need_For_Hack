import datetime
while True:
    date=raw_input("Enter date in format dd-mm-yyyy: ")
    if not date:
        print 'Please provide input'
        continue
    date=date.strip().split('-')
    if len(date)!=3:
        print 'Day, Month and Year should be separated by \'-\'.'
        continue
    d,m,y=date
    if y.isdigit() and len(y)==4:
        y=int(y)
    else:
        print 'Year should be 4-digit.'
        continue
    if m.isdigit() and 1<=int(m)<=12:
        m=int(m)
    else:
        print 'Month should be between 1 and 12.'
        continue
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    # Check for leap year
    if (y%4 ==0 and y%100 !=0) or (y%400 ==0):
        days[1] = 29
    if d.isdigit() and 1<=int(d)<=days[m-1]:
        d=int(d)
    else:
        print 'Day should be between 1 and %d'%days[m-1]
        continue
    break
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
WeekDay = ['Monday', 'Tuesday', 'Wednesday', 'Thhursday', 'Friday', 'Saturday', 'Sunday']
print 'Day Of the year:',WeekDay[datetime.date(y,m,d).weekday()]
print 'Date: %s,%d %s %d'%(WeekDay[datetime.date(y,m,d).weekday()],d,Month[m-1],y)
