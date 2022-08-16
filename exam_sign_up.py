#Danial Syed
#Calculates oral exam time slots
#The start_time is the when the person is first available and end_time being when they aren't available anymore. The lunch time is when they can't have a time slot since they are on lunch
#The available slots based off the previous inputs are returned
def oral_exam_sign_up(start_time, end_time, lunch_time):
    slots = 0
    hours = start_time
    mins = 0
    while(hours!=end_time):
        if hours==lunch_time and mins == 0:
            mins += 30
            if(mins >= 60):
                hours = hours + 1
                mins = mins % 60
            if hours > 12:
                hours = hours % 12
            elif hours == 0:
                hours = 12
        print(hours, ":", mins)
        mins += 10
        if(mins >= 60):
            hours += 1
            mins = mins % 60
        if hours > 12:
                hours = hours % 12
        elif hours == 0:
            hours = 12
        print(hours, ":", mins)
        slots += 1
        mins += 5
        if(mins >= 60):
            hours += 1
            mins = mins % 60
        if hours > 12:
                hours = hours % 12
        elif hours == 0:
            hours = 12
    return slots
print(oral_exam_sign_up(8,12,11))

