def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(yr,mnt):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  check_leap_year = is_leap(yr)
  month_index = mnt -1
  if mnt ==2 and check_leap_year:
    return 29
  else:
    return month_days[month_index]
  
#🚨 Do NOT change any of the code below 🚨
year = int(input("Enter Year: \n")) # Enter a year
month = int(input("Enter month\n")) # Enter a month
days = days_in_month(year, month)
print(f"Number of days in year {year} {month}th month is {days}")

