from tickets import *

class ParkingSlot:

    def __init__(self, 
                 slot_no, 
                 floor_no, 
                 vehicle_type, 
                 is_occupied, 
                 parking_lot_id,
                 ticket_id
                 ):
        self.slot_no = slot_no
        self.floor_no = floor_no,
        self.vehicle_type = vehicle_type
        self.is_occupied = is_occupied
        self.parking_lot_id = parking_lot_id
        self.registration = ''
        self.color = ''
        self.ticket_id = ticket_id
    

    def park_vehicle(self, registration, color):
        # Input
        # park_vehicle CAR KA-01-DB-1234 black
        # Ouput
        # Parked vehicle. Ticket ID: PR1234_1_4
        self.set_occupy_status()
        self.set_registration(registration)
        self.set_color(color)
        ticket_id = self.get_ticket_id()
        return ticket_id
    
    def unpark_vehicle(self):
        result = {'color' : '', 
                  'registration' : ''
                  }
        color = self.get_color()
        registration = self.get_registration()
        result['color'] = color
        result['registration'] = registration
        self.unset_occupy_status()
        self.unset_color()
        self.unset_registration()
        return result

    def set_occupy_status(self):
        self.is_occupied = True
    
    def unset_occupy_status(self):
        self.is_occupied = False
    
    def get_occupy_status(self):
        return self.is_occupied

    def set_registration(self, registration):
        self.registration = registration
    
    def get_registration(self):
        return self.registration
    
    def unset_registration(self):
        self.registration = ''
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def unset_color(self):
        self.color = ''

    def get_registration(self):
        return self.registration
    
    def get_floor_no(self):
        return self.floor_no
    
    def get_slot_no(self):
        return self.slot_no

    def get_parking_lot_id(self):
        return self.parking_lot_id
    
    def get_ticket_id(self):
        return self.ticket_id
    



