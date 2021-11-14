import matplotlib.pyplot as plt

f = open('datasett/kolsaastoppen_med_Eirik.csv', 'r')
lines = f.readlines()[1:] # må droppe den første linjen
t = [float(line.split(",")[0]) for line in lines]
x = [float(line.split(",")[1]) for line in lines] 
y = [float(line.split(",")[2]) for line in lines]
h = [float(line.split(",")[3]) for line in lines]

fig, axs = plt.subplots(2)
fig.suptitle('Kolsåstoppen med Eirik')

axs[0].plot(x, y)
axs[0].set_title("Koordinater")

axs[1].plot(t, h)
axs[1].set_title("Høyde")
axs[1].set(xlabel="Tid (s)", ylabel="Høyde (moh)")

plt.show()
