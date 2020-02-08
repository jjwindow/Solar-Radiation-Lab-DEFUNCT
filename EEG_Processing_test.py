"""
J. J. Window
08/02/2020

Attempt at implementing feature extraction and processing techniques for EEG signal.

TO DO
- Implement feature interrogation methods

"""

import csv
import matplotlib.pyplot as plt
import scipy as sp

class EpochObj:
    """
    An object to store an excerpt time-series EEG data.
    """
    def __init__(self, epochNum):
        """
        Initialise empty epoch instance.
        """
        self.t = []
        self.eeg = []
        self.epochNum = epochNum

    def insert(self, _t, _eeg):
        """
        Add time series measurement to epoch class.
        """
        self.t.append(_t)
        self.eeg.append(_eeg)

    def t_return(self):
        """
        Returns array of measurement times.
        """
        return self.t
    
    def eeg_return(self):
        """
        Returns array of EEG signal measurements in mV.
        """
        return self.eeg

    def plotEpoch(self):
        """
        Show a plot of the time series data.
        """
        fig = plt.plot(self.t, self.eeg)
        fig.show()
        return fig
    
    def epochNum_return(self):
        """
        Returns the epoch index.
        """
        return self.epochNum

def assembleData(filename = 'testdata.csv'): 
    """
    Function to read data from a pre-organised CSV into a list of epoch objects, each containing
    all time-series measurements in that epoch. CSV is assumed to be of the format ->

    TIME    |   EPOCH   |   SIGNAL mV       <- Headers here given as indication. CSV must have NO HEADERS
    ----------------------------------         to process the data properly, unless header removal implemented.
        T1  |     0     |      32       
         .  |     .     |       .
         .  |     .     |       .
         .  |     .     |       .
        TN  |     N_e   |       XN           <- For N data points (N_e is number of epochs)
    ----------------------------------


    """      
    with open(filename) as eeg:
        readEEG = csv.reader(eeg, delimiter=',')
        epochNums = set([row[1] for row in readEEG])
        epochsList = []

        for row in readEEG:
            # Populate column arrays with data from CSV
            _t = row[0]
            _epoch = row[1]
            _eeg = row[2]
            t.append(_t)
            epoch.append(_epoch)
            eeg.append(_eeg)

        for n in epochNums:
            # Instantiate each epoch
            NewEpoch = EpochObj(n)
            # Point in array where epoch first equals n
            # Assumes t, eeg, and epoch are all ordered in ascending time (hence epoch)
            # and that indices align (i.e - dataset is complete.)
            e = epoch.index[n]
            # Loop through all datapoints for epoch n
            while epoch[e] == n:
                # Populate epoch object with data.
                NewEpoch.insert(t[e], eeg[e])
                e += 1
            epochsList.append(NewEpoch)
    return epochsList
            

        