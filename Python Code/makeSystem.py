def make_system(pathName, lst_of_group_names, lst_of_group_names_ext, flow, cores, bound):
    import os
    os.chdir(str(pathName) + '/test_clean/')
    if not os.path.exists('system'):
        os.mkdir('system')
    ############################################################################
    #extendedFeatureEdgeMesh
    ############################################################################
    #write to file
    out_name = str(pathName) + "/test_clean/system/" + "surfaceFeatureExtractDict"
    out = open(out_name,"w")

    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   surfaceFeatureExtractDict;\n}\n")
    out.write("\n")
    if bound == 0:
        for i in lst_of_group_names:
            out.write(i + ".stl " + "{extractionMethod extractFromSurface; extractFromSurfaceCoeffs {includedAngle 150;} writeObj yes;}\n")
    elif bound == 1:
        for i in lst_of_group_names_ext:
            out.write(i + ".stl " + "{extractionMethod extractFromSurface; extractFromSurfaceCoeffs {includedAngle 150;} writeObj yes;}\n")
    out.close
    ###################################################
    #snappyHexMeshDict
    ###################################################
    out_name = str(pathName) + "/test_clean/system/" + "snappyHexMeshDict"
    out = open(out_name,"w")

    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   snappyHexMeshDict;\n}\n")

    out.write("\n")
    out.write("castellatedMesh true;\n")
    out.write("snap            true;\n")
    out.write("addLayers       true;\n")
    out.write("\n")

    out.write("geometry\n")
    out.write("{\n")
    if bound == 0:
        for i in lst_of_group_names:
            out.write(i + ".stl " + "{type triSurfaceMesh; name " + i + ";}\n")
    elif bound == 1:
        for i in lst_of_group_names_ext:
            out.write(i + ".stl " + "{type triSurfaceMesh; name " + i + ";}\n")
    out.write("}\n")

    out.write("\n")
    out.write("castellatedMeshControls\n")
    out.write("{\n")
    out.write("     locationInMesh (x y z);\n")
    out.write("     refinementSurfaces\n")
    out.write("     {\n")
    if bound == 0:
        for i in lst_of_group_names:
            if "refine" in i:
                out.write("         " + i + " {level (2  2);}\n")
            else:    
                out.write("         " + i + " {level (1  1);}\n") 
    elif bound == 1:
        for i in lst_of_group_names_ext:
            if "refine" in i:
                out.write("         " + i + " {level (2  2);}\n")
            else:    
                out.write("         " + i + " {level (1  1);}\n") 
    out.write("     }\n")

    out.write("     refinementRegions\n")
    out.write("     {\n")
    out.write("         wall\n")
    out.write("         {\n") 
    out.write("             mode  distance;\n")
    out.write("             levels  ((0.0 0));\n")
    out.write("         }\n")
    out.write("     }\n")
    out.write("\n")
    out.write("     features\n")
    out.write("     (\n")
    if bound == 0:
        for i in lst_of_group_names:
            if "refine" in i:
                out.write('         {file ' + '"' + i + '.eMesh"; level 2;}\n')
            else:
                out.write('         {file ' + '"' + i + '.eMesh"; level 1;}\n')
    elif bound == 1:
        for i in lst_of_group_names_ext:
            if "refine" in i:
                out.write('         {file ' + '"' + i + '.eMesh"; level 2;}\n')
            else:
                out.write('         {file ' + '"' + i + '.eMesh"; level 1;}\n')
    out.write("     );\n")
    out.write("\n")

    out.write("     minRefinementCells 0;\n")
    out.write("     maxGlobalCells 10000000;\n")
    out.write("     resolveFeatureAngle 30.0;\n")
    out.write("     nCellsBetweenLevels 4;\n")
    out.write("     maxLocalCells 500000;\n")
    out.write("     allowFreeStandingZoneFaces true;\n")
    out.write("}\n")
    out.write("\n")

    out.write("snapControls\n")
    out.write("{\n")
    out.write("     nFeatureSnapIter 10;\n")
    out.write("     multiRegionFeatureSnap true;\n")
    out.write("     nSolveIter 300;\n")
    out.write("     tolerance 1.0;\n")
    out.write("     nRelaxIter 5;\n")
    out.write("     nSmoothPatch 3;\n")
    out.write("     implicitFeatureSnap true;\n")
    out.write("     explicitFeatureSnap true;\n")
    out.write("}\n")
    out.write("\n")

    out.write("addLayersControls\n")
    out.write("{\n")
    out.write("     layers\n")
    out.write("     {\n")
    out.write('         "(blayer|wall).*"\n')
    out.write("             {\n")
    out.write("                 nSurfaceLayers 0;\n")
    out.write("             }\n")
    out.write("     }\n")

    out.write("     nSmoothSurfaceNormals 1;\n")
    out.write("     slipFeatureAngle 30.0;\n")
    out.write("     nBufferCellsNoExtrude 0;\n")
    out.write("     nRelaxIter 5;\n")
    out.write("     relativeSizes true;\n")
    out.write("     minMedianAxisAngle 90.0;\n")
    out.write("     maxFaceThicknessRatio 0.5;\n")
    out.write("     nSmoothNormals 3;\n")
    out.write("     maxThicknessToMedialRatio 0.5;\n")
    out.write("     nLayerIter 50;\n")
    out.write("     minThickness 0.05;\n")
    out.write("     nSmoothThickness 10;\n")
    out.write("     nGrow 0;\n")
    out.write("     nRelaxedIter 20;\n")
    out.write("     featureAngle 60.0;\n")
    out.write("     firstLayerThickness 0.1;\n")
    out.write("     expansionRatio 1.2;\n")
    out.write("}\n")
    out.write("\n")

    out.write("meshQualityControls\n")
    out.write("{\n")
    out.write("     minTetQuality 1.0E-20;\n")
    out.write("     minVol 1.0E-14;\n")
    out.write("     maxInternalSkewness 4.0;\n")
    out.write("     maxBoundarySkewness 20.0;\n")
    out.write("     maxConcave 80.0;\n")
    out.write("     minFaceWeight 0.05;\n")
    out.write("     minVolRatio 0.01;\n")
    out.write("     minTwist 0.05;\n")
    out.write("     minArea -1.0;\n")
    out.write("     maxNonOrtho 65.0;\n")
    out.write("     minTriangleTwist -1.0;\n")
    out.write("     minDeterminant 0.01;\n")
    out.write("     errorReduction 0.75;\n")
    out.write("     nSmoothScale 4;\n")
    out.write("     relaxed\n")
    out.write("     {\n")
    out.write("         maxNonOrtho 75.0;\n")
    out.write("     }\n")
    out.write("}\n")
    out.write("\n")

    out.write("mergeTolerance 1.0E-6;\n")
    out.write("debug 0;")
    out.close
    ##############################################################################################
    #controlDict
    ##############################################################################################
    out_name = str(pathName) + "/test_clean/system/" + "controlDict"
    out = open(out_name,"w")

    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   controlDict;\n}\n")
    out.write("\n")

    if flow != 2:
        out.write("application          simpleFoam;\n")
        out.write("startFrom            latestTime;\n")
        out.write("startTime            0.0;\n")
        out.write("endTime              200.0;\n")
        out.write("deltaT               1.0;\n")
        out.write("writeControl         timeStep;\n")
        out.write("writeInterval        10;\n")
        out.write("purgeWrite           2;\n")
        out.write("timeFormat           general;\n")
        out.write("timePrecision        6;\n")
        out.write("writeFormat          binary;\n")
        out.write("writePrecision       7;\n")
        out.write("writeCompression     uncompressed;\n")
        out.write("runTimeModifiable    true;\n")
    else:
        out.write("application          interFoam;\n")
        out.write("startFrom            latestTime;\n")
        out.write("startTime            0.0;\n")
        out.write("stopAt               endTime;\n")
        out.write("endTime              1.5;\n")
        out.write("deltaT               0.0001;\n")
        out.write("writeControl         adjustableRunTime;\n")
        out.write("writeInterval        0.0001;\n")
        out.write("purgeWrite           0;\n")
        out.write("writeFormat          binary;\n")
        out.write("writePrecision       6;\n")
        out.write("writeCompression     uncompressed;\n")
        out.write("timeFormat           general;\n")
        out.write("timePrecision        6;\n")
        out.write("runTimeModifiable    yes;\n")
        out.write("adjustTimeStep       yes;\n")
        out.write("\n")
        out.write("maxCo                0.8;\n")
        out.write("maxAlphaCo           0.8;\n")
        out.write("maxDeltaT            1;")
    out.close
    ##############################################################################
    #fvSchemes
    ##############################################################################
    out_name = str(pathName) + "/test_clean/system/" + "fvSchemes"
    out = open(out_name,"w")
    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   fvSchemes;\n}\n")
    out.write("\n")
    if flow != 2:
        out.write("ddtSchemes\n")
        out.write("{\n")
        out.write("     default             steadyState;\n")
        out.write("}\n")
        out.write("\n")
        out.write("gradSchemes\n")
        out.write("{\n")
        out.write("     default             Gauss linear;\n")
        out.write("     limited             cellLimited Gauss linear 1;\n")
        out.write("     grad(U)             $limited;\n")
        out.write("     grad(k)             $limited;\n")
        out.write("     grad(epsilon)       $limited;\n")
        out.write("}\n")
        out.write("\n")
        out.write("divSchemes\n")
        out.write("{\n")
        out.write("     default             none;\n")
        out.write("     div(phi,U)          bounded Gauss linearUpwind limited;\n")
        out.write("     turbulence          bounded Gauss limitedLinear 1;\n")
        out.write("     div(phi,k)          $turbulence;\n")
        out.write("     div(phi,epsilon)    $turbulence;\n")
        out.write("     div((nuEff*dev2(T(grad(U))))) Gauss linear;\n")
        out.write("}\n")
        out.write("\n")
        out.write("laplacianSchemes\n")
        out.write("{\n")
        out.write("     default             Gauss linear corrected;\n")
        out.write("}\n")
        out.write("\n")
        out.write("interpolationSchemes\n")
        out.write("{\n")
        out.write("     default             linear;\n")
        out.write("}\n")
        out.write("\n")
        out.write("snGradSchemes\n")
        out.write("{\n")
        out.write("     default             corrected;\n")
        out.write("}\n")
        out.write("\n")
        out.write("wallDist\n")
        out.write("{\n")
        out.write("     method meshWave;\n")
        out.write("}\n")
    else:
        out.write("ddtSchemes\n")
        out.write("{\n")
        out.write("     default             Euler;\n")
        out.write("}\n")
        out.write("\n")
        out.write("gradSchemes\n")
        out.write("{\n")
        out.write("     default             Gauss linear;\n")
        out.write("}\n")
        out.write("\n")
        out.write("divSchemes\n")
        out.write("{\n")
        out.write("     div(rhoPhi,U)  Gauss upwind;\n")
        out.write("     div(phi,alpha)  Gauss vanLeer;\n")
        out.write("     div(phirb,alpha) Gauss linear;\n")
        out.write("     div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear;\n")
        out.write("}\n")
        out.write("\n")
        out.write("laplacianSchemes\n")
        out.write("{\n")
        out.write("     default             Gauss linear corrected;\n")
        out.write("}\n")
        out.write("interpolationSchemes\n")
        out.write("{\n")
        out.write("     default             linear;\n")
        out.write("}\n")
        out.write("snGradSchemes\n")
        out.write("{\n")
        out.write("     default             corrected;\n")
        out.write("}\n")   
    out.close
    ###############################################################################
    #fvSolution
    ###############################################################################
    out_name = str(pathName) + "/test_clean/system/" + "fvSolution"
    out = open(out_name,"w")
    #header
    out.write("FoamFile\n{\n    version 2.0;\n    format   ascii;\n    class    dictionary;\n    object   fvSolution;\n}\n")
    out.write("\n")
    if flow != 2: #if flow is air or water steady
        out.write("solvers\n")
        out.write("{\n")
        out.write("     p\n")
        out.write("     {\n")
        out.write("         solver          GAMG;\n")
        out.write("         smoother        GaussSeidel;\n")
        out.write("         tolerance       1e-6;\n")
        out.write("         relTol          0.1;\n")
        out.write("     }\n")
        out.write("\n")
        out.write('"(U|k|omega|epsilon)"\n')
        out.write("     {\n")
        out.write("         solver          smoothSolver;\n")
        out.write("         smoother        symGaussSeidel;\n")
        out.write("         tolerance       1e-6;\n")
        out.write("         relTol          0.1;\n")
        out.write("     }\n")
        out.write("}\n")
        out.write("\n")
        out.write("SIMPLE\n")
        out.write("{\n")
        out.write("     residualControl\n")
        out.write("     {\n")
        out.write("         p               1e-4;\n")
        out.write("         U               1e-4;\n")
        out.write('         "(k|omega|epsilon)"  1e-4;\n')
        out.write("     }\n")
        out.write("     nNonOrthogonalCorrectors 0;\n")
        out.write("     pRefCell            0;\n")
        out.write("     pRefValue           0;\n")
        out.write("}\n")
        out.write("\n")
        out.write("potentialFlow\n")
        out.write("{\n")
        out.write("     nNonOrthogonalCorrectors 10;\n")
        out.write("}\n")
        out.write("\n")
        out.write("relaxationFactors\n")
        out.write("{\n")
        out.write("     fields\n")
        out.write("     {\n")
        out.write("         p               0.3;\n")
        out.write("     }\n")
        out.write("     equations\n")
        out.write("     {\n")
        out.write("         U               0.7;\n")
        out.write('         "(k|omega|epsilon).*" 0.7;\n')
        out.write("     }\n")
        out.write("}\n")
    else: #if flow is air-water mix
        out.write("solvers\n")
        out.write("{\n")
        out.write("     alpha.water\n")
        out.write("     {\n")
        out.write("         nAlphaCorr      1;\n")
        out.write("         nAlphaSubCycles 2;\n")
        out.write("         cAlpha          1;\n")
        out.write("     }\n")
        out.write("\n")
        out.write("     Phi\n")
        out.write("     {\n")
        out.write("         solver          GAMG;\n")
        out.write("         smoother        DIC;\n")
        out.write("         tolerance       1e-6;\n")
        out.write("         relTol          0.01;\n")
        out.write("     }\n")
        out.write("\n")
        out.write('     "pcorr.*"\n')
        out.write("     {\n")
        out.write("         solver          PCG;\n")
        out.write("         preconditioner  DIC;\n")
        out.write("         tolerance       1e-10;\n")
        out.write("         relTol          0;\n")
        out.write("     }\n")
        out.write("\n")
        out.write("     p_rgh\n")
        out.write("     {\n")
        out.write("         solver          GAMG;\n")
        out.write("         smoother        GaussSeidel;\n")
        out.write("         tolerance       1e-7;\n")
        out.write("         relTol          0.01;\n")
        out.write("     }\n")
        out.write("\n")
        out.write("     p_rghFinal\n")
        out.write("     {\n")
        out.write("         $p_rgh;\n")
        out.write("         tolerance       1e-07;\n")
        out.write("         relTol          0;\n")
        out.write("     }\n")
        out.write("\n")
        out.write("     U\n")
        out.write("     {\n")
        out.write("         solver          smoothSolver;\n")
        out.write("         smoother        symGaussSeidel;\n")
        out.write("         tolerance       1e-6;\n")
        out.write("         relTol          0;\n")
        out.write("     }\n")
        out.write("}\n")
        out.write("\n")
        out.write("potentialFlow\n")
        out.write("{\n")
        out.write("     nNonOrthogonalCorrectors 10;\n")
        out.write("     PhiRefCell               0;\n")
        out.write("     PhiRefValue              0;\n")   
        out.write("}\n")
        out.write("\n")
        out.write("PIMPLE\n")
        out.write("{\n")
        out.write("     momentumPredictor   no;\n")
        out.write("     nCorrectors         3;\n")
        out.write("     nNonOrthogonalCorrectors 1;\n")
        out.write("     piRefCell                0;\n")
        out.write("     pRefValue                0;\n") 
        out.write("}") 
    out.close
    #############################################################################################
    #setFields
    #############################################################################################
    if flow == 2: #if flow is air-water mix
        out_name = str(pathName) + "/test_clean/system/" + "setFieldsDict"
        out = open(out_name,"w")
        #header
        out.write("FoamFile\n{\n    version 2.0;\n    class    dictionary;\n    format	ascii;\n    object   setFieldsDict;\n}\n")
        out.write("\n")
        out.write("regions (\n")
        out.write("\n")
        out.write("     sphereToCell\n")
        out.write("     {\n")
        out.write("         centre      (x y z);\n")
        out.write("         radius      ____;\n")
        out.write("         fieldValues\n")
        out.write("             (\n")
        out.write("                 volScalarFieldValue alpha.water 1")
        out.write("             );\n")
        out.write("     }\n")
        out.write(");")
        out.close
    #############################################################################################
    #decomposeParDict
    #############################################################################################
    if cores > 1:
        out_name = str(pathName) + "/test_clean/system/" + "decomposeParDict"
        out = open(out_name,"w")
        out.write("FoamFile\n{\n    version 2.0;\n    class    dictionary;\n    format	ascii;\n    object   decomposeParDict;\n}\n")
        out.write("\n")
        out.write("numberOfSubdomains   " + str(cores) + ";\n")
        out.write("method               scotch;")
        out.close
