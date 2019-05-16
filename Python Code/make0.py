def makeZero(pathName, lst_of_group_names, dim, flow, inletU, bound, turbulence):
    #create 0 folder
    import os
    os.chdir(str(pathName) + '/test_clean/')
    if not os.path.exists('0'):
        os.mkdir('0')
    ########################################################################
    #U file
    ########################################################################
    if bound == 1:
        lst_of_group_names.append('inlet')
        lst_of_group_names.append('outlet')
        lst_of_group_names.append('frontAndBack')
        lst_of_group_names.append('lowerWall')
        lst_of_group_names.append('upperWall')
    #write to file
    out_name = str(pathName) + "/test_clean/0/" + "U"
    out = open(out_name,"w")

    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   binary;\n    class    volVectorField;\n    object   U;\n}\n")
    out.write("\n")

    out.write("dimensions   [0 1 -1 0 0 0 0];\n")
    out.write("internalField    uniform     (0.0 0.0 0.0);\n")
    out.write("\n")
    out.write("boundaryField\n")
    out.write("{\n")
    out.write("\n")
    out.write("     boundaries\n")
    out.write("     {\n")
    out.write("     type zeroGradient;\n")
    out.write("     }\n")
    out.write("\n")
    for i in lst_of_group_names:
        if ("inlet" in i) and (dim == 0):
            out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform (" + str(inletU) + " 0.0 0.0);\n     }\n")
        elif ("inlet" in i) and (dim == 1):
            out.write("     " + i + "\n     {\n     type flowRateInletVelocity;\n     volumetricFlowRate constant " + str(inletU) + ";\n     value uniform (0.0 0.0 0.0);\n     }\n")
        elif "outlet" in i:
            out.write("     " + i + "\n     {\n     type zeroGradient;\n     }\n")
        elif ("outlet" not in i) and ("inlet" not in i):
            out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform (0.0 0.0 0.0);\n     }\n")
    out.write("}")
    out.close
    ######################################################################################
    #P or p_rgh file
    ######################################################################################
    #from su2ToSTL import lst_of_group_names
    #write to file
    if flow != 2:
        out_name = str(pathName) + "/test_clean/0/" + "P"
        out = open(out_name,"w")

        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   binary;\n    class    volScalarField;\n    object   p;\n}\n")
        out.write("\n")
        out.write("dimensions   [0 2 -2 0 0 0 0];\n")
        out.write("internalField    uniform     0.0;\n")
        out.write("\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            if "outlet" not in i:
                out.write("     " + i + "\n     {\n     type zeroGradient;\n     }\n\n")
            else:
                out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform 0.0;\n     }\n\n")
        out.write("}")
    elif flow == 2:
        out_name = str(pathName) + "/test_clean/0/" + "p_rgh"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   binary;\n    class    volScalarField;\n    object   p_rgh;\n}\n")
        out.write("\n")
        out.write("dimensions   [1 -1 -2 0 0 0 0];\n")
        out.write("internalField    uniform     0.0;\n")
        out.write("\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            #if i != "outlet" and i != "inlet":
            if ("outlet" not in i) and ("inlet" not in i):
                out.write("     " + i + "\n     {\n     type fixedFluxPressure;\n     }\n\n")
            #elif i == "outlet":
            elif "outlet" in i:
                out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform 0.0;\n     }\n\n")
            #elif i == "inlet":
            elif "inlet" in i:
                out.write("     " + i + "\n     {\n     type zeroGradient;\n     }\n\n")
        out.write("}")
    out.close
    #######################################################################################
    #alpha.water
    #######################################################################################
    if flow == 2:
        out_name = str(pathName) + "/test_clean/0/" + "alpha.water"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   binary;\n    class    volScalarField;\n    object   alpha.water;\n}\n")
        out.write("\n")
        out.write("dimensions   [0 0 0 0 0 0 0];\n")
        out.write("\n")
        init_flow = int(input("Enter 0 if internal field begins as air, 1 if water: "))
        inlet_flow = int(input("Enter 0 if inlet flow is air, 1 if water: "))
        out.write("internalField    uniform     " + str(init_flow) + ";\n")
        out.write("\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            #if i != "outlet" and i != "inlet":
            if ("outlet" not in i) and ("inlet" not in i):
                out.write("     " + i + "\n     {\n     type constantAlphaContactAngle;\n     theta0          45.1235;\n     limit           gradient;\n     value uniform " + str(init_flow) + ";\n     }\n\n")
            #elif i == "outlet":
            elif "outlet" in i:
                out.write("     " + i + "\n     {\n     type inletOutlet;\n     inletValue      uniform " + str(init_flow) + ";\n     value        uniform " + str(init_flow) + ";\n     }\n\n")
            #elif i == "inlet":
            elif "inlet" in i:
                out.write("     " + i + "\n     {\n     type inletOutlet;\n     inletValue      uniform " + str(inlet_flow) + ";\n     value        uniform " + str(inlet_flow) + ";\n     }\n\n")
        out.write("}")
#######################################################################################
#k
#######################################################################################
    if turbulence == 1:
        out_name = str(pathName) + "/test_clean/0/" + "k"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    volScalarField;\n    object   k;\n}\n")
        out.write("\n")
        out.write("dimensions       [0 2 -2 0 0 0 0];\n")
        out.write("\n")
        out.write("internalField    uniform K_VALUE;\n")
        out.write("//       K_VALUE = 1.5*(inletVelocity*turbulentIntensity)^2\n")
        out.write("// Low turbulence case (e.g. external flow across cars/submarines/aircrafts)\n")
        out.write("//       0 < turbulentIntensity < 0.01\n")
        out.write("// Medium turbulence case (e.g. internal flow in simple geometries like pipes or low speed flows)\n")
        out.write("//       0.01 < turbulentIntensity < 0.05\n")
        out.write("// High turbulence case (e.g. high speed internal flow in complex geometries like heat exchangers/compressors/turbines)\n")
        out.write("//       0.05 < turbulentIntensity < 0.20\n")
        out.write("\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            if ("outlet" not in i) and ("inlet" not in i):
                out.write("     " + i + "\n     {\n     type kqRWallFunction;\n     value uniform K_VALUE;\n     }\n\n")
            elif "inlet" in i:
                out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform K_VALUE;\n     }\n\n")
            elif "outlet" in i:
                out.write("     " + i + "\n     {\n     type zeroGradient;\n     }\n\n")
        out.write("}")
        out.close
