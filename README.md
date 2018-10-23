# FDTD_make_shape

[SALMON](https://salmon-tddft.jp/) has a FDTD functionality to simulate electromagnetic problems. This program makes the input shape file.

## Requirements

 - Python 3
 - NumPy

If you are windows user who uses python for the first time, I recommend to install [WinPython](https://sourceforge.net/projects/winpython/) that includes all requirements for this program.

## Usage

`make_shape.py` is an executable file. `shape.inp` is a input file. `make_shape.py` and `shape.inp` **must be in the same hierarchy**.<br><br>
The input parameters are as follows:<br>

- ***al_em(3)*** <br>
Size of simulation box in electromagnetic analysis. **This must match the input parameter in SALMON**.

- ***dl_em(3)*** <br>
Spacing of real-space grids in electromagnetic analysis. **This must match the input parameter in SALMON**.

- ***n_s*** <br>
Number of shape-templates. Maximum is 200.

- ***rot_type*** <br>
Type of rotation for shape-template. `'degree'` and `'radian'` can be chosen. Default is `'radian'`.

- ***output*** <br>
Type of output file. `'cube'` and `'mp'` can be chosen. If `'cube'`, the output file can be drawn by [ParaView](https://www.paraview.org/download/)(Usage: Open the cube file by ParaView→click:Molecule→Apply→Gridded Data→Representation→Volume). Default is `'cube'`.

- ***typ_s(x)*** <br>
Type of x-th shape-template. Maximum of x is `n_s`. `'ellipsoid'`, `'half-ellipsoid'`, `'elliptic-cylinder'`, `'triangular-cylinder'`, `'rectangular-cylinder'`, `'elliptic-cone'`, `'triangular-cone'`, and `'rectangular-cone'` can be chosen.

- ***id_s(x)*** <br>
ID number of x-th shape-template. **This ID number must match the index of the input parameter in SALMON**(e.g. `epsilon`, `rmu`, and `sigma`).

- ***inf_s(x,:)*** <br>
Information of x-th shape-template. This depends on `typ_s`. See `about_inf_s.pdf` in detail.

- ***ori_s(x,3)*** <br>
Origin of x-th shape-template.

- ***rot_s(x,3)*** <br>
Rotation angle of x-th shape-template. Rotation axes of `rot_s(x,1:3)` correspond to x-, y-, and z-axes, respectively. 

## External Links

### SALMON Project
  - SALMON Official Website - https://salmon-tddft.jp/
  - SALMON Github Repository - https://github.com/salmon-tddft/SALMON/
