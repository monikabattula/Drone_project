import matplotlib.pyplot as plt
import numpy as np
import time

# Simulated distance readings (in cm)
def measureDistance():
    # Generate a random distance between 5 and 20 cm for simulation purposes
    return np.random.uniform(5, 20)

# Function to simulate servo control
def controlServo(angle, servo_id):
    print(f"Servo {servo_id} moved to angle: {angle} degrees")

# Visualization function
def visualize_servo_control(distance, servo_angle1, servo_angle2, ax):
    ax.clear()
    ax.plot([0, 1], [0, distance], label='Ultrasonic Sensor')
    ax.scatter(1, distance, color='red', label='Detected Mango')
    ax.text(1.1, distance, f'{distance:.2f} cm', color='red')
    
    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 25)
    ax.set_xlabel('Position')
    ax.set_ylabel('Distance (cm)')
    ax.set_title(f'Servo Control Simulation\nServo 1: {servo_angle1}°, Servo 2: {servo_angle2}°')
    ax.legend()
    plt.pause(0.01)

# Main simulation loop
def main():
    fig, ax = plt.subplots()
    plt.ion()  # Turn on interactive mode

    servo_angle1 = 0  # Default position
    servo_angle2 = 0  # Default cutting mechanism position
    controlServo(servo_angle1, 1)
    controlServo(servo_angle2, 2)

    while True:
        distance = measureDistance()
        print(f"Measured Distance: {distance:.2f} cm")
        
        if distance < 10:
            servo_angle1 = 90  # Move end effector
            controlServo(servo_angle1, 1)
            servo_angle2 = 45  # Perform cutting
            controlServo(servo_angle2, 2)
        else:
            servo_angle1 = 0  # Default position
            controlServo(servo_angle1, 1)
            servo_angle2 = 0  # Default cutting mechanism position
            controlServo(servo_angle2, 2)
        
        visualize_servo_control(distance, servo_angle1, servo_angle2, ax)
        
        time.sleep(1)

if __name__ == "__main__":
    main()