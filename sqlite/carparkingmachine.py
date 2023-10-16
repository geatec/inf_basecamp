import dataclasses as dc
import datetime as dt
import sqlite3 as sl
import os
import sys as ss

@dc.dataclass
class ParkedCar:
    id: int
    license_plate: str
    check_in: dt.datetime
    check_out: dt.datetime
    parking_fee: float

class CarParkingMachine:
    def __init__ (self):
        self.db_conn = sl.connect(os.path.join(ss.path[0], 'carparkingmachine.db'))

        self.db_conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0
            );'''
        )

        self.cur = self.db_conn.cursor ()

    def find_by_id(self, id) -> ParkedCar:
        # This method will search for a parked_car in the database based on the row ID an return a ParkedCar object with the data
        self.cur.execute ("SELECT * FROM parkings WHERE id = ?", (id,))
        print (self.cur.fetchall ())


    def find_last_checkin(self, license_plate) -> int:
        # This method will search for the last row for a given license_plate that has NOT checked-out yet (return row ID if found)
        self.cur.execute ("SELECT * FROM parkings WHERE license_plate = ?", ('7006NT',))
        print (self.cur.fetchall ())

    def insert(self, parked_car: ParkedCar) -> ParkedCar:
        # This method will insert details of a created ParkedCar object and put the new row ID (from database) on the object, return the object with this new row ID
        self.cur.execute (
            "INSERT INTO parkings VALUES (null, ?, ?, ?, ?, ?)",
            ('cpm1', parked_car.license_plate, parked_car.check_in, parked_car.check_out, parked_car.parking_fee)
        )

    def update(self, parked_car: ParkedCar) -> None:
        # This method will update details of a ParkedCar object inside the database (update based on ParkedCar.id <- Datbase Row ID)
        pass

    def show_all (self):
        self.cur.execute ("SELECT * FROM parkings")
        print (self.cur.fetchall ())

carParkingMachine = CarParkingMachine ()

parkedCar = ParkedCar (0, '7006NT', 'check_in_time', 'check_out_time', 70)
carParkingMachine.insert (parkedCar)

parkedCar2 = ParkedCar (0, '9505VJ', 'check_in_time', 'check_out_time', 80)
carParkingMachine.insert (parkedCar2)

carParkingMachine.show_all ()

carParkingMachine.find_by_id (1)
