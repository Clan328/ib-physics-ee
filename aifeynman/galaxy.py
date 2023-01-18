class Galaxy:
    def __init__(self, M, SM, SFR):
        self.M = M
        self.SM = SM
        self.SFR = SFR
        
    def __repr__(self):
        return f"<Galaxy M:{self.M} SM:{self.SM} SFR:{self.SFR}>"