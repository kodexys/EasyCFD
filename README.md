# EasyCFD
EasyCFD is an automated open source workflow for computational fluid dynamics simulations. 

This page containts the following:
* Python Code
   * ezFOAM.py
      * The graphics window the user interacts with to supply input necessary for building an OpenFOAM case
   * main.py
      * The master function that ezFOAM.py calls. It contains a function that calls all the functions below
   * make0.py
      * Builds the 0 folder
   * makeConstant.py
      * Builds the constant folder
   * makeSystem.py
      * Builds the system folder
   * su2ToSTL.py
      * Converts the enGrid SU2 file to STL files for each named boundary
   * groups.py
      * Function called by su2ToSTL.py that extracts the boundary names
      
      
      
