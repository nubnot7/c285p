"""forest_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = 64

wheel1=robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2=robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3=robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4=robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

speed=4

keyboard.enable(timestep)
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while (robot.step(timestep) !=-1):

    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    if(key_pressed== 315):
        wheel1.setVelocity(speed)
        wheel2.setVelocity(speed)
        wheel3.setVelocity(speed)
        wheel4.setVelocity(speed)
    
    if(key_pressed== 317):
        wheel1.setVelocity(-speed)
        wheel2.setVelocity(-speed)
        wheel3.setVelocity(-speed)
        wheel4.setVelocity(-speed)
        
    if(key_pressed== 314):
        wheel1.setVelocity(-speed)
        wheel2.setVelocity(speed)
        wheel3.setVelocity(-speed)
        wheel4.setVelocity(speed)
    
    if(key_pressed== 316):
        wheel1.setVelocity(speed)
        wheel2.setVelocity(-speed)
        wheel3.setVelocity(speed)
        wheel4.setVelocity(-speed)
    
    if(key_pressed== -1):
        wheel1.setVelocity(0)
        wheel2.setVelocity(0)
        wheel3.setVelocity(0)
        wheel4.setVelocity(0)

    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)


# Enter here exit cleanup code.
