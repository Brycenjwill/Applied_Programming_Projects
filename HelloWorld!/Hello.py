from datetime import datetime

def getmonth(m):
    if(m == 1):
        return "January"
    elif(m == 2):
       return "February"
    elif(m ==3):
        return "March"
    elif(m ==4):
        return "April"
    elif(m ==5):
        return "May"
    elif(m ==6):
        return "June"
    elif(m ==7):
        return "July"
    elif(m ==8):
        return "August"
    elif(m ==9):
        return "September"
    elif(m ==10):
        return "October"
    elif(m ==11):
        return "November"
    elif(m ==12):
        return "December"
month = getmonth(datetime.now().month)

print(f"Hello World! Today is {month} {datetime.now().day}. Thanks for stopping by, I hope you have a great day.")