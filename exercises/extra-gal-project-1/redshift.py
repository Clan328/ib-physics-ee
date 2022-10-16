import h5py
import numpy as np
from tqdm.notebook import trange, tqdm

from galaxy import Galaxy

class Redshift:
    def __init__(self, path, load=True):
        self.h = h5py.File(path, 'r')
        
        self.Box = int(self.h.attrs["Box"])
        self.Ngalaxies = int(self.h.attrs["Ngalaxies"])
        self.Redshift = self.h.attrs["Redshift"]
        
        if load:
            self.load_galaxies()
    
    def load_galaxies(self):
        self.x = np.real(self.h.get('x'))
        self.y = np.real(self.h.get('y'))
        self.z = np.real(self.h.get('z'))
        self.M = np.real(self.h.get('Mvir'))
        self.SM = np.real(self.h.get('StellarMass'))
        self.SFR = np.real(self.h.get('StarFormationRate'))
        self.ID = np.int_(self.h.get('CentralObject'))
        
        self.galaxies = []

        for i in trange(self.Ngalaxies):
            g = Galaxy(self.x[i], self.y[i], self.z[i],
                       self.M[i], self.SM[i], self.SFR[i], self.ID[i])
            self.galaxies.append(g)
        
    def __repr__(self):
        return f"<Redshift Box:{self.Box} Ngalaxies:{self.Ngalaxies} Redshift:{self.Redshift}>"