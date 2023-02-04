import time

import KeyboardControl as kp
from djitellopy import tello
import time
import cv2
import numpy as np
import math

global img
###### VARIABLES #####
x,y = 500,500
angle = 0
yaw_angle = 0
points = [] 

#### PARAMETERS ######
LinearVelocity = 117/10 # forward Speed in cm/s (15 cm/s)
AngularVelocity =360/10 # Angular Speed  (Degres/s)
interval = 0.25 
dInterval = LinearVelocity * interval # dx
aInterval = AngularVelocity * interval # dalpha
######### FUNCTIONS ###############
def GetKeyboardInput():
    print("keyobard init")
    left_right , forward_backward , up_down ,yaw = 0 , 0 , 0 , 0
    speed = 30
    d = 0
    global yaw_angle,x,y,angle
    if kp.getKey("LEFT"):
        left_right = -speed
        d = dInterval
        angle = -180
    elif kp.getKey("RIGHT"):
        left_right = speed
        d = -dInterval
        angle = 180

    if kp.getKey("w"):
        up_dowqqqn = speed
    elif kp.getKey("s"):
        up_down = -speed

    if kp.getKey("UP"):
        forward_backward = speed
        d = dInterval
        angle = 270
    elif kp.getKey("DOWN"):
        forward_backward = -speed
        d = -dInterval
        angle = -90

    if kp.getKey("a"):
        yaw = speed
        yaw_angle += aInterval
    elif kp.getKey("d"):
        yaw = -speed
        yaw_angle -= aInterval


    if kp.getKey("q"): #LAND
        me.land()

    if kp.getKey("e"): #TAKEOFF
        me.takeoff()
    if kp.getKey("z"):
        cv2.imwrite(f'/home/omer/TelloDrone/{time.time()}.jpg',img)
        time.sleep(0.3)

    angle += yaw_angle
    x += int(d*math.cos(math.radians(angle)))
    y += int(d*math.sin(math.radians(angle)))
    print("keyobard return")

    return [left_right , forward_backward , up_down ,yaw , x , y ]



def drawPoints(img,points):
    for point in points:
        print("draw points")
        cv2.circle(img, point,5,(0,0,255),cv2.FILLED)


############## MAIN CODES   ######################
kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())




#me.takeoff()qeeeee

me.streamon()

while True:
    vals=GetKeyboardInput()
    me.send_rc_control(vals[0],vals[1],vals[2],vals[3])

    img = np.zeros((1000,1000,3),np.uint8)
    points.append((vals[4],vals[5]))
    drawPoints(img,points)
    cv2.imshow("output",img)
    cv2.waitKey(1)





