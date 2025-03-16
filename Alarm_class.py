import datetime, time
import display

class Alarm:
    def __init__(self, alarm, ampm_hour, format, mode):
        self.alarm = alarm
        self.ampm_hour = ampm_hour
        self.format = format
        self.mode = mode

        self.ring = False
        self.timeout = 0
        self.sound = "alarm.mp3"
        
    def display_alarm(self, clock_time):
        while True:
            if not self.ring:
                if self.mode == False:
                    display.alarm_24h(self)
                else:
                    display.alarm_12h(self)
            

            if int(self.alarm[0]) == int(clock_time.clock[0]) and int(self.alarm[1]) == int(clock_time.clock[1]) and int(self.alarm[2])+1 == int(clock_time.clock[2]):
                self.timeout = 10
                self.ring = self.alarm_ring()
                

            if self.ring and self.timeout == 0:
                self.ring = self.alarm_stop()

            if self.timeout > 0:
                time.sleep(1)
                self.timeout -= 1

            

    def change_alarm(self):
        while True:
            user_alarm = display.input_user_alarm()
                        
            #Verify if it's a number
            try:
               test = int(user_alarm)
            except Exception:
                display.error_NaN()
                continue

            #Verify if the input contain exactly 6 numbers
            if len(user_alarm) != 6:
                display.error_number_length()
                continue

            #Verify if it's a valid hour with datetime error directly
            try:
                test = datetime.datetime(1970, 1, 1, int(user_alarm[:2]), int(user_alarm[2:4]), int(user_alarm[4:]))
            except Exception:
                display.error_invalid_time()
                continue

            if self.mode == True:
                user_format = display.input_user_format(user_alarm)
                        
                if user_format != "AM" and user_format != "PM":
                    display.error_format()
                    continue

                if int(user_alarm[:2]) > 12:
                    display.error_invalid_time(self.mode)
                    continue

                self.format = user_format
                if user_format == "PM" and user_alarm[:2] != "12":
                    user_alarm = str(int(user_alarm[:2])+12) + user_alarm[2:]
                elif user_format == "AM" and user_alarm[:2] == "12":
                    user_alarm[:2] = "00"

            display.message_alarm_valid()
                
            self.alarm = (user_alarm[:2], user_alarm[2:4], user_alarm[4:])

            
            if int(user_alarm[:2]) > 11:
                if user_alarm[:2] == "12":
                    self.ampm_hour = user_alarm[:2]
                else:
                    if int(user_alarm[:2]) < 22:
                        self.ampm_hour = "0" + str(int(user_alarm[:2])-12)
                    else:
                        self.ampm_hour = str(int(user_alarm[:2])-12)
                self.format = "PM"
            
            else:
                if user_alarm[:2] == "00":
                    self.ampm_hour = "12"
                else:
                    self.ampm_hour = user_alarm[:2]
                self.format = "AM"
                    
            

            return
        
    def alarm_ring(self):
        display.alarm_on(self.mode)
        #play.sound(self.alarm_sound)
        return True
    
    def alarm_stop(self):
        display.alarm_off(self.mode)
        #stop.sound(self.alarm_sound)
        return False