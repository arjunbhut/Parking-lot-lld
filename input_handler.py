from parking_lot import *
from parking_slot import *

def input_manager(lines):
    
    parking_lot_obj = ''
    for line in lines:
        inputs = line.strip().split(" ")

        if inputs[0] == "create_parking_lot":
            id = inputs[1]
            floors = int(inputs[2])
            slots_per_floor = int(inputs[3])

            parking_lot_obj = ParkingLot(id=id, 
                                         floors=floors, 
                                         slots_per_floor=slots_per_floor
                                         )
            parking_lot_obj.create_parking_slots()

        if inputs[0] == "display":
            type_of_count = inputs[1]
            vehicle_type = inputs[2]
            if type_of_count == "free_count":
                result = parking_lot_obj.get_free_count_for_vehicle(vehicle_type)
                for floor, count in result.items():
                    print(f"No. of free slots for {vehicle_type} on Floor {floor}: ", count)
            elif type_of_count == "free_slots":
                result = parking_lot_obj.get_free_slots_for_vehicle(vehicle_type)
                for floor, list_of_free_slots in result.items():
                    print(f"Free slots for {vehicle_type} on Floor {floor}: ", list_of_free_slots)
            else:
                result = parking_lot_obj.get_occupied_slots_for_vehicle(vehicle_type)
                for floor, list_if_occupied_slots in result.items():
                    print(f"Occupied slots for {vehicle_type} on Floor {floor}: ", list_if_occupied_slots)
        
        # park_vehicle CAR KA-01-DB-1234 black
        if inputs[0] == "park_vehicle":
            vehicle_type = inputs[1]
            registration = inputs[2]
            color = inputs[3]
            parking_slot = parking_lot_obj.find_parking_slot_for_vehicle(vehicle_type)
            if isinstance(parking_slot, str):
                print("Parking Lot Full")
            else:
                ticket_id = parking_slot.park_vehicle(registration, color)
                print("Parked vehicle. Ticket ID: ", ticket_id)
        
        if inputs[0] == "unpark_vehicle":
            ticket_id = inputs[1]
            ticket_parts = ticket_id.split("_")
            floor_no = int(ticket_parts[1])
            slot_no = int(ticket_parts[2])
            max_floors = parking_lot_obj.get_max_floors()
            max_slots = parking_lot_obj.get_max_slots()
            if floor_no > max_floors or slot_no > max_slots:
                print("Invalid Ticket")
                continue
            parking_slot = parking_lot_obj.get_parking_slot_from_ticket_id(ticket_id)
            result = parking_slot.unpark_vehicle()
            if not result.get('registration', ''):
                print("Invalid Ticket")
            else: 
                print("Unparked vehicle with Registration Number: ",result['registration'], " and Color: ", result['color'])           




        