import sys
from omniORB import CORBA, PortableServer
from generator import Generator;
import KeyGen, KeyGen__POA

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

ei = Generator()
eo = ei._this()

with open("id", "w") as objid:
    objid.write(orb.object_to_string(eo))

obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(obj)
print "Server running"

poaManager = poa._get_the_POAManager()

poaManager.activate()

orb.run()