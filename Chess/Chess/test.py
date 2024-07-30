class Stone:
    def __init__(self, belongs_to, current_location):
        self.belongs_to = belongs_to
        self.available_locations = []
        self.current_location = current_location    
        print("Stone")

class Pawn(Stone):
    def __init__(self,belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        
        self.name = "Pawn"
        print(self.name)

a = Pawn("hasan",(2,2))