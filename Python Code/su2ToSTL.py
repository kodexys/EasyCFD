def convertFile(pathName, fileName):
    from groups import get_group
    import os, shutil
    os.chdir(str(pathName))
    
    if os.path.exists('test_clean'):
        shutil.rmtree('test_clean')

    if not os.path.exists('test_clean'):
        os.mkdir('test_clean')

    os.chdir(str(pathName) + '/test_clean')

    if not os.path.exists('constant'):
        os.mkdir('constant')

    if not os.path.exists('0'):
        os.mkdir('0')

    if not os.path.exists('system'):
        os.mkdir('system')

    os.chdir(str(pathName) + '/test_clean/constant/')
    if not os.path.exists('triSurface'):
        os.mkdir('triSurface')

    test_clean = open(str(fileName),"r")

    # Get number of nodes
    line = test_clean.readline()
    while("NPOIN" not in line):
        line = test_clean.readline()
    nodes = int(line[line.rfind(" "):]) 
    #print(nodes)

    # Loop to read xyz node coordinates into list
    points = []
    for n in range(nodes):
        coord = test_clean.readline()
        coord = coord[:coord.rfind(" ")]
        #points.append(coord)
        point = [float(x) for x in coord.split(" ")]
        points.append(point)
    #print(points)

    # Find minimum and maximum x coords, y coords, and z coords
    x_coords = []
    y_coords = []
    z_coords = []
    for i in range(len(points)):
        x_coords.append(points[i][0])
        y_coords.append(points[i][1])
        z_coords.append(points[i][2])
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    z_min = min(z_coords)
    z_max = max(z_coords)

    # Center stl by finding its center and shifting it to (0 0 0)
    x_mid = (x_max + x_min)/2
    y_mid = (y_max + y_min)/2
    z_mid = (z_max + z_min)/2


    for i in range(len(x_coords)):
        x_coords[i] -= x_mid
        y_coords[i] -= y_mid
        z_coords[i] -= z_mid

    # Update minimum and maxium coordinates for blockMeshDict vertices
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    z_min = min(z_coords)
    z_max = max(z_coords)

    # Shifting stl
    for i in range(len(points)):
        points[i][0] -= x_mid
        points[i][1] -= y_mid
        points[i][2] -= z_mid

    # Get number of groups
    line = test_clean.readline()
    while("NMARK" not in line):
        line = test_clean.readline()
    groups = int(line[line.rfind(" "):]) 
    #print(groups)
    group_names = []
    # print out stl for each group
    for group in range(groups):
        lst_of_group_names = get_group(pathName, test_clean, group_names, points)
    lst_of_group_names_ext = lst_of_group_names.copy()
    return (x_min, x_max, y_min, y_max, z_min, z_max, lst_of_group_names, lst_of_group_names_ext)  