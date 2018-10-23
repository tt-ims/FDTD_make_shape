List of all input keywords
==========================

-  `&calculation`_
-  `&control`_
-  `&units`_
-  `&parallel`_
-  `&system`_
-  `&atomic_red_coor`_
-  `&atomic_coor`_
-  `&pseudo`_
-  `&functional`_
-  `&rgrid`_
-  `&kgrid`_
-  `&tgrid`_
-  `&propagation`_
-  `&scf`_
-  `&emfield`_
-  `&maxwell`_
-  `&analysis`_
-  `&hartree`_
-  `&ewald`_
-  `&opt`_ (Trial)
-  `&md`_  (Trial)
-  `&misc`_

&calculation
------------


- **calc_mode** (character, 0d/3d)
   Choice of Calculation modes. ``'GS'`` and ``'RT'`` can be chosen.
   If ``&system/iperiodic=3``, ``'GS_RT'`` can be chosen.
