def survivedRobotsHealths(positions, healths, directions):
        
    robots = []
    for i in range(len(positions)):
        robots.append([positions[i], healths[i], directions[i], i])
        
    robots.sort()
    alive = []
        
    for robot in robots:
        while alive and alive[-1][2] == 'R' and robot[2] == 'L':
                
            if alive[-1][1] > robot[1]:
                alive[-1][1] -= 1
                break
                
            elif alive[-1][1] < robot[1]:
                robot[1] -= 1
                alive.pop()
                
            else:
                alive.pop()
                break
        else:
            alive.append(robot)
        
    alive.sort(key=lambda x: x[3])
    return [r[1] for r in alive]


positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))

positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
print(survivedRobotsHealths(positions, healths, directions))

positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"
print(survivedRobotsHealths(positions, healths, directions))
