# 3) breakdown_time(seconds)
#   Convert a non-negative integer number of seconds into as few units as
#   possible using 3600, 60, and 1. Return a dictionary like {3600: h, 60: m, 1: s}.
#   If input is invalid (not int or negative), return -1.
#   For seconds == 0, return {}.


seconds = 3600

def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    
    if seconds == 0:
        return {}
    
    HoursRest = seconds % 3600
    
    Hours = (seconds-HoursRest)/3600
    
    MinutesRest = HoursRest % 60
    
    Minutes = (HoursRest - MinutesRest)/60
    
    
        
    dictionary = {3600: Hours, 60: Minutes, 1: MinutesRest}
    
    
    return dictionary
    
    
    pass

print(breakdown_time(seconds))