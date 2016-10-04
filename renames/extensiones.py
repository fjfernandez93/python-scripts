import os
import glob

def changeExtension(oldE, newE, mypath):
    print "######"
    newE = "." + newE
    oldE = "." + oldE
    pattern = "*"+oldE
    matches = os.path.join(mypath, pattern)
    for dire in glob.glob(matches):
        old = os.path.join(mypath,dire)
        nuevo = os.path.join(mypath,os.path.splitext(dire)[0] + newE)
        os.rename(old, nuevo)
        print os.path.split(dire)[1] + " --> " + os.path.split(nuevo)[1]



if __name__ == '__main__':


    ruta = "/Users/paco/Documents/Proyectos/Python/renames/pruebas"
    vieja = raw_input("antigua extension: ")
    nueva = raw_input("nueva extension: ")
    changeExtension(vieja, nueva, ruta)
    print "####### Hecho ########"
