def main():
    is_armed = True
    motion_detected = True
    door_open = False
    is_afternoon = True
    display_alarm()

def display_alarm(arm, ms, dop, an):
    if arm:
        if ms:
            print("INTRUDER")
        if dop:
            print("door is open")

    else:
        if an: 
            print("Welcome home")


main()