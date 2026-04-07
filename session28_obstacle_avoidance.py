# SESSION 28 – TESLA (Obstacle Avoidance)

def obstacle_avoidance(distance, threshold=0.3):
    if distance < threshold:
        return "Turn Right"
    else:
        return "Move Forward"

def main():
    obstacle_distance = 0.25  # in meters

    action = obstacle_avoidance(obstacle_distance)

    print("Obstacle Distance:", obstacle_distance, "m")
    print("Action:", action)

if __name__ == "__main__":
    main()
