import CoDrone
from CoDrone import Direction, Degree
drone = CoDrone.CoDrone()
drone.pair(drone.Nearest)
start = input("Click any key to strat")


def display_menu():
    print("\tMenu")
    print("1. pitch\n" +
        "2. yaw\n" +
        "3. roll\n" +
        "4. throttle\n"+
        "5. Square \n"
        "6. Triangle \n"
        "7. circle\n"
        "8. verticalSquare \n"
        "9. ladder \n"
        "10. Exit")

def resetAll():
    drone.set_pitch(0)
    drone.set_yaw(0)
    drone.set_roll(0)
    drone.set_throttle(0)
    # drone.hover(1)

# 50,2
def square(power, seconds):
    drone.set_eye_led(255, 255, 0, CoDrone.Mode.SOLID)
    drone.set_all_led(0, 0, 255, CoDrone.Mode.BLINK)
    drone.set_throttle(20)
    print("setting pitch")
    drone.set_pitch(power)
    print("moving")
    drone.move(seconds)
    print("setting 90 degree")
    drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90)
    drone.set_throttle(0)
    print("setting pitch")
    drone.set_pitch(power)
    print("moving")
    drone.move(seconds)
    print("setting 90 degree")
    drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90)
    drone.set_throttle(20)
    print("setting pitch")
    drone.set_pitch(power)
    print("moving")
    drone.move(seconds)
    print("setting 90 degree")
    drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90)
    drone.set_throttle(0)
    print("setting pitch")
    drone.set_pitch(power)
    print("moving")
    drone.move(seconds)
    drone.set_throttle(-10)
    drone.set_pitch(0)
    drone.move(1)

# 100,1
def triangle(power, seconds):
    drone.set_eye_led(0, 0, 255, CoDrone.Mode.SOLID)
    drone.set_all_led(255, 255, 0, CoDrone.Mode.BLINK)
    drone.set_throttle(20)
    drone.set_pitch(power)
    drone.move(seconds)
    drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90)
    drone.set_throttle(0)
    drone.set_pitch(power)
    drone.move(seconds)
    drone.turn_degree(Direction.RIGHT, Degree.ANGLE_135)
    drone.set_throttle(10)
    drone.set_pitch(power)
    drone.move(seconds+1)

#50 4
def circle(power, seconds): #50,6
    drone.set_all_led(255, 0, 255, CoDrone.Mode.BLINK)
    drone.set_yaw(power)
    drone.set_pitch(power*1.5)
    drone.set_throttle(20)
    drone.move(seconds)
    drone.set_throttle(-20)
    drone.move(seconds)
    drone.hover(1)
    drone.set_all_led(255, 255, 0, CoDrone.Mode.BLINK)
    drone.set_yaw(power)
    drone.set_pitch(power * 1.5)
    drone.set_throttle(20)
    drone.move(seconds)
    drone.set_throttle(-20)
    drone.move(seconds)

#100 6
def yaw(power,seconds):
    drone.set_all_led(255,0,255,CoDrone.Mode.BLINK)
    drone.set_throttle(20)
    drone.set_yaw(power)
    drone.move(seconds)
    drone.set_all_led(0, 0, 255, CoDrone.Mode.STROBE)
    drone.set_throttle(0)
    drone.set_yaw(-1 * power)
    drone.set_throttle(-40)
    drone.move(7)
    drone.hover(2)
# 100,1
def verticalSquare(power,seconds):
    drone.set_all_led(0, 0, 255, CoDrone.Mode.SOLID)
    drone.set_pitch(power)
    drone.move(seconds)
    drone.set_pitch(0)
    drone.set_throttle(power)
    drone.move(seconds)
    drone.set_throttle(0)
    drone.set_pitch(-1*power)
    drone.move(seconds)
    drone.set_pitch(0)
    drone.set_throttle(-1*power)
    drone.move(seconds)
    drone.hover(1)


# def ladder (power, seconds):
#     for i in range (0,2):
#         drone.set_pitch(power)
#         drone.move(seconds)
#         drone.set_pitch(0)
#         drone.set_throttle(power)
#         drone.move(seconds)
#         drone.set_throttle(0)
#     drone.set_pitch(0)
#     drone.set_all_led(0, 0, 255, CoDrone.Mode.STROBE)
#     drone.set_throttle(-1 * power)
#     drone.move(seconds)
#     drone.hover(1)

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




