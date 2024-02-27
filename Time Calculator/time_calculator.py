def add_time(start, duration, day=None):
  # Split the start time into hours and minutes
  start_time, period = start.split()
  start_hours, start_minutes = map(int, start_time.split(':'))

  # Split the duration into hours and minutes
  duration_hours, duration_minutes = map(int, duration.split(':'))

  # Convert the start time to 24-hour format
  if period == 'PM':
    start_hours += 12

  # Calculate the total minutes
  total_minutes = start_minutes + duration_minutes
  total_hours = start_hours + duration_hours + total_minutes // 60

  # Calculate the new hours and minutes
  new_hours = total_hours % 24
  new_minutes = total_minutes % 60

  # Determine the period (AM or PM)
  if new_hours < 12:
    new_period = 'AM'
  else:
    new_period = 'PM'

  # Convert the new hours to 12-hour format
  if new_hours > 12:
    new_hours -= 12
  elif new_hours == 0:
    new_hours = 12
    
  # Determine the number of days later
  days_later = total_hours // 24
  
  # Determine the day of the week
  if day:
    days_of_week = [
      'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
      'Saturday'
    ]
    day_index = days_of_week.index(day.capitalize())
    new_day_index = (day_index + days_later) % 7
    new_day = days_of_week[new_day_index]
  else:
    new_day = None
    
  # Format the new time string
  new_time = f"{new_hours}:{new_minutes:02d} {new_period}"
  if new_day:
    new_time += f", {new_day}"
  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({days_later} days later)"
    
  return new_time