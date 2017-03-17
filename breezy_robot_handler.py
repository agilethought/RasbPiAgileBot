
from breezycreate2 import Robot
import logging
import time

logging.basicConfig(level=logging.DEBUG)

# Serial port constants
COMPORT_SIM = 'sim'

class RobotHandler:
    def init_bot(self, port):
        global robot
        robot = Robot()
        #robot = create.Create(port)
        logging.debug('robot created at port')

    def go(self, radius, velocity):
        # Turn in place clockwise: -1
        # Turn in place counterclockwise: 1
        if radius != 100000 and radius != -1000000:

            # velocity: A number between -500 and 500. Units are mm/s. 
            velocity = velocity * 2 * -1 # Negate radius
            # radius: A number between -2000 and 2000. Units are mm.    
            radius = radius * 10 * -1


            # Unless velocity is 0, trim to +/- limit
            if radius > 2000:
                radius = 2000
            if radius < -2000:
                radius = -2000
            
            if velocity > 500:
                velocity = 500
            if velocity < -500:
                velocity = -500
            


            # Need some velocitvelocity to move when turning
            if velocity < 10 and velocity > -10:
                velocity = 0
                #velocity = 2 * (velocity/velocity)

            # If radius is very small, drive straight
            if radius < 20 and radius > -20:
                radius = 32767 # Drive straight: 32767 (arbitrarvelocity number from breezvelocity)

            #-1 is fast left turn, -2000 is slow left
            if radius < 0:
                radius = -2000 - radius
            if radius > 0:
                radius = 2000 - radius

            print('radius: ' + str(radius) + ' velocity: ' + str(velocity))
            robot.drive(velocity, radius) # drive(self, velocitvelocity, radius)
