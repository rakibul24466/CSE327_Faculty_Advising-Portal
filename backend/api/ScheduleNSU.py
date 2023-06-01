from datetime import datetime, timedelta

class_days = ['S','T','R','A','M','W']


def split_class_period(start_time, duration, break_duration):
    time_slots = []
    current_time = datetime.combine(datetime.today(), start_time)
    end_time = current_time + timedelta(hours=duration)

    while current_time < end_time:
        class_start = current_time.strftime('%I:%M %p')
        current_time += timedelta(hours=1)
        class_end = current_time.strftime('%I:%M %p')
        time_slots.append(f"{class_start} - {class_end}")  # Add class period slot
        current_time += timedelta(minutes=break_duration)  # Adding the break duration
    return time_slots

# Example usage
start_time = datetime.strptime('8:00 AM','%I:%M %p').time()
duration = 10  # 10 hours (for a whole day)
break_duration = 10  # 10 minutes
time_slots = split_class_period(start_time, duration, break_duration)
class_slots = []
for i in class_days:
    for slot in time_slots:     
        class_slots.append(i +' - '+ slot)

class_schedule_tuple = ()
p=1
m=10
for i in class_days:
    class_schedule_tuple = class_schedule_tuple + tuple(zip([k for k in range(p,m)], class_slots[p-1:m]))
    p+=9
    m+=9


import pandas as pd

class_slot_data = pd.DataFrame(class_schedule_tuple)
class_slot_data.to_csv("class_slots.csv",index=False)

