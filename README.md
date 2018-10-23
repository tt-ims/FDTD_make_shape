# FDTD_make_shape

[SALMON](https://salmon-tddft.jp/) has a FDTD functionality to simulate electromagnetic problems. This program makes the input shape file.

## Requirements

 - Python 3
 - NumPy

If you are windows user who uses python for the first time, I recommend to install [WinPython](https://sourceforge.net/projects/winpython/) that includes all requirements for this program.

## Usage

### shape.inp

`shape.inp` is a input file for this program. `shape.inp` and `make_shape.py` **must be in the same hierarchy**.<br>
The input parameters are as follows:<br>

- ***al_em(3)*** <br>
Size of simulation box in electromagnetic analysis.

- ***dl_em(3)*** <br>
Spacing of real-space grids in electromagnetic analysis.

## External Links

### SALMON Project
  - SALMON Official Website - https://salmon-tddft.jp/
  - SALMON Github Repository - https://github.com/salmon-tddft/SALMON/
