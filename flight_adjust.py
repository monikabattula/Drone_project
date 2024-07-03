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
def visualize_servo_control(distance, servo_angle1, servo_angle2, plot_axis):
    plot_axis.clear()
    plot_axis.plot([0, 1], [0, distance], label='Ultrasonic Sensor')
    plot_axis.scatter(1, distance, color='red', label='Detected Mango')
    plot_axis.text(1.1, distance, f'{distance:.2f} cm', color='red')
    
    plot_axis.set_xlim(0, 1.5)
    plot_axis.set_ylim(0, 25)
    plot_axis.set_xlabel('Position')
    plot_axis.set_ylabel('Distance (cm)')
    plot_axis.set_title(f'Servo Control Simulation\nServo 1: {servo_angle1}°, Servo 2: {servo_angle2}°')
    plot_axis.legend()
    plt.pause(0.01)

# Main simulation loop
def main():
    fig, plot_axis = plt.subplots()
    plt.ion()  # Turn on interactive mode

    servo_angle1 = 0  # Default position
    servo_angle2 = 0  # Default cutting mechanism position
    controlServo(servo_angle1, 1)
    controlServo(servo_angle2, 2)

    try:
        while True:
            distance = measureDistance()
            print(f"Measured Distance: {distance:.2f} cm")
            
            if distance < 10:
                servo_angle1 = 33.69  # Move end effector to calculated angle
                controlServo(servo_angle1, 1)
                servo_angle2 = 45  # Perform cutting at 45 degrees
                controlServo(servo_angle2, 2)
            else:
                servo_angle1 = 0  # Default position
                controlServo(servo_angle1, 1)
                servo_angle2 = 0  # Default cutting mechanism position
                controlServo(servo_angle2, 2)
            
            visualize_servo_control(distance, servo_angle1, servo_angle2, plot_axis)
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()