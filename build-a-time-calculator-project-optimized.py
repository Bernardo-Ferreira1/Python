def add_time(start, duration, week_days=None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Extract start time in 12-hour format and convert to 24-hour time
    time, period = start.split()
    hours, minutes = map(int, time.split(':'))
    
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Convert start time to total minutes
    start_minutes = hours * 60 + minutes
    
    # Convert duration time to total minutes
    dur_hours, dur_minutes = map(int, duration.split(':'))
    duration_minutes = dur_hours * 60 + dur_minutes
    
    # Calculate new time in minutes
    new_time = start_minutes + duration_minutes
    
    # Calculate number of days passed
    days_passed = new_time // 1440
    new_time = new_time % 1440  # Get the remaining minutes after full days

    # Calculate the new time in AM/PM format
    new_hours = new_time // 60
    new_minutes = new_time % 60
    
    if new_hours == 0:
        new_hours = 12
        period = 'AM'
    elif new_hours == 12:
        period = 'PM'
    elif new_hours > 12:
        new_hours -= 12
        period = 'PM'
    else:
        period = 'AM'
    
    # Format the new time
    time_str = f"{new_hours}:{new_minutes:02} {period}"
    
    # Calculate the weekday if provided
    if week_days:
        week_index = days.index(week_days.capitalize())
        new_weekday = days[(week_index + days_passed) % 7]
        if days_passed == 0:
            final_string = f"{time_str}, {new_weekday}"
        elif days_passed == 1:
            final_string = f"{time_str}, {new_weekday} (next day)"
        else:
            final_string = f"{time_str}, {new_weekday} ({days_passed} days later)"
    else:
        if days_passed == 0:
            final_string = time_str
        elif days_passed == 1:
            final_string = f"{time_str} (next day)"
        else:
            final_string = f"{time_str} ({days_passed} days later)"
    
    return final_string
