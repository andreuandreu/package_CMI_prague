import pandas as pd
import matplotlib.pyplot as plt
import read_surrogate_data as rsd
import numpy as np

name = '../data/exp_raw/binfiles/Rossler_bin_0.000.bin'


plt.rcParams['figure.figsize'] = [12, 9]
#df = pd.read_csv('EURUSD.csv',sep='\t', index_col='Date')
df = rsd.read_bin_bin_dataframe(name)
df.sort_index(inplace=True)
#df = df.resample('W').last()
series = df['x']


fig, ax = plt.subplots(3,1)
# assigning time values of the signal
# initial time period, final time period and phase angle
signalTime = np.arange(1, 100, 0.5);
  
# getting the amplitude of the signal
signalAmplitude = np.sin(signalTime)
  
# plotting the signal 
ax[0].plot(signalTime, signalAmplitude, color ='green')
  
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_title("Signal")
  
  
# plotting the phase spectrum of the signal 
ax[1].phase_spectrum(signalAmplitude, color ='green')
  
ax[1].set_title("Phase Spectrum of the Signal")
plt.show()
