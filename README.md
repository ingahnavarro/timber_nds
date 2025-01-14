# timber_nds

## Installation

This package is built with `setuptools`. To install, navigate to the root of the downloaded package (where the pyproject.toml file is) and execute:

`pip install .`

If you want to have an editable installation (e.g. for development):

`pip install . -e`

If you are planning on developing this package, it is recommended that you first create a new conda environment. Activate the new environment and install the package into that environment.

## Quick start

```python
import package_name as pn

pn.my_function() # Returns None
my_class = pn.MyClass()
```

## Python version

This package, in its current form, runs on Python versions from 3.7+

## Connections
Not included, any value was modified because of this


## Limitations
El cálculo es para piezas rectangulares
No se incluye la revisión de esfuerzos de compresión neta en cálculos de flexotensión. 
No se incluyen modificaciones geométricas de los elementos para el cálculo, se asumen piezas sin perforaciones o cortes, exceptuando las incisiones. 
No se incluye la revisión por aplastamiento para fuerzas horizontales y se considera que la fuerza cortante es representativa de la fuerza en el apoyo. Si existe alguna condición que pueda afectar esto, debe considerarse por aparte. 
No se incluyen efectos de segundo orden en el cálculo por flexocompresión
Unidades: cm y kgf, para que haya congruencia. Esto se puede modificar en la app.
En la app no se pueden borrar secciones o elementos. 

Direcciones locales: `x` es longitudinal, `y` horizontal y `z` vertical. 
Ejes globales: `x` y `y` horizontales,  `z`vertical.