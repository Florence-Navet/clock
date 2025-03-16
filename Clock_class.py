import datetime
import time, display

class Clock:
    def __init__(self, clock, ampm_hour, format, mode):
        self.clock = clock
        self.ampm_hour = ampm_hour
        self.format = format
        self.mode = mode

    def clock_ticking(self, clock_datetime):
        clock_datetime = clock_datetime + datetime.timedelta(seconds=1)
        self.clock = (clock_datetime.strftime('%H'), clock_datetime.strftime('%M'), clock_datetime.strftime('%S'))
        
        # %I = hour in 12h format
        self.ampm_hour = clock_datetime.strftime('%I')
        # %p = AM/PM
        self.format = clock_datetime.strftime('%p')

    def display_clock(self, event):
        while True:
            event.wait()
            try:
                clock_datetime = datetime.datetime(1970, 1, 1, int(self.clock[0]), int(self.clock[1]), int(self.clock[2]))
            except Exception:
                display.error_invalid_time(self.mode)

            if self.mode == False:
                display.clock_24h(self)
            else:
                display.clock_12h(self)
                
            self.clock_ticking(clock_datetime)

            time.sleep(1)

    def change_clock(self):
        while True:
            clock_config = display.input_clock_config()

            if clock_config == "automatique" or clock_config == "auto" or clock_config == "a":
                current_time = datetime.datetime.now()
                self.clock = (current_time.strftime("%H"), current_time.strftime("%M"), current_time.strftime("%S"))
                return
            
            elif clock_config == "manuel" or clock_config == "m":
                while True:
                    user_clock = display.input_user_clock()
                        
                    #Verify if it's a number
                    try:
                        test = int(user_clock)
                    except Exception:
                        display.error_NaN()
                        continue

                    #Verify if the input contain exactly 6 numbers
                    if len(user_clock) != 6:
                        display.error_number_length()
                        continue

                    #Verify if it's a valid hour with datetime error directly
                    try:
                        test = datetime.datetime(1970, 1, 1, int(user_clock[:2]), int(user_clock[2:4]), int(user_clock[4:]))
                    except Exception:
                        display.error_invalid_time()
                        continue

                    if self.mode == True:
                        user_format = display.input_user_format(user_clock)
                        
                        if user_format != "AM" and user_format != "PM":
                            display.error_format()
                            continue

                        if int(user_clock[:2]) > 12:
                            display.error_invalid_time(self.mode)
                            continue

                        self.format = user_format
                        if user_format == "PM" and user_clock[:2] != "12":
                            user_clock = str(int(user_clock[:2])+12) + user_clock[2:]
                        elif user_format == "AM" and user_clock[:2] == "12":
                            user_clock[:2] = "00"

                    display.message_clock_valid()
                    
                    self.clock = (user_clock[:2], user_clock[2:4], user_clock[4:])
                    return    
            
            else:
                continue