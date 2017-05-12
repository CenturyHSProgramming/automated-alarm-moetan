# automatedAlarm.py
# by _______

# Write function defintion: automatedAlarm()

# Make sure it returns a value

def automatedAlarm(day,noSchool):
    if day in('Saturday','Sunday'):
            return '9:00'
    elif noSchool==False:
        if day in('Monday', 'Tuesday','Thursday','Friday'):
            return '7:00'
        elif day=='Wednesday':
            return '7:30'
    elif noSchool==True:
        if day== 'Monday':
            return '9:30'
        elif day in('Wednesday', 'Tuesday','Thursday','Friday'):
            return '8:30'

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
