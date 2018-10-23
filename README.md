# FDTD_make_shape

[SALMON](https://salmon-tddft.jp/) has a FDTD functionality to simulate electromagnetic problems. This program makes the input shape file.

## Requirements

 - Python 3
 - NumPy

If you are windows user who uses python for the first time, I recommend to install [WinPython](https://sourceforge.net/projects/winpython/) that includes all requirements for this program.

## Usage

`make_shape.py` is an executable file. `shape.inp` is a input file for this program. `make_shape.py` and `shape.inp` **must be in the same hierarchy**.<br><br>
The input parameters are as follows:<br>

- ***al_em(3)*** <br>
Size of simulation box in electromagnetic analysis. This must match the input parameter in SALMON.

- ***dl_em(3)*** <br>
Spacing of real-space grids in electromagnetic analysis. This must match the input parameter in SALMON.

- ***n_s*** <br>
Number of shape-templates. Maximum is 200.

- ***rot_type*** <br>
Type of rotation for shape-template. `'degree'` and `'radian'` can be chosen. Default is `'radian'`.

- ***output*** <br>
Type of output file. `'cube'` and `'mp'` can be chosen. Default is `'cube'`.

- ***typ_s(x)*** <br>
Type of x th shape-templates. Maximum of x is determined by `n_s`.

- ***id_s(x)*** <br>
Tes.

- ***inf_s(x,:)*** <br>
Tes.

- ***ori_s(x,3)*** <br>
Tes.

- ***rot_s(x,3)*** <br>
Tes.

## External Links

### SALMON Project
  - SALMON Official Website - https://salmon-tddft.jp/
  - SALMON Github Repository - https://github.com/salmon-tddft/SALMON/
