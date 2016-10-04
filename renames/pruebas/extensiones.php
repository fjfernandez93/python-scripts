import os

mypath = "/Users/paco/Documents/Proyectos/Python/pruebas"


for dire in os.listdir(mypath):
    if dire.endswith(".py"):
        old = os.path.join(mypath,dire)
        nuevo = os.path.splitext(dire)[0] + ".php"
        print nuevo
        #os.rename(old, nuevo)
