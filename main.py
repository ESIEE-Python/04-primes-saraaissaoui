"""
Module principal pour vérifier et afficher les nombres premiers jusqu'à 100.
"""

from math import sqrt  # Cette ligne peut être supprimée si `sqrt` n'est pas utilisée

def isprime(p):
    """
    Vérifie si un nombre entier p est un nombre premier.
    
    Args:
        p (int): Le nombre à vérifier.
    
    Returns:
        bool: True si p est un nombre premier, False sinon.
    """
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """
    Fonction principale pour tester et afficher les nombres premiers jusqu'à 100.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
