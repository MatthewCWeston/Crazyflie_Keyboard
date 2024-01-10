import pygame # For handling input

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.commander import Commander
URI = 'radio://0/80/2M' # Make sure this is your URI, check the UI for controllers if you're unsure.

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

cflib.crtp.init_drivers(enable_debug_driver=False)

with SyncCrazyflie(URI) as scf:
    cmd = scf.cf.commander # scf has a Crazyflie instance, which then has a commander.
    
    # Control loop
    run = True
    thrust = 10001
    thrust_inc = 5000
    yaw = 0
    yawrate = 30
    pitch = 0
    roll = 0
    straferate = 10
    
    try:
        print('''
            You can now operate your Crazyflie using the keyboard! 
            
            Tap space or c to adjust your vertical thrust.
            Hold Q or E to turn right or left.
            Hold WASD to strafe along the horizontal plane.
            Tap L to cut engine power and close the program.
            
            Please note that precise, elegant movement requires a Flow deck. I cover that sort of thing in the other script, which should be added in a little while, if it isn't there already.
        ''')
        while run:
            
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    match event.key: # WS for vertical movement
                        case pygame.K_SPACE: # Thrust up
                            thrust = min(thrust + thrust_inc, 60000)
                        case pygame.K_c: # Thrust down
                            thrust = max(thrust - thrust_inc, 10001)
                        case pygame.K_q: # Turn left
                            yaw = -yawrate
                        case pygame.K_e: # Turn right
                            yaw = yawrate
                        case pygame.K_w: # Forward
                            pitch = -straferate
                        case pygame.K_s: # Reverse
                            pitch = straferate
                        case pygame.K_a: # Left
                            roll = straferate
                        case pygame.K_d: # Right
                            roll = -straferate
                        case pygame.K_l:
                            print("L pressed!") # Abort
                            run = False
                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_q | pygame.K_e: # stop turning
                            yaw = 0
                        case pygame.K_w | pygame.K_s: # stop strafe forward/reverse
                            pitch = 0
                        case  pygame.K_a | pygame.K_d: # stop strafe left/right
                            roll = 0
            # Send a setpoint. Roll pitch yaw thrust.
            '''
                Roll turns the crazyflie side to side. Used for lateral movement. 
                Pitch turns the crazyflie up or down. Used for forward and reverse movement.
                Yaw turns the crazyflie along the horizontal plane. Used for turning.
            '''
            # degrees degrees degrees/sec [10001, 60000]
            setpoint = [roll,pitch,yaw,thrust]
            #print(f"Sending setpoint: {setpoint}")
            cmd.send_setpoint(*setpoint);
    finally:
        # cut engines and abort.
        cmd.send_stop_setpoint()    
    

pygame.quit()
exit()
