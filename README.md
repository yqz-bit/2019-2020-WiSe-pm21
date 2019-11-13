# Introduction

These are Jupyter notebooks for PM-21 (Python: Der Alleskleber), Winter Semester
2019-2020, Faculty of Biology, University of Freiburg.

## View at https://mybinder.org/v2/gh/astraw/2019-2020-WiSe-pm21/master

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/astraw/2019-2020-WiSe-pm21/master)

## Run locally with anaconda

```
conda env create -f environment.yml
source activate pm21
jupyter notebook
```

## This course on Ilias

https://ilias.uni-freiburg.de/goto.php?target=crs_1383552&client_id=unifreiburg

## Some useful Python data science cheat sheets

- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf

## In case matplotlib in Windows shows DLL errors:

When importing matplotlib, if you are getting an error like
`ImportError: DLL load failed: Das angegebene Modul wurde nicht gefunden` or
`ImportError: DLL load failed: The specified module could not be found`, do:

1) Open a Terminal in your `pm21` Anaconda virtual environment.
2) Inside the terminal, type this line-by-line:

```
pip uninstall pillow
pip uninstall matplotlib
conda uninstall matplotlib
conda install matplotlib
```

See [this](https://github.com/matplotlib/matplotlib/issues/14691#issuecomment-508552825)
for related information.
