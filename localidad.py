"""
TAD Localidad:

- Generadora:
    - localidad(corta: str, larga: str) -> Localidad
- Selectoras:
    - corta(loc: Localidad) -> str
    - larga(loc: Localidad) -> str
"""

def localidad(corta, larga):
    return [corta, larga]

def corta(loc):
    return loc[0]

def larga(loc):
    return loc[1]
