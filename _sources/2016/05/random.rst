# Building a simple class to generate random numbers

Random numbers are pretty fascinating.  Where does the randomness come from?  How random is it really?  If its not really random then how can this be exploited?
Testing


.. plot::

   import matplotlib.pyplot as plt
   import numpy as np
   import seaborn as sbn
   sbn.set()
   x = np.random.randn(1000)
   plt.hist( x, 20)
   plt.grid()
   plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
   plt.show()
