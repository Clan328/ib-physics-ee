import h5py
import numpy as np
from tqdm.notebook import trange, tqdm

from galaxy import Galaxy

class Redshift:
    def __init__(self, path, load=True, Ngalaxies=-1):
        self.h = h5py.File(path, 'r')
        
        self.Box = int(self.h.attrs["Box"])
        if Ngalaxies >= 0:
            self.Ngalaxies = min(int(self.h.attrs["Ngalaxies"]), Ngalaxies)
        else:
            self.Ngalaxies = int(self.h.attrs["Ngalaxies"])
        self.Redshift = self.h.attrs["Redshift"]
        
        self.galaxies = []
        
        if load:
            self.load_galaxies()
    
    def load_galaxies(self):
        M = np.real(self.h.get('Mvir'))
        SM = np.real(self.h.get('StellarMass'))
        SFR = np.real(self.h.get('StarFormationRate'))
        
        self.galaxies = []

        for i in trange(self.Ngalaxies):
            g = Galaxy(M[i], SM[i], SFR[i])
            self.galaxies.append(g)
        
    def __repr__(self):
        return f"<Redshift Box:{self.Box} Ngalaxies:{self.Ngalaxies} Redshift:{self.Redshift}>"