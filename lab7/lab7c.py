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
    """Add two Time objects and return the result."""
    seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(seconds)
def change_time(time, seconds):
    """Modify a Time object by adding or subtracting seconds."""
    new_time = sec_to_time(time_to_sec(time) + seconds)

    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

    return None
def time_to_sec(time):
    """Convert a Time object into seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def sec_to_time(seconds):
    """Convert seconds into a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
def valid_time(t):
    """Check if a time object is valid"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False

    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False

    return True
