#cust
#cat
#product
class category:
    def setcatid(self,ide):
        self.id=ide

    def setcatname(self, name):
        self.name=name

    def getcatid(self):
        return self.id

    def getcatname(self):
        return self.name


class product(category):
    def setproid(self,idl):
        self.id=idl
    
    def setcatid(self,ide):
        self.id2=ide

    def setproname(self,name):
        self.name=name

    def setproprice(self,price):
        self.price=price
    
    def getcatid(self):
        return self.id2

    def getproid(self):
        return self.id

    def getproname(self):
        return self.name

    def getproprice(self):
        return self.price
    



class cust:

    def setcusttype(self,typ):
        self.type=typ

    def setcustid(self, ide):
        self.id=ide

    def setcustname(self,name):
        self.name=name

    def setcustpass(self, pas):
        self.pas=pas

    def setaddress(self, add):
        self.add=add

    def setpincode(self,pin):
        self.pin=pin

    def getaddress(self):
        return self.add

    def getpincode(self):
        return self.pin

    def getcusttype(self):
        return self.type
    
    def getcustid(self):
        return self.id

    def getcustname(self):
        return self.pas
    


class order:
    def setorderid(self,ie):
        self.id9=ie
    
    def setcatide(self, cid):
        self.id8=cid
    
    def setproid(self,id4):
        self.id7=id4
    
    def setcustid(self,id3):
        self.id=id3
    
    def getcatide(self):
        return self.id8
    
    def getproid(self):
        return self.id7
    
    def getcustid(self):
        return self.id


    def getorderid(self):
        return self.id9    







    
