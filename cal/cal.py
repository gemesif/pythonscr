import calendar
from calendar import HTMLCalendar

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()




year = 2016
month = 1
cal = calendar.month(year, month)


# print(cal)

tc= calendar.HTMLCalendar(firstweekday=0)
print(tc.formatday(11, 2))
# print(tc.formatmonth(2016, 5, 0, ))
