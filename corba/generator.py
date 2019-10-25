import KeyGen, KeyGen__POA

class Generator(KeyGen__POA.Generator):
    def codeKey(self, key):
        key = key.encode("hex")
        return key
    
    def decodeKey(self, key):
        key = key.decode("hex")
        return key