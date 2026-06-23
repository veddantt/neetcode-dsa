class Solution:
    def carFleet(self, target, position, speed):
        # Pair each car's position with its speed
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
            
        # Sort cars based on position in descending order (closest to target first)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        fleets = 0
        current_fleet_time = 0.0
        
        for pos, spd in cars:
            # Calculate the time needed for the current car to reach the target
            # Use float() to ensure floating-point division in Python 2
            time_to_target = float(target - pos) / spd
            
            # If this car takes more time than the current fleet ahead of it,
            # it cannot catch up. It forms a brand new slower fleet.
            if time_to_target > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_target
                
        return fleets