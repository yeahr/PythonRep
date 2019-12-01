
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

b = signal.firwin(30,0.2)
w,h = signal.freqz(b)
alpha = 0.2
w1,h1 = signal.freqz([alpha],[1,alpha-1])

plt.figure(figsize=(4,3))
plt.subplot(2,1,1)
plt.plot(w/2/np.pi,20*np.log10(np.abs(h)),label='fir')
plt.plot(w1/2/np.pi,20*np.log10(np.abs(h1)),label='iir',color='g', linestyle='--')
plt.grid('on')
plt.xlim(0,0.5)
plt.legend()


plt.subplot(2,1,2)
plt.plot(w/2/np.pi,20*np.log10(np.abs(h)),label='fir')
plt.plot(w1/2/np.pi,20*np.log10(np.abs(h1)),label='iir',color='g', linestyle='--')
plt.grid('on')
plt.xlim(0,0.5)
plt.xlabel('pi')
plt.ylabel('幅度')
plt.title('filter amplite')
plt.legend()
plt.show()
