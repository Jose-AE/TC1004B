import motor_module 
import time



motor_module.setup()  # Call the setup function first

# Now you can use the movement functions
motor_module.forward()
time.sleep(2)  # Sleep for 2 seconds (or however long you want the motors to run)
motor_module.stop()  # Stop the motors

