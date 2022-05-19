# 100,1
def ladder(power,seconds):#100,1
    drone.set_all_led(0, 0, 255, CoDrone.Mode.BLINK)
    drone.set_pitch(power)
    drone.move(seconds)
    drone.set_pitch(0)
    drone.set_all_led(0, 0, 255, CoDrone.Mode.STROBE)
    drone.set_throttle(power)
    drone.move(seconds)
    drone.set_throttle(0)
    drone.set_all_led(255, 255, 0, CoDrone.Mode.BLINK)
    drone.set_pitch(power)
    drone.move(seconds)
    drone.set_pitch(0)
    drone.set_all_led(255, 255, 0, CoDrone.Mode.STROBE)
    drone.set_throttle(power)
    drone.move(seconds)
    drone.set_throttle(0)
    drone.set_all_led(0, 0, 255, CoDrone.Mode.BLINK)
    drone.set_pitch(power)
    drone.move(seconds)
    # now move back to ground
    drone.set_pitch(0)
    drone.set_all_led(0, 0, 255, CoDrone.Mode.STROBE)
    drone.set_throttle(-1*power)
    drone.move(seconds)
    drone.hover(1)

def pitch(power,seconds):
    drone.set_pitch(power)
    drone.move(seconds)
    drone.set_pitch(-1 * power)
    drone.move(seconds)

def roll(power,seconds):
    drone.set_throttle(50)
    drone.set_roll(power)
    drone.move(seconds)
    drone.set_roll(-1 * power)
    drone.move(seconds)

def throttle(power,seconds):
    drone.set_throttle(power)
    drone.move(seconds)
    drone.set_throttle(-1 * power)
    drone.move(seconds)

while True:
    display_menu()
    option = input("Pick an option")
    power = int(input("What is the power value?"))
    seconds = int(input("What is the move() value?"))
    resetAll()
    drone.takeoff()

    if option == "1":# 100,2
        pitch(power,seconds)

    elif option =="2":
        yaw(power,seconds)

    elif option == "3": # 100,1
        roll(power,seconds)

    elif option  == "4": # 50,2
        throttle(power,seconds)

    elif option == "5":
        square(power, seconds)

    elif option == "6":
        triangle(power, seconds)

    elif option == "7":
        circle(power, seconds)

    elif option == "8":
        verticalSquare(power, seconds)

    elif option == "9":
        ladder(power, seconds)

    elif option == "10":
        drone.land()
        drone.close()
        break
    else:
        print("you pressed a wrong key")

    resetAll()
    drone.land()