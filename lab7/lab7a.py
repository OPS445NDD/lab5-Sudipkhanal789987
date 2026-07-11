#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object as formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def sum_times(t1, t2):
    """Add two time objects and carry seconds/minutes correctly."""
    total = Time(0, 0, 0)

    total.hour = t1.hour + t2.hour
    total.minute = t1.minute + t2.minute
    total.second = t1.second + t2.second

    while total.second >= 60:
        total.second -= 60
        total.minute += 1

    while total.minute >= 60:
        total.minute -= 60
        total.hour += 1

    return total
def valid_time(t):
    """Check if a time object is valid"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False

    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False

    return True
