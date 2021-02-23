def angleClock(hour, minutes):  # O(1) both
    minutesAngle = minutes * 6
    hourAngle = (((hour % 12) * 30) + ((minutes / 60) * 30))
    angle = abs(hourAngle - minutesAngle)
    # print(hourAngle)
    return min(angle, 360 - angle)


def angleClock_alt(hour, minutes):  # O(1) both
    """
    Calculate everything on a minute basis
    In one minute, the minute hand moves by 360/60 degrees. Thus, for n minutes it's 360/60 * n
    For hours, we first do % division b/c otherwise numbers can be too large. In one minute, the hour rotates by 30 / 60 = 0.5 degrees
    """
    minute_angle = 360 / 60 * minutes
    hour_angle = ((hour % 12) + (minutes / 60)) * 30
    diff = abs(minute_angle - hour_angle)
    if diff > 180:
        diff = 360 - diff
    return diff


if __name__ == '__main__':
    print(angleClock(12, 30))
    print(angleClock(3, 30))
    print(angleClock(12, 15))
    print(angleClock(4, 50))
    print(angleClock(12, 0))
    print(angleClock_alt(12, 30))
    print(angleClock_alt(3, 30))
    print(angleClock_alt(12, 15))
    print(angleClock_alt(4, 50))
    print(angleClock_alt(12, 0))