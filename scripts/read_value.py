# interactuar con contratos ya deployados
from brownie import SimpleStorage, accounts, config

def read_contract():
    # SimpleStorage es un objeto tipo array de deploys. Por lo tanto, los diferentes indices seran
    # los diferentes deploys que se han persistido. Nos da la direccion donde se encuentra el contrato
    
    # Primer deploy
    # SimpleStorage[0]

    # Ultimo deploy realizado
    # SimpleStorage[-1]

    # Lo voy a poder ver en la ruta build/deployments/<chain_id>
    # En el caso de Rinkeby, sera build/deployments/4

    # No es necesario tener el ABI ni la address. La direccion la sabe por lo que dije arriba, y el ABI lo sabe cuando compila, en build/contracts
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())
    #no va a funcionar porque no esta deployado porque no tengo dinero en la cuenta
    pass


def main():
    read_contract()
