def calculateCPS(clicks, seconds):
    cps = clicks/seconds

    return cps

def calculateTotalTime(blocks, speed):
    time = 1/speed
    totalTime = time * blocks

    return totalTime

print("This version of the program is DEPRECIATED now! Consider using the better C++ version.")
print("For calculating CPS in GD. This calculator assumes your in-game speed, total clicks, cps, and fps are constant.\n")
gameTime = [8.372, 10.386, 12.914, 15.600, 19.200]

while (True):
    while (True):
        try:
            totalClicks = input("Input total # of clicks in a block segment: ")
            # Used to convert *10^ to e+
            totalClicks = totalClicks.replace("*10^", "e+")
            totalClicks = totalClicks.replace("x10^", "e+")
            totalClicks = float(totalClicks)
        except:
            print("Input valid float.")
        else:
            break
    while (True):
        try:
            totalBlocks = input("Input total # of blocks traveled: ")
            # Used to convert *10^ to e+
            totalBlocks = totalBlocks.replace("*10^", "e+")
            totalBlocks = totalBlocks.replace("x10^", "e+")
            totalBlocks = float(totalBlocks)
        except:
            print("Input valid float.")
        else:
            break
    while (True):
        try:
            ingameSpeed = float(input("Input in-game speed (0.5, 1, 2, 3, 4): "))
        except:
            print("Input valid float.")
        else:
            break

    if (ingameSpeed < 1): ingameSpeed = 0
    if (ingameSpeed > 4): ingameSpeed = 4
    ingameSpeed = int(ingameSpeed)

    totalTime = calculateTotalTime(totalBlocks, gameTime[ingameSpeed])
    totalUnits = totalBlocks * 30
    cps = calculateCPS(totalClicks, totalTime)
    print("\nCPS: " + str(cps) + "\nFPS Required: " + str(cps*2) + "\nIn " + str(totalTime) + " seconds (" + str(totalUnits) + " units).")
    confirm = input("\nCalculate more? (Y/n): ")
    confirm = confirm.lower()
    if (confirm == "n"):
        break
