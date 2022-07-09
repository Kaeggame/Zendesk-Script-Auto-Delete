#library from Python in order to use time in the script.
from datetime import date, timedelta

#Use to get today's date.
today = date.today()
print(today) #Use to debug and see the date.

#The variable "five_years" corresponds to today's date minus 5 years including leap year.
five_years = today - timedelta(1826.25)
print(five_years) #Use to debug and see if the date minus 5 years is good.