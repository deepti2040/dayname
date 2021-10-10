# python program to find day of 
# the week for a given date import datetime

from datetime import date
import calendar 
def findDay(date):
		day,month,year = (int(i) for i in date.split(''))
		dayNumber = calendar.weekday(year,month,day)
				days = ["1 Monday" , "2 Tuesday" , "3 Wednesday" , "4 Thursday" , "5 Friday" , "6 Saturday" , "7 Sunday" ]
		
		return (days[dayNumber])
		#Driver program

		date = '14 10 2021'
		print(findDay(date))