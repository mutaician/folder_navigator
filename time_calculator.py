def add_time(start, duration, starting_day = ''):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_hr = int(start.split(' ')[0].split(':')[0])
    start_hr = start_hr + 12 if 'PM' in start else start_hr
    total_hr = start_hr + int(duration.split(':')[0])
    
    total_min = int(start.split(' ')[0].split(':')[1]) + int(duration.split(':')[1])
    total_time_min = total_hr * 60 + total_min
    final_hr = total_time_min // 60
    final_min = total_time_min % 60
    final_12_hr = final_hr % 12
    
    final_12_hr = 12 if final_12_hr == 0 else final_12_hr
    clock_format = 'PM' if final_hr % 24 >= 12 else 'AM'
    new_time = f'{final_12_hr}:{final_min:02d} {clock_format},'

    if starting_day.capitalize() in days_of_week:
        day_index = days_of_week.index(starting_day.capitalize())
        if final_hr > 24:
            day_index += final_hr // 24
            day_index %= 7
        day = days_of_week[day_index]
        new_time += f' {day}'
    if final_hr > 24 and final_hr < 48:
        new_time += ' (next day)'
    elif final_hr >= 48:
        new_time += f' ({final_hr // 24} days later)'
    print(new_time)

# Tests
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
add_time("8:16 PM", "466:02", "tuesday")