#  Write a function for checking the speed of drivers.
#  This function should have one parameter: speed.
#
#   a.  If speed is less than 70, it should print “Ok”.
#   b.  Otherwise, for every 5km above the speed limit (70),
#       it should give the driver one demerit point and
#       print the total number of demerit points.
#       For example,
#       if the speed is 80, it should print: “Points: 2”.
#   c. If the driver gets more than 12 points,
#       the function should print: “License suspended”

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'


print(check_speed(80))
