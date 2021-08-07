title = 'Myfile.txt'
WriteFile = 'Writefile.out'


file = open(title, 'r') # 'r' is for read file
WriteToFile = open(WriteFile, 'w')
WriteToFile.write("Time [s], Temperature [K]" + "\n")


line = file.readline()


for line in file:
    x = line.split()
    WriteToFile.write(x[0] + "  ,  " + str(float(x[2]) + 273.15) + "\n")

file.close()