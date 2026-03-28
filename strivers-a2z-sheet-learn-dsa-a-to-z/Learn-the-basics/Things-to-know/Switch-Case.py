# https://takeuforward.org/plus/dsa/problems/switch-case?source=strivers-a2z-dsa-track

class Solution:
    def whichWeekDay(self, day):
        if(day>7 or day<1):
            print("Invalid")
        else:
            if(day==1):
                print("Monday")
            elif(day==2):
                print("Tuesday")
            elif(day==3):
                print("Wednesday")
            elif(day==4):
                print("Thursday")
            elif(day==5):
                print("Friday")
            elif(day==6):
                print("Saturday")