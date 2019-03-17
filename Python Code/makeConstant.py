def make_constant(pathName, flow, x_min, x_max, y_min, y_max, z_min, z_max, bound, turbulence):
    #create constant folder
    import os
    os.chdir(str(pathName) + '/test_clean/')
    if not os.path.exists('constant'):
        os.mkdir('constant')

    #################################################
    #g file
    #################################################
    out_name = str(pathName) + "/test_clean/constant/" + "g"
    out = open(out_name,"w")
    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   g;\n}\n")
    out.write("\n")

    out.write("dimensions   [0 1 -2 0 0 0 0];\n")
    out.write("value        (0.0 -9.81 0.0);\n")
    out.close
    ###################################################
    #turbulence properties
    ###################################################
    out_name = str(pathName) + "/test_clean/constant/" + "turbulenceProperties"
    out = open(out_name,"w")
    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   turbulenceProperties;\n}\n")
    out.write("\n")
    if turbulence == 0:
        out.write("simulationType laminar;\n")
    else:
        out.write("simulationType RAS;\n")
        out.write("{\n")
        out.write("     RASModel        kEpsilon;\n")
        out.write("     turbulence      on;\n")
        out.write("     printCoeffs     on;\n")
        out.write("}")
    out.close
    #####################################################
    #transportProperties
    #####################################################
    out_name = str(pathName) + "/test_clean/constant/" + "transportProperties"
    out = open(out_name,"w")
    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   transportProperties;\n}\n")
    out.write("\n")
    if flow == 0:
        out.write("nu nu [0 2 -1 0 0 0 0] 14.8E-6;\n")
    elif flow == 1:
        out.write("nu nu [0 2 -1 0 0 0 0] 1E-6;\n")
    elif flow == 2:
        out.write("phases (water air);\n")
        out.write("\n")
        out.write("water\n")
        out.write("{\n")
        out.write("     transportModel Newtonian;\n")
        out.write("     nu             [0 2 -1 0 0 0 0] 1e-06;\n")
        out.write("     rho            [1 -3 0 0 0 0 0] 1000;\n")
        out.write("}\n")
        out.write("\n")
        out.write("air\n")
        out.write("{\n")
        out.write("     transportModel Newtonian;\n")
        out.write("     nu             [0 2 -1 0 0 0 0] 1.48e-05;\n")
        out.write("     rho            [1 -3 0 0 0 0 0] 1;\n")
        out.write("}\n")
        out.write("\n")
        out.write("sigma               [1 0 -2 0 0 0 0] 0.0707106;")
    out.write("transportModel Newtonian;")
    out.close
    ################################################################################################
    #polyMesh
    ###############################################################################################
    os.chdir(str(pathName) + '/test_clean/constant/')
    if not os.path.exists('polyMesh'):
        os.mkdir('polyMesh')

    #from makeBlockMeshDict
    #make bounding box slightly larger than stl
    if bound == 0:
        if x_min > 0:
            x_min = x_min - (x_min/100)
        else:
            x_min = x_min + (x_min/100)

        if y_min > 0:
            y_min = y_min - (y_min/100)
        else:
            y_min = y_min + (y_min/100)

        if z_min > 0:
            z_min = z_min - (z_min/100)
        else:
            z_min = z_min + (z_min/100)

        if x_max > 0:
            x_max = x_max + (x_max/100)
        else:
            x_max = x_max - (x_max/100)

        if y_max > 0:
            y_max = y_max + (y_max/100)
        else:
            y_max = y_max - (y_max/100)

        if z_max > 0:
            z_max = z_max + (z_max/100)
        else:
            z_max = z_max - (z_max/100)
    elif bound == 1:
        if x_min > 0:
            x_min = x_min - (x_min*10)
        else:
            x_min = x_min + (x_min*10)

        if y_min > 0:
            y_min = y_min - (y_min*10)
        else:
            y_min = y_min + (y_min*10)

        if z_min > 0:
            z_min = z_min - (z_min*10)
        else:
            z_min = z_min + (z_min*10)

        if x_max > 0:
            x_max = x_max + (x_max*10)
        else:
            x_max = x_max - (x_max*10)

        if y_max > 0:
            y_max = y_max + (y_max*10)
        else:
            y_max = y_max - (y_max*10)

        if z_max > 0:
            z_max = z_max + (z_max*10)
        else:
            z_max = z_max - (z_max*10)

    vol = float((x_max - x_min) * (y_max - y_min) * (z_max - z_min))
    if bound == 0:
        n_cells = 200000
    elif bound == 1:
        n_cells = 500000
    cell_length = (vol/n_cells) ** (1/3)
    n_xcells = int((x_max - x_min)/cell_length)
    n_ycells = int((y_max - y_min)/cell_length)
    n_zcells = int((z_max - z_min)/cell_length)

    #write to file
    out_name = str(pathName) + "/test_clean/constant/polyMesh/" + "blockMeshDict"
    out = open(out_name,"w")

    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   blockMeshDict;\n}\n")

    out.write("\n")
    out.write("convertToMeters 1;\n")
    out.write("\n")

    out.write("edges\n(\n);\n")
    out.write("\n")

    out.write("// xmin=" + str(x_min) + " ymin=" + str(y_min) + " zmin=" + str(z_min) + "\n")
    out.write("// xmax=" + str(x_max) + " ymax=" + str(y_max) + " zmax=" + str(z_max) + "\n")
    out.write("\n")

    out.write("vertices\n")
    out.write("(\n")
    out.write("    (" + str(x_min) + " " + str(y_min) + " " + str(z_min) + ")\n")
    out.write("    (" + str(x_max) + " " + str(y_min) + " " + str(z_min) + ")\n")
    out.write("    (" + str(x_max) + " " + str(y_max) + " " + str(z_min) + ")\n")
    out.write("    (" + str(x_min) + " " + str(y_max) + " " + str(z_min) + ")\n")
    out.write("    (" + str(x_min) + " " + str(y_min) + " " + str(z_max) + ")\n")
    out.write("    (" + str(x_max) + " " + str(y_min) + " " + str(z_max) + ")\n")
    out.write("    (" + str(x_max) + " " + str(y_max) + " " + str(z_max) + ")\n")
    out.write("    (" + str(x_min) + " " + str(y_max) + " " + str(z_max) + ")\n")
    out.write(");\n")
    out.write("\n")


    out.write("boundary\n")
    out.write("(\n")
    if bound == 0:
        out.write("    boundaries\n")
        out.write("    {\n")
        out.write("         type patch;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (0 4 7 3)\n")
        out.write("             (2 6 5 1)\n")
        out.write("             (1 5 4 0)\n")
        out.write("             (3 7 6 2)\n")
        out.write("             (0 3 2 1)\n")
        out.write("             (4 5 6 7)\n")
        out.write("         );\n")
        out.write("    }\n")
    elif bound == 1:
        out.write("    frontAndBack\n")
        out.write("     {\n")
        out.write("         type patch;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (0 3 2 1)\n")
        out.write("             (4 5 6 7)\n")
        out.write("         );\n")
        out.write("     }\n")
        out.write("\n")
        out.write("    inlet\n")
        out.write("     {\n")
        out.write("         type wall;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (0 4 7 3)\n")
        out.write("         );\n")
        out.write("     }\n")
        out.write("\n")
        out.write("    outlet\n")
        out.write("     {\n")
        out.write("         type wall;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (2 6 5 1)\n")
        out.write("         );\n")
        out.write("     }\n")
        out.write("\n")
        out.write("    lowerWall\n")
        out.write("     {\n")
        out.write("         type wall;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (3 7 6 2)\n")
        out.write("         );\n")
        out.write("     }\n")
        out.write("\n")
        out.write("    upperWall\n")
        out.write("     {\n")
        out.write("         type wall;\n")
        out.write("         faces\n")
        out.write("         (\n")
        out.write("             (1 5 4 0)\n")
        out.write("         );\n")
        out.write("     }\n")
        out.write("\n")
    out.write(");\n")

    out.write("\n")

    out.write("blocks\n")
    out.write("(\n")
    #make product of xyz cells between 50000 and 2 million?
    out.write("hex (0 1 2 3 4 5 6 7) (" + str(n_xcells) + " " + str(n_ycells) + " " + str(n_zcells) +") simpleGrading (1 1 1)\n")
    out.write(");\n")
    out.close

    if not os.path.exists('extendedFeatureEdgeMesh'):
        os.mkdir('extendedFeatureEdgeMesh')
