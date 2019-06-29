import numpy as np
import matplotlib.pyplot as plt
a = b = np.arange(0,3,.02)
c = np.exp(a)
d = c[::-1]
plt.plot(a,c,'k--',label = 'Model length')
plt.plot(a,d,'k:', label = 'Data length')
plt.plot(a,c+d,'k',label = 'Total message length')

legend = plt.legend(loc = 'upper center', shadow = True, fontsize = 'x-large')
legend.get_frame().set_facecolor('#dddddd')
plt.show()
