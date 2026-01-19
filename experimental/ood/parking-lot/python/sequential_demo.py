import logging

from src.parking_fare import FareCalculator, BaseFareStrategy, PeakHoursFareStrategy
from src.parking_lot import ParkingLot
from src.parking_manager import ParkingManager
from src.parking_spot import CompactSpot, RegularSpot, OversizedSpot
from src.vehicle import Car


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    available_spots = [
        CompactSpot(spot_number=1),
        CompactSpot(spot_number=2),
        RegularSpot(spot_number=3),
        OversizedSpot(spot_number=4)
    ]
    parking_manager = ParkingManager(available_spots)

    fare_strategies = [
        BaseFareStrategy(),
        PeakHoursFareStrategy(),
    ]
    fare_calculator = FareCalculator(fare_strategies)

    parking_lot = ParkingLot(parking_manager, fare_calculator)

    ferrari = Car("AB888BB")
    porsche = Car("BI777OO")
    ferrari_ticket = parking_lot.enter_vehicle(ferrari)
    porsche_ticket = parking_lot.enter_vehicle(porsche)
    parking_lot.leave_vehicle(porsche_ticket)
    parking_lot.leave_vehicle(ferrari_ticket)