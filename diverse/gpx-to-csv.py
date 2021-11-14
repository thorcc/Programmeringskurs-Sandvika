# Program som konverterer gpx-filer til csv-filer
# Programmet krever pakken gpx_converter 
# Åpne terminalen/CMD og kjør kommandoen: pip install -U gpx-converter

from gpx_converter import Converter
from datetime import datetime

input = "kolsaastoppen_med_Eirik.gpx"
output = "kolsaastoppen_med_Eirik.csv"

Converter(input_file=input).gpx_to_csv(output_file=output)

# Resten av koden konverterer fra datetime til sekunder
f = open(output,"r")
lines = f.readlines()

starttime = datetime.strptime(lines[1].split(",")[0][:19], "%Y-%m-%d %H:%M:%S")
f = open(output, "w")
f.write(lines[0])
for line in lines[1::]:
    newline = line.split(",")
    newtime = datetime.strptime(newline[0][:19], "%Y-%m-%d %H:%M:%S")
    newline[0] = str(int((newtime - starttime).total_seconds()))
    f.write(",".join(newline))