#######################################################################################
#epsilon
#######################################################################################
        out_name = str(pathName) + "/test_clean/0/" + "epsilon"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    volScalarField;\n    object   epsilon;\n}\n")
        out.write("\n")
        out.write("dimensions       [0 2 -3 0 0 0 0];\n")
        out.write("\n")
        out.write("internalField    uniform EPSILON_VALUE;\n")
        out.write("//       EPSILON_VALUE = (0.09^0.75)*((k^1.5)/(0.07*characteristicInletScale))\n")
        out.write("\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            if ("outlet" not in i) and ("inlet" not in i):
                out.write("     " + i + "\n     {\n     type epsilonWallFunction;\n     value uniform EPSILON_VALUE;\n     }\n\n")
            elif "inlet" in i:
                out.write("     " + i + "\n     {\n     type fixedValue;\n     value uniform EPSILON_VALUE;\n     }\n\n")
            elif "outlet" in i:
                out.write("     " + i + "\n     {\n     type zeroGradient;\n     }\n\n")
        out.write("}")
        out.close
#######################################################################################
#nut
#######################################################################################
        out_name = str(pathName) + "/test_clean/0/" + "nut"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    volScalarField;\n    object   nut;\n}\n")
        out.write("\n")
        out.write("dimensions       [0 2 -1 0 0 0 0];\n")
        out.write("\n")
        out.write("internalField    uniform 0;\n")
        out.write("boundaryField\n")
        out.write("{\n")
        out.write("\n")
        out.write("     boundaries\n")
        out.write("     {\n")
        out.write("     type zeroGradient;\n")
        out.write("     }\n")
        out.write("\n")
        for i in lst_of_group_names:
            if ("outlet" not in i) and ("inlet" not in i):
                out.write("     " + i + "\n     {\n     type nutkWallFunction;\n     value uniform 0;\n     }\n\n")
            elif "inlet" in i:
                out.write("     " + i + "\n     {\n     type calculated;\n     value uniform 0;\n     }\n\n")
            elif "outlet" in i:
                out.write("     " + i + "\n     {\n     type calculated;\n     value uniform 0;\n     }\n\n")
        out.write("}")
        out.close