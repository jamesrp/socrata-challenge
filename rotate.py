def timestring_to_minutes(timestring):
    """Convert '[H]H:MM AM' to a int = number of minutes since midnight."""
    hour_minute, tag = timestring.split(' ')
    hour, minute = hour_minute.split(':')
    total = int(minute)
    # hour 12 is actually 0 minutes
    if hour != '12':
        total += 60 * int(hour)
    if tag == 'PM':
        total += 720
    return total

def degrees_traveled(time1,time2):
    """Return the degrees traveled by the minute hand from time1 to time2."""
    minutes1 = timestring_to_minutes(time1)
    minutes2 = timestring_to_minutes(time2)
    difference = minutes2 - minutes1
    if difference < 0:
        # Correct for 24-hour day
        difference += 1440
    return difference * 6

print degrees_traveled("10:15 AM","12:45 PM")
print degrees_traveled("10:00 PM","9:00 PM")

