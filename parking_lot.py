
from parking_slot import *
from collections import defaultdict

class ParkingLot():

    def __init__(self, id, floors, slots_per_floor):
        self.id = id
        self.floors = floors
        self.slots_per_floor = slots_per_floor
        self.slots = {}
        self.current_avaiable_slots = {}
        self.ticket_id_to_slot_key = {}
    
    def get_parking_lot_id(self):
        return self.id
    
    def get_ticket_id_for_slot(self, slot_key):
        parking_lot_id = self.get_parking_lot_id()
        ticket_id = str(parking_lot_id) + "_" +slot_key
        return ticket_id

    def create_parking_slots(self):

        parking_lot_id = self.get_parking_lot_id()
        for i in range(1,self.floors+1):
            for j in range(1, self.slots_per_floor+1):
                vehicle_type = self.get_vehicle_type(j)
                slot_key = str(i) + "_" + str(j)
                ticket_id = self.get_ticket_id_for_slot(slot_key)
                parking_slot = ParkingSlot(slot_no=j,
                                           floor_no= i,
                                           vehicle_type= vehicle_type,
                                           is_occupied= False,
                                           ticket_id= ticket_id,
                                           parking_lot_id= parking_lot_id)
                
                self.slots[slot_key]= parking_slot
                if vehicle_type not in self.current_avaiable_slots:
                    self.current_avaiable_slots[vehicle_type] = slot_key
                
    def get_vehicle_type(self, slot_no):

        if slot_no == 1:
            return "TRUCK"
        elif slot_no == 2 or slot_no == 3:
            return "BIKE"
        else:
            return "CAR"
    
    def create_slot_key(self, floor_no, slot_no):
        return str(floor_no)+"_"+str(slot_no)

    def get_next_slot_for_vehicle(self, vehicle_type):
        
        if vehicle_type == "TRUCK":
            slot_min = 1
            slot_max = 1
        elif vehicle_type == "BIKE":
            slot_min = 2
            slot_max = 3
        else:
            slot_min = 4
            slot_max = self.slots_per_floor
        
        for i in range(1, self.floors+1):
            for j in range(slot_min, slot_max+1):
                slot_key = self.create_slot_key(i, j)
                parking_slot = self.slots[slot_key]
                occupy_status = parking_slot.get_occupy_status()
                if not occupy_status:
                    ticket_id = parking_slot.get_ticket_id()
                    self.set_ticket_id_for_slot_key(slot_key,
                                                    ticket_id)
                    return parking_slot
        return "NO"

    def get_parking_slot(self, slot_key):
        return self.slots[slot_key]

    def find_parking_slot_for_vehicle(self, vehicle_type):
        parking_lot = self.get_next_slot_for_vehicle(vehicle_type)
        return parking_lot
    
    def set_ticket_id_for_slot_key(self,slot_key, ticket_id):
        self.ticket_id_to_slot_key[ticket_id] = slot_key
    
    def get_parking_slot_from_ticket_id(self, ticket_id):

        slot_key = self.ticket_id_to_slot_key[ticket_id]
        parking_slot = self.slots[slot_key]
        return parking_slot
    
    def get_count_for_vehicle(self, vehicle_type):
        floor_slot_details = {}
        if vehicle_type == "TRUCK":
            slot_min = 1
            slot_max = 1
        elif vehicle_type == "BIKE":
            slot_min = 2
            slot_max = 3
        else:
            slot_min = 4
            slot_max = self.slots_per_floor
        
        for i in range(1, self.floors+1):
            for j in range(slot_min, slot_max+1):
                slot_key = self.create_slot_key(i, j)
                parking_slot = self.slots[slot_key]
                occupy_status = parking_slot.get_occupy_status()
                slot_key = self.create_slot_key(i, j)
                if occupy_status:
                    floor_slot_details[slot_key] = 1
                else:
                    floor_slot_details[slot_key] = 0
        
        return floor_slot_details
    
    def get_free_count_for_vehicle(self, vehicle_type):
        floor_slot_details = self.get_count_for_vehicle(vehicle_type)
        per_floor_count = defaultdict(int)
        for slot_key, occupied_status in floor_slot_details.items():
            floor = int(slot_key.split("_")[0])
            if floor not in per_floor_count:
                per_floor_count[floor] = 0
            if not occupied_status:
                per_floor_count[floor] += 1
        
        return per_floor_count
    
    def get_occupied_slots_for_vehicle(self, vehicle_type):
        floor_slot_details = self.get_count_for_vehicle(vehicle_type)
        per_floor_occupied_slots = defaultdict(list)
        for slot_key, occupied_status in floor_slot_details.items():
            floor = int(slot_key.split("_")[0])
            slot_no = int(slot_key.split("_")[1])

            if floor not in per_floor_occupied_slots:
                    per_floor_occupied_slots[floor] = []
            if occupied_status:
                per_floor_occupied_slots[floor].append(slot_no)
        
        return per_floor_occupied_slots

    def get_free_slots_for_vehicle(self, vehicle_type):
        floor_slot_details = self.get_count_for_vehicle(vehicle_type)
        per_floor_free_slots = defaultdict(list)
        for slot_key, occupied_status in floor_slot_details.items():
            floor = int(slot_key.split("_")[0])
            slot_no = int(slot_key.split("_")[1])

            if floor not in per_floor_free_slots:
                    per_floor_free_slots[floor] = []
            if not occupied_status:
                per_floor_free_slots[floor].append(slot_no)
        return per_floor_free_slots

    def get_max_floors(self):
        return self.floors
    
    def get_max_slots(self):
        return self.slots_per_floor
    

    
    




    