import matplotlib.pyplot as plt # importerer bibliotek for plotting

fil = open("datasett/eksempelfil.txt") # åpner filen eksempelfil.txt, som ligger i mappen datasett, og lagrer filinnholdet i variabelen fil

x = [] # oppretter en tom liste for x-verdiene
y = [] # oppretter en tom liste for y-verdiene

for linje in fil: # går gjennom én og én linje i variabelen fil, og kaller hver linje for linje:
    oppdelt_linje = linje.split(" ") # funksjonen open() leser inn hver linje samlet som en string, må derfor splitte linjen med metoden .split(), mellom parentesene skrives det linjen skal splittes på. Mellomrom er " ", komma er "," osv.
    x.append(int(oppdelt_linje[0])) # Konverterer elementet på plass 0 i den oppdelte linjen til int (heltall), og legger det til i listen x
    y.append(float(oppdelt_linje[1])) # Konverterer elementet på plass 1 i den oppdelte linjen til float (desimaltall), og legger det til i listen y


plt.title("Eksempelfil") # legger til en tittel på plottet
plt.xlabel("x-verdier") # legger til en tekst på x-aksen
plt.ylabel("y-verdier") # legger til en tekst på y-aksen
plt.plot(x,y) # plotter listene x og y
plt.show() # viser plottet