#Input: total_seconds
#Constants: SECONDS_PER_HOUR = 3600
#           SECONDS_PER_MINUTE = 60

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60


def seconds_to_hours_minutes_seconds(seconds):
    hours = seconds // SECONDS_PER_HOUR
    minutes = (seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds_final = seconds - hours * SECONDS_PER_HOUR - minutes * SECONDS_PER_MINUTE
    return hours, minutes, seconds_final
