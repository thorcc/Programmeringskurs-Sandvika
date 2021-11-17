#import matplotlib.pyplot as plt
from pylab import *

fil = open('datasett/kolsaastoppen_med_Eirik.csv')
linjer = fil.readlines() # lager en liste med linjene i fil

t = []
x = []
y = []
h = []

for linje in linjer[1:]: #[1:] dropper den første linjen i filen
    oppdelt_linje = linje.split(",")
    t.append(float(oppdelt_linje[0]))
    x.append(float(oppdelt_linje[1]))
    y.append(float(oppdelt_linje[2]))
    h.append(float(oppdelt_linje[3]))

title('Kolsåstoppen med Eirik')
plot(x, y)
show()
