# Lese fra fil

Lesing av filer i Python kan gjøres med den innebygde funksjonen `open("filsti")`.
Mellom parentesene skrives stien til filen som skal leses inn, relativt til python-filen vi skriver i.
Det betyr at hvis vi for eksempel skal lese inn en fil som ligger i samme mappe som python-filen vi skriver i, er filstien kun filnavnet på filen vi skal lese inn, for eksempel slik: `"badetemperaturer.csv"`.
Og hvis filen vi skal lese inn ligger i en *undermappe*, skriver vi navnet på mappen skråstrek navnet på filen, for eksempel slik: `"datasett/kolsaastoppen_med_Eirik.csv"`.

Under er et kodeeksempel på lesing av fil og plotting i Python.

```python
import matplotlib.pyplot as plt # importerer bibliotek for plotting

fil = open("datasett/eksempelfil.txt") # åpner filen eksempelfil.txt, som ligger i mappen datasett, og lagrer filinnholdet i variabelen fil

x = [] # oppretter en tom liste for x-verdiene
y = [] # oppretter en tom liste for y-verdiene

for linje in fil: # går gjennom én og én linje i variabelen fil, og kaller hver linje for linje:
    oppdelt_linje = linje.split(" ") # funksjonen open() leser inn hver linje samlet som en string, må derfor splitte linjen med metoden .split(), mellom parentesene skrives hva linjen skal splittes på. Mellomrom er " ", komma er "," osv.
    x.append(int(oppdelt_linje[0])) # Konverterer elementet på plass 0 i den oppdelte linjen til int (heltall), og legger det til i listen x
    y.append(float(oppdelt_linje[1])) # Konverterer elementet på plass 1 i den oppdelte linjen til float (desimaltall), og legger det til i listen y


plt.title("Eksempelfil") # legger til en tittel på plottet
plt.xlabel("x-verdier") # legger til en tekst på x-aksen
plt.ylabel("y-verdier") # legger til en tekst på y-aksen
plt.plot(x,y) # plotter listene x og y
plt.show() # viser plottet

```