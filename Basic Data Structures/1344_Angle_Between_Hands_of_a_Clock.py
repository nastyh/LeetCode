def angleClock(hour, minutes):  # O(1) both
    minutesAngle = minutes * 6
    hourAngle = (((hour % 12) * 30) + ((minutes / 60) * 30))
    angle = abs(hourAngle - minutesAngle)
    return min(angle, 360 - angle)