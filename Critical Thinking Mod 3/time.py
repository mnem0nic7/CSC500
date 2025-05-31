# get current time in hours (0-23)
current_time = int(input("What is the current time (in hours, 0-23)?\n "))

# get the number of hours to wait for the alarm
wait_hours = int(input("How many hours before the alarm sounds?\n "))

# calculate when the alarm will go off
alarm_time = (current_time + wait_hours) % 24

# output the result
print(f"The alarm will go off at {alarm_time}")