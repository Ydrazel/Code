# -*- code: utf-8 -*-

def main():
    distanceKM = int(input("Enter the distance in kilometers: "))
    timeMin = int(input("Enter the durations minute part: "))
    timeSec = int(input("Enter the duration's second part: "))
    convertions(distanceKM,timeMin,timeSec)
    return distanceKM,timeMin,timeSec

def convertions(distanceKM,timeMin,timeSec):
    distanceML = distanceKM / 1.61
    totalSecs = timeMin * 60 + timeSec
    timeHr = totalSecs / pow(60,2)
    pace = (totalSecs / distanceML) / 60
    speed = distanceML / timeHr
    print(f"Average pace: {pace:.2f}")
    print(f"Average speed: {speed:.2f}")
main()
