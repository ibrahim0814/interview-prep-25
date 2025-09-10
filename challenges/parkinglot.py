import enum
from typing import List

"""
Welcome to your interview. Boilerplate is provided. Please edit the code as you see fit. To run the code at any time, hit the run button in the top left corner.

Goals: Design a parking lot using object-oriented principles

Here are a few methods that you should be able to run:

Tell us how many spots are remaining
Tell us how many total spots are in the parking lot
Tell us when the parking lot is full
Tell us when the parking lot is empty
Tell us when certain spots are full e.g. when all motorcycle spots are taken
Tell us how many spots vans are taking up
Assumptions:

The parking lot can hold motorcycles, cars and vans
The parking lot has motorcycle spots, car spots and large spots
A motorcycle can park in any spot
A car can park in a regular or large spot
A van can park in a large spot, but it will take up 3 regular spots
These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed


large spot = 3 regular spots
motorcycle spot unique, only motorcycles park there
(logic for this in our class)



ParkingLot class
    remaining
    total
    full 
    empty
    full for certain spots
    

"""
class VehicleType(enum.Enum):
    MOTORCYCLE = 'motorcycle'
    CAR = 'car'
    VAN = 'van'

class Vehicle:
    def __init__(self, type: VehicleType):
        self.type = type



class Spot:
    def __init__(self):
        self.isOccupied = False
        self.isVan = False

class ParkingLot:
    def __init__(self, motorcycleSpots: int, regularSpots: int):
        self.mSpotList = [Spot() for _ in range(motorcycleSpots)]
        self.rSpotList = [Spot() for _ in range(regularSpots)]
        self.totalSpots = motorcycleSpots + regularSpots
        
    # parking lot is full
    def isParkingLotFull(self) -> bool:
        isMFull = True
        isRFull = True

        for spot in self.mSpotList:
            if not spot.isOccupied:
                isMFull = False
                break
        
        for spot in self.rSpotList:
            if not spot.isOccupied:
                isRFull = False
                break
                
        return isMFull and isRFull
    

    def isParkingLotEmpty(self) -> bool:
        isMEmpty = True
        isREmpty = True

        for spot in self.mSpotList:
            if spot.isOccupied:
                isMEmpty = False
                break
        
        for spot in self.rSpotList:
            if spot.isOccupied:
                isREmpty = False
                break
                
        return isMEmpty and isREmpty

    def spotsRemaining(self) -> dict:

        # calculate how many motorcycle spots remain 
        mSpotsRemaining = 0
        for spot in self.mSpotList:
            if not spot.isOccupied:
                mSpotsRemaining += 1
        
        rSpotsRemaining = 0
        for spot in self.rSpotList:
            if not spot.isOccupied:
                rSpotsRemaining += 1

        
        return {
            "motorcycle": mSpotsRemaining,
            "regular": rSpotsRemaining
        }

    
    def vanSpotsTakenUp(self) -> int:
        numSpots = 0
        for spot in self.rSpotList:
            if spot.isVan:
                numSpots += 1
        return numSpots

    def occupyNextAvailableSpot(self, list: List[Spot], isVan: bool):
        numRuns = 1
        if isVan:
            numRuns = 3

        while numRuns > 0:
            for spot in list:
                if not spot.isOccupied:
                    spot.isOccupied = True
                    spot.isVan = True
                    break
            numRuns -= 1

        return list

    def park(self, vehicle: Vehicle) -> None:
        
        spotsRemaining = self.spotsRemaining()
        print('spots left', spotsRemaining)
        motorcycleSpots = spotsRemaining['motorcycle']
        regularSpots = spotsRemaining['regular']

        if vehicle.type == VehicleType.CAR:
            if regularSpots > 0:
                self.occupyNextAvailableSpot(self.rSpotList, False)
                print('Vehicle parked successfully')
            else:
                print('No spots available')
        elif vehicle.type == VehicleType.VAN:
            if regularSpots > 2:
                self.occupyNextAvailableSpot(self.rSpotList, True)
                print('Vehicle parked successfully')
            else:
                print('No Van spots available')
        elif vehicle.type == VehicleType.MOTORCYCLE:
            if motorcycleSpots > 0:
                self.occupyNextAvailableSpot(self.mSpotList, False)
                print('Vehicle parked successfully')
            elif regularSpots > 0:
                self.occupyNextAvailableSpot(self.rSpotList, False)
                print('Vehicle parked successfully')
            else:
                print('No spots available')





    



lot = ParkingLot(5, 9)
myCar = Vehicle(VehicleType.CAR)
myVan1 = Vehicle(VehicleType.VAN)
myVan2 = Vehicle(VehicleType.VAN)
myVan3 = Vehicle(VehicleType.VAN)


lot.park(myCar)
lot.park(myVan1)
lot.park(myVan2)
lot.park(myVan3)


