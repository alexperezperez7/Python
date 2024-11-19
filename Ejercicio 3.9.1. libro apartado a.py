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
