from datetime import datetime as d

with open("output.txt", "a") as outfile :
    outfile.write(str(d.now()) + "\n")
