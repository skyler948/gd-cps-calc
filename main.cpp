#include <iostream>
#include <math.h>

using namespace std;

float calculateTotalTime(float blocks, float speed)
{
    float time = 1/speed;
    float totalTime = time * blocks;

    return totalTime;
}

float calculateCPS(float time, float clicks)
{
    float cps = clicks/time;

    return cps;
}

float runCalculations(const float gameTime[])
{
    float totalClicks;
    cout << "\nInput total # of clicks in a block segment: ";
    cin >> totalClicks;

    float totalBlocks;
    cout << "Input total # of blocks traveled: ";
    cin >> totalBlocks;

    float gameSpeed;
    cout << "Input in-game speed (0.5, 1, 2, 3, 4): ";
    cin >> gameSpeed;

    if (gameSpeed < 1) gameSpeed = 0;
    if (gameSpeed > 4) gameSpeed = 4;
    gameSpeed = round(gameSpeed);
    int gameSpeedInt = int(gameSpeed);

    float totalTime = calculateTotalTime(totalBlocks, gameTime[gameSpeedInt]);
    float totalCPS = calculateCPS(totalTime, totalClicks);

    return totalCPS;
}

void multiCalc(const float gameTime[], int speedSegments)
{
    float allValues[speedSegments];
    float averageCPS;
    for (int i = 0; i < speedSegments; i++)
    {
        allValues[i] = runCalculations(gameTime);
        averageCPS += allValues[i];
    }
    averageCPS = averageCPS / speedSegments;
    
    cout << "\nIndividual values | ";
    for (int i = 0; i < speedSegments; i++)
    {
        cout << "CPS: " << allValues[i] << ", FPS: " << allValues[i] * 2 << " | ";
    }
    cout << "\nAverages | CPS: " << averageCPS << ", FPS: " << averageCPS*2 << " | " << endl;
}

int main()
{
    const float inGameTime[5] = {8.372, 10.386, 12.914, 15.600, 19.200};

    int speedSegments;
    cout << "For calculating CPS in GD. How many speed segments? (1 = Constant speed): ";
    cin >> speedSegments;

    float singleSegmentCPS;

    if (speedSegments <= 1)
    {
        singleSegmentCPS = runCalculations(inGameTime);
        cout << "\nCPS: " << singleSegmentCPS << " | FPS: " << singleSegmentCPS*2 << endl; 
    }
    else
    {
        multiCalc(inGameTime, speedSegments);
    }

    return 0;
}