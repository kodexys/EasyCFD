#This master file executes all scripts and functions necessary to build an OpenFOAM case

from su2ToSTL import convertFile
from make0 import makeZero
from makeConstant import make_constant
from makeSystem import make_system
from scripts import makeScripts

def execute(pathName, fileName, dim, flow, inletU, bound, cores, theta, turbulence):
    x_min, x_max, y_min, y_max, z_min, z_max, lst_of_group_names, lst_of_group_names_ext = convertFile(pathName, fileName)
    makeZero(pathName, lst_of_group_names, dim, flow, inletU, bound, turbulence)
    make_constant(pathName, flow, x_min, x_max, y_min, y_max, z_min, z_max, bound, turbulence)
    make_system(pathName, lst_of_group_names, lst_of_group_names_ext, flow, cores, bound)
    makeScripts(pathName, fileName, flow, cores, theta, bound, lst_of_group_names, lst_of_group_names_ext)

if __name__ == "__main__":
    fileName = "Damper.su2"
    dim = int(input("Enter 0 if U unit is m/s, 1 if U unit is m3/s: "))
    flow = int(input("Enter 0 if air, 1 if water, 2 if air/water mix: "))
    inletU = float(input("Enter flow rate value: "))
    bound = int(input("Enter 0 if bounds are triSurface, 1 if bounds are blockMesh: "))
    cores = int(input("Enter the number of processor cores you wish to use for simulation (1 or more): "))
    execute(pathName, fileName, dim, flow, inletU, bound, cores)
