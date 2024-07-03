import time
from pymultiwii import MultiWii

# Replace 'COM3' with the correct serial port for your setup
board = MultiWii("COM3")

# Define the tolerance range for hovering (in degrees for lat/lon and meters for altitude)
TOLERANCE_LAT_LON = 0.00001  # approximately 1 meter
TOLERANCE_ALTITUDE = 1.0  # 1 meter
HOVER_TIME_REQUIRED = 15  # in seconds

def get_drone_position():
    try:
        board.getData(MultiWii.GPS)
        latitude = board.gps['lat'] / 10000000.0  # Latitude in degrees
        longitude = board.gps['lon'] / 10000000.0  # Longitude in degrees
        altitude = board.gps['alt'] / 100.0  # Altitude in meters
        timestamp = time.time()
        return (latitude, longitude, altitude, timestamp)
    except Exception as e:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Error getting data: {e}")
        return None

def is_hovering(position_history):
    if len(position_history) < 2:
        return False

    latitudes = [pos[0] for pos in position_history]
    longitudes = [pos[1] for pos in position_history]
    altitudes = [pos[2] for pos in position_history]

    lat_variance = max(latitudes) - min(latitudes)
    lon_variance = max(longitudes) - min(longitudes)
    alt_variance = max(altitudes) - min(altitudes)

    return lat_variance <= TOLERANCE_LAT_LON and lon_variance <= TOLERANCE_LAT_LON and alt_variance <= TOLERANCE_ALTITUDE

def main():
    position_history = []

    while True:
        current_position = get_drone_position()
        if current_position:
            position_history.append(current_position)

            # Keep only the positions from the last 15 seconds
            current_time = time.time()
            position_history = [pos for pos in position_history if current_time - pos[3] <= HOVER_TIME_REQUIRED]

            if is_hovering(position_history):
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Drone has been hovering for the last 15 seconds.")
            else:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Drone is not hovering.")
        else:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - No current position data available.")

        time.sleep(1)

if __name__ == "__main__":
    main()
