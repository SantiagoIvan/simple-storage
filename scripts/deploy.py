# Brownie es un framework de desarrollo y de testing para smart contracts proyectos en python.
# Esas cosas que hice manualmente de compilar el proyecto, crear las ABI y las interfaces de los contratos que iba a deplotar,
# Brownie las hace manualmente.
# Creando contratos en Contracts, con brownie compile automaticamente me compila los contratos en me crea
# los archivos .json con toda la informacion del compilado.
# Tambien se encarga de levantar localmente una blockchain de prueba Ganache si no esta levantada con ciertos comandos


# Lo que necesito agregar es una direccion y una clave privada para testear, como una muck account
# Brownie tiene un account package para entender como trabajar con las cuentas

from hashlib import new
from brownie import accounts, SimpleStorage, network

# De esta forma importo el paquete y puedo acceder a las cuentas de Ganache, o mandarle otras cuentas mias de la TestNet

# Contiene la logica para deployar al contrato
def deploy_simple_storage():
    # 1) Ganache
    # my_account = accounts[0] #la primera de esas 10 que te crea con Ganache
    # print(my_account)
    # Esto solo funciona usando Ganache

    # 2) Cuenta integrada encriptada - La mas segura
    # Puedo por linea de comando agregar mi wallet de metamask para que trabaje con esa
    # si decido deployar el contrato en una Red de prueba
    # brownie accounts new <nombre>
    # Despues te va a pedir la clave privada y una clave de encriptacion y uala, tenes una clave integrada a Brownie
    
    # my_account = accounts.load("santu-account")
    # print(my_account)
    
    # Ahora cada vez que corras el script te va a pedir la clave para desencriptar la cuenta.

    # 3) Cuenta agregada a las variables de entorno
    # export PRIVATE_KEY=0xetcetera en un archivo .env
    # archivo brownie-config.yaml:
    # En ese archivo Brownie se fija informacion sobre donde se va a deployar o buildear o agarrar cosas de ahi
    # dontenv: .env 
    # Con esa linea le decis a brownie que cuando corra scripts, las variables de entorno las saque del archivo .env
    # En el archivo .env vamos a tener el export de la private key
    # account = accounts.add(os.getenv("PRIVATE_KEY"))


    # Por ahora voy a usar la de Ganache
    my_account = get_account()
    # Para deployar el contrato, primero necesito traerlo aca. Antes en Web3.py tenia que leer el archivo y hacer toda la bola esa del abi, bytecode, crear la transaccion.
    # Con brownie, puedo directamente importar los contratos como si fueran packages
    simple_storage = SimpleStorage.deploy({"from": my_account}, publish_source=True) #devuelve una instancia del contrato deployado.
    # ese objeto posee la interfaz del contrato.
    # Testeando la ejecucion de las funciones del contrato
    value = simple_storage.retrieve()
    print(value)
    # En este caso, no hizo falta una transaccion, debido a que es una funcion de tipo 'view'

    # Ahora para generar efecto de lado sobre la blockchain, necesito de alguna forma incluir el from address, ya que necesito generar la transaccion
    transaction = simple_storage.store(15, {"from": my_account})
    transaction.wait(1) # va a esperar a que una cantidad de bloques sea minada antes de continuar la ejecucion
    # Esto es con el fin de evitar la condicion de carrera. Si yo consulto el valor antes del wait, nada me asegura que el bloque no se mino y que la transaccion fue confirmada dentro de la blockchain
    # Como estamos en Ganache no va a pasar nada, pero en las demas redes si.
    # Segun vitalik, para asegurar que una transaccion haya sido confirmada, hay que esperar 7 u 8 bloques por lo tanto
    # transaction.wait(7)
    # https://ethereum.stackexchange.com/questions/109862/race-conditions-in-brownie-how-to-guarantee-this-will-execute-in-order
    new_value = simple_storage.retrieve()
    print(new_value)

    # Se puede ver lo facil que es con Brownie interactuar con la blockchain




# Development networks - redes temporales. Como la Ganache network, todas las transacciones son borradas luego de la ejecucion del test/script o lo que se este ejecutando en esa funcion
 
# Etherum networks - son persistentes. Como Rinkebi
# 
# Antes, en Web3.py usamos un HttpProvider con una url. Vamos a hacer algo parecido aca 

# archivo .env
# export WEB3_INFURA_PROJECT_ID=<id_de_Infura>

# Si en lugar de Ganache, quisiera deployar en Rinkeby, necesito cambiar de red.
# Para eso, debemos importar el componente network de brownie. 
# Si la red es otra diferente a la default (Ganache) debo especificarlo en el comando

# brownie run scripts/deploy.py --network rinkeby (por ejemplo)
# deploy_simple_storage() actualmente esta usando accounts[0] que es lo que obtenes cuando usas Ganache, por lo tanto tirara error.

# Si yo quiero que se adapte a la red, debo primero consultar la red en la que quiero ejecutar el script

def get_account():
    if(network.show_active() == "development"):
        print("Ganache")
        return accounts[0]
    else:
        print("otro")
        return accounts.load("santu-account") #me va a decir que no tengo plata :rat:

    

# Ejecuta las funciones de deploy
def main():
    deploy_simple_storage()
    print("hello")