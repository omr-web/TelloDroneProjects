import KeyboardControl as kp
from djitellopy import tello
from time import sleep


def GetKeyboardInput():
    left_right , forward_backward , up_down ,yaw = 0 , 0 , 0 , 0
    speed = 30

    if kp.getKey("LEFT"):
        left_right = -speed
    elif kp.getKey("RIGHT"):
        left_right = speed

    if kp.getKey("w"):
        up_dowqqqn = speed
    elif kp.getKey("s"):
        up_down = -speed

    if kp.getKey("UP"):
        forward_backward = speed
    elif kp.getKey("DOWN"):
        forward_backward = -speed

    if kp.getKey("a"):
        yaw = speed
    elif kp.getKey("d"):
        yaw = -speed

    if kp.getKey("q"): #LAND
        me.land()

    if kp.getKey("e"): #TAKEOFF
        me.takeoff()
    return [left_right , forward_backward , up_down ,yaw]



#####################################
kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())




#me.takeoff()


while True:
    vals=GetKeyboardInput()
    print(vals)
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    sleep(0.05)


