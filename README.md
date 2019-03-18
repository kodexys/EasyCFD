# EasyCFD
EasyCFD is an automated open source workflow for computational fluid dynamics (CFD) simulations. The goal of this project is to shatter the status-quo in education and industry that CFD software is difficult and expensive to use. EasyCFD makes OpenFOAM, an open source CFD software package, easy and accessible by maximizing work done by the computer and minimizing work done by the human user without sacrificing accuracy.

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
* Sample Geometry
   * Provided STL geometry files to be processed through enGrid
* Necessary Software
   * enGrid is the software used for preparing STL geometry files for OpenFOAM use. An installer is included in this folder, but it can also be downloaded from https://sourceforge.net/projects/engrid/
   * Python 3 is the programming language of EasyCFD. The Python 3.7.2 installer is included in this folder, but other Python 3 versions can be downloaded from https://www.python.org/downloads/ 
   * blueCFD-Core is OpenFOAM for Microsoft Windows and runs the CFD simulations. The latest version can be downloaded from http://bluecfd.github.io/Core/Downloads/
      
      
      
