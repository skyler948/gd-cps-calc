def calculateCPS(clicks, seconds):
    cps = clicks/seconds

    return cps

def calculateTotalTime(blocks, speed):
    time = 1/speed
    totalTime = time * blocks

    return totalTime

print("For calculating CPS in GD. This calculator assumes your in-game speed, total clicks, cps, and fps are constant.")
totalClicks = int(input("Input total # of clicks in a block segment: "))
totalBlocks = float(input("Input total # of blocks traveled: "))
ingameSpeed = float(input("Input in-game speed (0.5, 1, 2, 3, 4): "))

if (ingameSpeed == 0.5): ingameSpeed = 0
if (ingameSpeed > 4): ingameSpeed = 4
ingameSpeed = int(ingameSpeed)
gameTime = [8.372, 10.386, 12.914, 15.600, 19.200]

totalTime = calculateTotalTime(totalBlocks, gameTime[ingameSpeed])
cps = calculateCPS(totalClicks, totalTime)
print("\nCPS: " + str(cps) + "\nFPS Required: " + str(cps*2) + "\nIn " + str(totalTime) + " seconds.")
