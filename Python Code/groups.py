def get_group(pathName, in_file, group_names, points):

    line = in_file.readline()
    group_name =line[line.rfind(" "):]
    group_name = group_name[1:-1] #get rid of spaces at beginning and end
    group_names.append(group_name)
    # get number of triangles
    elements = in_file.readline()
    elements = int(elements[elements.rfind(" "):])
    #print(elements)

    # Loop for triangles
    element_points = []
    for element in range(elements):
        element = in_file.readline()
        element = [int(x) for x in element.split(" ")]
        element = element[1:]
        element_points.append(element)
    #print(element_points)

    #replace point indicies for the actual coordinates, write it out to file
    out_name = str(pathName) + "/test_clean/constant/triSurface/" + group_name + ".stl"
    out = open(out_name,"w")
    out.write("solid ascii\n")

    for i in range(elements):
        out.write("facet normal 1.00 0.00 0.00\n")                                                     
        out.write("outer loop\n")
        for j in range(3):
            #print(element_points[i][j])
            element_points[i][j] = str(points[element_points[i][j]])
            element_points[i][j] = element_points[i][j].replace('[','').replace(',','').replace(']','')
            out.write("vertex " + (element_points[i][j]) + "\n")
    #print(element_points)
        out.write("endloop\n")
        out.write("endfacet\n")

    out.write("endsolid")
    out.close()
    return group_names