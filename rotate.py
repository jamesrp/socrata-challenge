def timestring_to_minutes(timestring):
    """Convert '[H]H:MM AM' to a int = number of minutes since midnight."""
    try:
        hour_minute, tag = timestring.split(' ')
        hour, minute = [int(x) for x in hour_minute.split(':')]
        assert(0 <= hour <= 12)
        assert(0 <= minute <= 59)
        assert(tag == 'PM' or tag == 'AM')
    except:
        raise ValueError, "Input not a valid timestring."
    total = int(minute)
    # hour 12 is actually 0 minutes
    if hour != 12:
        total += 60 * hour
    if tag == 'PM':
        total += 720
    return total

def degrees_traveled(time1,time2):
    """Return the degrees traveled by the minute hand from time1 to time2."""
    minutes1 = timestring_to_minutes(time1)
    minutes2 = timestring_to_minutes(time2)
    difference = minutes2 - minutes1
    if difference < 0:
        difference += 1440
    return difference * 6

