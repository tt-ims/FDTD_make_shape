# FDTD_make_shape

[SALMON](https://salmon-tddft.jp/) has a FDTD functionality to solve electromagnetic problems. This program, `FDTD_make_shape`, is a tool to make shapes for the FDTD calculation in the format of the input file of SALMON.

![figure](examples/09_elliptic-ring/image.png)

## Requirements

 - Python 3
 - NumPy

If you are windows user who uses python for the first time, I recommend to install [WinPython](https://sourceforge.net/projects/winpython/) that includes all requirements for this program.

## Usage

`make_shape.py` is an executable file. `shape.inp` is a input file. `make_shape.py` and `shape.inp` **must be in the same directory**. When you use WinPython, open `make_shape.py` by Spyder.exe that is included in WinPython and push F5 key.<br><br>
The input parameters are as follows:<br>

- ***al_em(3)*** <br>
Size of simulation box in electromagnetic analysis. **This must match the input parameter in SALMON**.

- ***dl_em(3)*** <br>
Spacing of real-space grids in electromagnetic analysis. **This must match the input parameter in SALMON**.

- ***n_s*** <br>
Number of shape-templates. Maximum is 200.

- ***iperiodic*** <br>
Dimension for periodic boundary condition. `0` is for isolated systems, and `3` is for periodic systems. **Note that the coordinate system ranges from `-al_em/2` to `al_em/2` for `iperiodic=0` while ranges from `0` to `al_em` for `iperiodic=3`**. Default is `0`.

- ***output*** <br>
Type of output file. `'cube'` and `'mp'` can be chosen. If `'cube'`, the output file can be drawn by [ParaView](https://www.paraview.org/download/)(Usage: Open the cube file by ParaView→click:Molecule→Apply→Gridded Data→Representation→Volume) in which `al_em` is used in atomic units. However, at this time(2018/11/27), ParaView cannot well draw for cuboid mesh(cubic mesh is no problem). Default is `'cube'`.

- ***rot_type*** <br>
Type of rotation for shape-template. `'radian'` and `'degree'` can be chosen. Default is `'radian'`.

- ***typ_s(x)*** <br>
Type of x-th shape-template. Maximum of x is `n_s`. `'ellipsoid'`, `'half-ellipsoid'`, `'elliptic-cylinder'`, `'triangular-cylinder'`, `'rectangular-cylinder'`, `'elliptic-cone'`, `'triangular-cone'`, `'rectangular-cone'`, and `'elliptic-ring'` can be chosen.

- ***id_s(x)*** <br>
ID number of x-th shape-template. **This ID number must match the index of the input parameter in SALMON**(e.g. `epsilon`, `rmu`, and `sigma`).

- ***inf_s(x,:)*** <br>
Information of x-th shape-template. This depends on `typ_s`. See `shape-template_manual.pdf` in detail.

- ***ori_s(x,3)*** <br>
Origin of x-th shape-template. Default is `0.0d0, 0.0d0, 0.0d0`.

- ***rot_s(x,3)*** <br>
Rotation angle of x-th shape-template. Rotation axes of `rot_s(x,1:3)` correspond to x-, y-, and z-axes, respectively. Priorities for rotation axes are x-, y-, and z-axes. Default is `0.0d0, 0.0d0, 0.0d0`.

## External Links

### SALMON Project
  - SALMON Official Website - https://salmon-tddft.jp/
  - SALMON Github Repository - https://github.com/salmon-tddft/SALMON/
