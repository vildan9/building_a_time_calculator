def add_time(start, duration, day=None):
    # Helper function to get the name of the day
    def get_day_name(index):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[index]

    # Split the start time into time and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert 12-hour time to 24-hour time
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Split the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the end time
    end_hour = start_hour + duration_hours
    end_minute = start_minute + duration_minutes

    # Handle minute overflow
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute %= 60

    # Handle hour overflow
    days_later = end_hour // 24
    end_hour %= 24

    # Convert 24-hour time to 12-hour time
    if end_hour == 0:
        end_hour = 12
        end_period = 'AM'
    elif end_hour < 12:
        end_period = 'AM'
    elif end_hour == 12:
        end_period = 'PM'
    else:
        end_hour -= 12
        end_period = 'PM'

    # Prepare the result time string
    result_time = f"{end_hour}:{end_minute:02d} {end_period}"

    # Handle the day of the week
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(day.capitalize())
        result_day_index = (start_day_index + days_later) % 7
        result_day = days_of_week[result_day_index]
        result_time += f", {result_day}"

    # Handle "next day" or "n days later"
    if days_later == 1:
        result_time += " (next day)"
    elif days_later > 1:
        result_time += f" ({days_later} days later)"
    
    return result_time



