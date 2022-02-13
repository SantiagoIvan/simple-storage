from brownie import SimpleStorage, accounts
# brownie test
# te levanta tambien Ganache si es necesario

# brownie test -k <nombre_de_una_funcion> 
# testea una funcion en especifico


# Deployando en una red de Prueba:
# brownie networks list - lista todas las redes compatibles con brownie, ya viene incluida con los adapters de esas redes
# facilita mucho mas la conexion que haciendolo manualmente con web3.py

def test_deploy():
    # Setup inicial
    my_account = accounts[0]
    # Acciones
    simple_storage = SimpleStorage.deploy({"from": my_account})
    initial_value = simple_storage.retrieve()
    expected = 0
    # Comprobaciones
    assert initial_value == expected

def test_updating_storage():
    my_account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": my_account})
    
    transaction = simple_storage.store(15, {"from": my_account})
    transaction.wait(1)
    value = simple_storage.retrieve()
    expected = 15

    assert value == expected

