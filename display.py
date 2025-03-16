#TODO variable for each line (l) + the "clear line" separated + the "save cursor"

#TODO display available commands

#TODO center the display

# ANSI codes
dic_cursor = {
    "delete_line_1-clock": "\033[s\033[H\033[2K",
    "delete_line_2-alarm": "\033[s\033[H\033[1B\033[2K",
    "delete_line_3-message": "\033[H\033[2B\033[2K",
    "delete_line_4-command": "\033[H\033[3B\033[2K",
    "delete_line_5-input": "\033[H\033[4B\033[2K",
    "delete_line_6-error": "\033[H\033[5B\033[2K",

    "cursor_position_load": "\033[u",

    "cursor_after_alarm": "\033[s\033[H\033[1B\033[8C",
    "delete_after_alarm": "\033[s\033[H\033[1B\033[8C\033[0K",
    "cursor_after_alarm_12h": "\033[s\033[H\033[1B\033[11C",
    "delete_after_alarm_12h": "\033[s\033[H\033[1B\033[11C\033[0K",

    "cursor_move_left_2": "\033[2D",
    "cursor_move_left_8": "\033[8D",

    "delete_all_after_position": "\033[0J",
    "delete_all": "\033[H\033[0J"
}

# Special actions
def all_clear():
    print(dic_cursor["delete_all"], end="", flush=True)

# Line 1 - Clock
def clock_12h(clock_time):
    print(f"{dic_cursor["delete_line_1-clock"]}{clock_time.ampm_hour}:{clock_time.clock[1]}:{clock_time.clock[2]} {clock_time.format}{dic_cursor["cursor_position_load"]}", end="", flush=True)

def clock_24h(clock_time):
    print(f"{dic_cursor["delete_line_1-clock"]}{clock_time.clock[0]}:{clock_time.clock[1]}:{clock_time.clock[2]}{dic_cursor["cursor_position_load"]}", end="", flush=True)

# Line 2 - Alarm
def alarm_12h(alarm_time):
    print(f"{dic_cursor["delete_line_2-alarm"]}{alarm_time.ampm_hour}:{alarm_time.alarm[1]}:{alarm_time.alarm[2]} {alarm_time.format}{dic_cursor["cursor_position_load"]}", end="", flush=True)

def alarm_24h(alarm_time):
    print(f"{dic_cursor["delete_line_2-alarm"]}{alarm_time.alarm[0]}:{alarm_time.alarm[1]}:{alarm_time.alarm[2]}{dic_cursor["cursor_position_load"]}", end="", flush=True)

def alarm_on(mode):
    if mode == True:
        print(f"{dic_cursor["cursor_after_alarm_12h"]} Ring Ring!! Ring Ring!!{dic_cursor["cursor_position_load"]}", end="", flush=True)
    else:
        print(f"{dic_cursor["cursor_after_alarm"]} Ring Ring!! Ring Ring!!{dic_cursor["cursor_position_load"]}", end="", flush=True)

def alarm_off(mode):
    if mode == True:
        print(f"{dic_cursor["delete_after_alarm_12h"]}{dic_cursor["cursor_position_load"]}", end="", flush=True)
    else:
        print(f"{dic_cursor["delete_after_alarm"]}{dic_cursor["cursor_position_load"]}", end="", flush=True)

# Line 3 - Message

def message_first_time():
    print(f"{dic_cursor["delete_line_3-message"]}Bienvenue dans Horloge.", end="", flush=True) #ZA WARUDO!!!

def message_alarm_valid():
    print(f"{dic_cursor["delete_line_3-message"]}Alarme changé avec succes!{dic_cursor["cursor_position_load"]}", end="", flush=True)

def message_clock_valid():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge changé avec succes!{dic_cursor["cursor_position_load"]}", end="", flush=True)

def message_stop():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge stoppé.", end="", flush=True) #ZA WARUDO!!!

def message_start():
    print(f"{dic_cursor["delete_line_3-message"]}Horloge redémarré.", end="", flush=True) #TOKI WO UGOKIDASU.

def message_help():
    print(f"{dic_cursor["delete_line_3-message"]}(H)orloge ; (A)larme ; (M)ode ; (S)top ; (D)émarrer ; (C)ommandes pour réafficher cette liste", end="", flush=True) #TOKI WO UGOKIDASU.

def message_byebye():
    print(f"{dic_cursor["delete_line_3-message"]}Le programme va quitter...", end="", flush=True) #My final message.


# Line 4 - Commands
def input_command():
    return input(f"{dic_cursor["delete_line_4-command"]}{dic_cursor["delete_all_after_position"]}Commande : ").lower()

# Line 5 - Input
def input_clock_config():
    return input(f"{dic_cursor["delete_line_5-input"]}{dic_cursor["delete_all_after_position"]}Configurer l'heure en: (M)anuel, (A)uto? ").lower()

def input_user_clock():
    return input(f"{dic_cursor["delete_line_5-input"]}Veuillez entrer l'heure au format hh:mm:ss : ________{dic_cursor["cursor_move_left_8"]}").replace(":", "")

def input_user_format(user_time):
    return input(f"{dic_cursor["delete_line_5-input"]}Veuillez entrer AM ou PM : {user_time[:2]}:{user_time[2:4]}:{user_time[4:]} __{dic_cursor["cursor_move_left_2"]}").upper()

def input_user_alarm():
    return input(f"{dic_cursor["delete_line_5-input"]}Veuillez entrer l'alarme au format hh:mm:ss : ________{dic_cursor["cursor_move_left_8"]}").replace(":", "")

# Line 6 - Errors
def error_invalid_time(mode):
    if mode == True:
        print(f"{dic_cursor["delete_line_6-error"]}/!\\Entrer une heure valide! (01-12):(00-59):(00-59)", end="")
    else:
        print(f"{dic_cursor["delete_line_6-error"]}/!\\Entrer une heure valide! (00-23):(00-59):(00-59)", end="")

def error_NaN():
    print(f"{dic_cursor["delete_line_6-error"]}/!\\Enter uniquement des chiffres ou des \":\"!", end="")

def error_number_length():
    print(f"{dic_cursor["delete_line_6-error"]}/!\\Enter exactement 6 chiffres au total!", end="")

def error_format():
    print(f"{dic_cursor["delete_line_6-error"]}/!\\Enter AM ou PM!", end="")

def commands():
    print(f"{dic_cursor["delete_line_6-error"]}(H)orloge pour modifier le temps ; (A)larme pour configurer une alarme ; (M)ode pour changer entre l'affichage 12h et 24h ; (S)top pour arreter l'horloge et (D)émarrer pour la reprendre ; (C)ommandes pour réafficher cette liste", end="")
    




