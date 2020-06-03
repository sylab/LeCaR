from .lecar import LeCaR

def get_algorithm(alg_name):
    alg_name = alg_name.lower()

    if alg_name == 'lecar':
        return LeCaR
    return None
