from datetime import datetime, timedelta

today_date = datetime.now()
print("Today is " + str(today_date))

one_day = timedelta(1)
yesterday = today_date - one_day
print("Yesterday was " + str(yesterday.day))

student_birthday = input("What is your birthday (dd/mm/yyyy)? ")
student_birthday_date = datetime.strptime(student_birthday, '%d/%m/%Y')

### Exercise: Find how many days to the next birthday.
# 1. First find this year's birthday by replacing the year with current year. 
# 2. Then check if the birthday has happened this year already 
# 3. If it has, subtract from next year's date.
# 4. If it hasn't, subtract from it.

# 1.
today_year = today_date.year
this_year_birthday = student_birthday_date.replace(year=today_year)

# 2.
if (today_date - this_year_birthday) >= 0:
    print("Success")
else:
    pass

print(this_year_birthday)
days_to_birthday = student_birthday_date - today_date
print(f'It is {str(days_to_birthday)} days to your birthday! Hurray!!!')