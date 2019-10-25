import sys
from omniORB import CORBA
import KeyGen


orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

ior = sys.argv[1]
obj = orb.string_to_object(ior)

generatorObj = obj._narrow(KeyGen.Generator)

if generatorObj is None:
    print "Object reference is null"
    sys.exit(1)

menu = "[1]Gerar senha\n[2]Decodificar senha\n[0]Sair"


run = True
while run:
    print menu
    op = raw_input(":")
    if op == "1": 
        key = raw_input("Digite uma palavra para gerar a senha: ")
        result  = generatorObj.codeKey(key)
        print "Senha gerada: '%s'" % (result)
    elif op == "2":
        key = raw_input("Digite a senha que foi gerada: ")
        result  = generatorObj.decodeKey(key)
        print "Palavra resultante: '%s'" % (result)
    elif op == "0":
        run = False
    else:
        print "Opcao invalida"