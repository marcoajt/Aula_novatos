import calendar
from datetime import date

WEEKDAYS = {
    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
    'Friday': 4, 'Saturday': 5, 'Sunday': 6
}

class MeetupDayException(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def meetup(year, month, week, weekday):
    wd = WEEKDAYS[weekday]
    _, days_in_month = calendar.monthrange(year, month)
    
    candidates = []
    for day in range(1, days_in_month + 1):
        if calendar.weekday(year, month, day) == wd:
            candidates.append(date(year, month, day))
    
    if not candidates:
        raise MeetupDayException("That day does not exist.")
    
    if week == 'teenth':
        for d in candidates:
            if 13 <= d.day <= 19:
                return d
    elif week == 'first':
        return candidates[0]
    elif week == 'second':
        return candidates[1]
    elif week == 'third':
        return candidates[2]
    elif week == 'fourth':
        return candidates[3]
    elif week == 'fifth':
        if len(candidates) < 5:
            raise MeetupDayException("That day does not exist.")
        return candidates[4]
    elif week == 'last':
        return candidates[-1]
    else:
        raise ValueError("Invalid week")
