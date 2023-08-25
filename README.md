[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# EPECsolve
This repository is part of the [EPECSolve](https://github.com/ssriram1992/EPECsolve/) project, and contains the data and instances of the paper _When Nash Meets Stackelberg_ (to appear, Management Science).
- [Code](https://github.com/ssriram1992/EPECsolve/)
- [Instances](https://github.com/ds4dm/EPECInstances)
- [arXiv](https://arxiv.org/abs/1910.06452) pre-print with the detailed mathematical description of our instances


Goverments act as Stackelberg leaders by trading energy, with the aim of minimizing their emissions, and eventually to maximize tax incomes. Within each country, energy producers act as Stackelberg followers and play a Nash game between themselves, aiming to maximize their profits.  A full description of these instances is available [here](Description.pdf)


## Folder organization

We generated three instances sets for our computations. 
- _InstanceSetA_ contains 149 instances where there are 3 to 5 countries 
- _InstanceSetB_ contains 50 instances with strictly 7 countries. These instances were selected if the full enumeration algorithm was not able to solve them within 10 second on a single core machine.
- _InstanceSetInsights_ contains 50 instances with 2 countries with 3 followers each. Such instances are useful to derive managerial insights from our model 
- _ChileArgentina_ contains the ChileArgentina case-study data and instance generator
- _ResultParser.py_ produces the tables that can be found in the [arXiv](https://arxiv.org/abs/1910.06452) pre-print (and the paper)
- _PaperTables.xlxs_ contains the aggregate results of our tests and the content of the tables reported in our paper.
