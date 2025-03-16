import threading, time
import display
from Clock_class import Clock
from Alarm_class import Alarm

def command_terminal(event, clock_time, alarm_time):
    while True:
        
        command = display.input_command()
        match command:
            case "mode" | "m":
                clock_time.mode = not clock_time.mode
                if alarm_time:
                    alarm_time.mode = not alarm_time.mode

                continue
            case "horloge" | "h":
                event.clear()
                clock_time.change_clock()
                event.set()
                continue
            case "alarme" | "a":
                if not alarm_time:
                    alarm_time = Alarm(("00","00","00"),0,"", clock_time.mode)
                    threading.Thread(target=alarm_time.display_alarm, args=(clock_time,)).start()
                alarm_time.change_alarm()
                continue
            case "stop" | "s":
                event.clear()
                display.message_stop()
                continue
            case "demarrer" | "d":
                event.set()
                display.message_start()
                continue
            case "commandes" | "c":
                # display.commands()
                display.message_help()
                continue
            # case "quitter" | "q":
            #     display.message_byebye()
            #     time.sleep(3)
            #     break
            case _:
                continue

def main():
    clock_time = Clock((0,0,0),0,"", False)
    alarm_time = False
    event = threading.Event()
    quit = False

    display.all_clear()
    display.message_first_time()

    clock_time.change_clock()

    display.message_help()

    threading.Thread(target=command_terminal, args=(event, clock_time, alarm_time)).start()
    event.set()
    threading.Thread(target=clock_time.display_clock, args=(event,)).start()   

main()