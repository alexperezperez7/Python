#Inputs: hours
#        minutes
#        seconds
#Constants: SECONDS_PER_HOUR = 3600
#           SECONDS_PER_MINUTE = 60

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def conversion_to_seconds(hours, minutes, seconds):
    result = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds
    return result


def seconds_to_hours_minutes_seconds(seconds):
    hours = seconds // SECONDS_PER_HOUR
    minutes = (seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds_final = seconds - hours * SECONDS_PER_HOUR - minutes * SECONDS_PER_MINUTE
    return hours, minutes, seconds_final

h1 = input('Please enter the hours(first interval):')
h1 = int(h1)
m1 = input('Please enter the minutes(first interval):')
m1 = int(m1)
s1 = input('Please enter the seconds(first interval):')
s1 = int(s1)
h2 = input('Please enter the hours(second interval):')
h2 = int(h2)
m2 = input('Please enter the minutes(second interval):')
m2 = int(m2)
s2 = input('Please enter the seconds(second interval):')
s2 = int(s2)

total_seconds_first_interval = conversion_to_seconds(h1, m1, s1)
total_seconds_second_interval = conversion_to_seconds(h2, m2, s2)

sum_of_seconds_total = total_seconds_first_interval + total_seconds_second_interval

hh, mm, ss = seconds_to_hours_minutes_seconds(sum_of_seconds_total)

print('Total hours:', hh, 'Total minutes:', mm, 'Total seconds:', ss)
