class Galaxy:
    def __init__(self, x, y, z, M, SM, SFR, ID):
        self.x = x
        self.y = y
        self.z = z
        self.M = M
        self.SM = SM
        self.SFR = SFR
        self.ID = ID
        
    def __repr__(self):
        return f"<Galaxy x:{self.x} y:{self.y} z:{self.x} M:{self.M} SM:{self.SM} SFR:{self.SFR} ID:{self.ID}>"