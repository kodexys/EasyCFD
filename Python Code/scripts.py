def makeScripts(pathName, fileName, flow, cores, theta, bound, lst_of_group_names, lst_of_group_names_ext):
    import os, shutil    

    os.chdir(str(pathName) + '/test_clean')

    out_name = str(pathName) + "/test_clean/" + "just_prep"
    out = open(out_name,"w")
    out.write("cd ..\n")
    out.write("cp -r test_clean test_ran\n")

    if (theta != str(0)) and (bound == 1):
        out.write("cd test_ran/constant/triSurface\n")
        for i in lst_of_group_names_ext:
            out.write("surfaceTransformPoints -yawPitchRoll '(" + str(theta) + " 0 0)' " + i + ".stl " + i + ".stl\n")
        out.write("cd ..\n")
        out.write("cd ..\n")
    else:
        out.write("cd test_ran\n")
    out.write("surfaceFeatureExtract.exe > log.SurfaceFeatureExtract\n")
    out.write("blockMesh.exe > log.BlockMesh\n")
    out.write("echo Enter parafoam and load the blockMesh and STL files in the trisurface folder. Use the sphere source to find a suitable locationInMesh\n")
    out.write("echo Then, go into test_ran snappyHexMeshDict and make the necessary change\n")
    out.write("echo Finally, open test_ran in blueCape and enter ./snap_solve\n")
    out.close

    out_name = str(pathName) + "/test_clean/" + "snap_solve"
    out = open(out_name, "w")
    out.write("decomposePar.exe > log.Decompose\n")
    out.write("mpirun -np " + str(cores) + " snappyHexMesh -overwrite -parallel > log.Snappy\n")
    out.write("reconstructParMesh -constant\n")
    out.write("rm -r *processor*\n")
    out.write("transformPoints.exe  -scale '(0.001 0.001 0.001)' >log.transformPoints\n")
    if (theta != str(0)) and (bound == 0):
        out.write("transformPoints -yawPitchRoll '(" + str(theta) + " 0 0)'\n")
    out.write("decomposePar.exe > log.Decompose\n")    
    out.write("mpirun -n " + str(cores) + " renumberMesh -overwrite -parallel\n")

    if flow == 2:
        out.write("mpirun -np " + str(cores) + " interFoam -parallel  | tee log\n")
        out.write("reconstructPar\n")
        out.write("rm -r *processor*\n")
        
    else:
        out.write("mpirun -np " + str(cores) + " simpleFoam -parallel  | tee log\n")
        out.write("reconstructPar -latestTime\n")
        out.write("rm -r *processor*\n")
    out.close