
class Ticket:

    def __init__(self, parking_lot_id, floor_no, slot_no):
        self.parking_lot_id = parking_lot_id
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.slot_key = str(self.floor_no)+"_"+str(self.slot_no)
    
    def get_slot_key(self):
        return self.slot_key
    
    def get_ticket_id(self):
        return str(self.parking_lot_id)+"_"+str(self.floor_no)+"_"+str(self.slot_no)
    


    
        