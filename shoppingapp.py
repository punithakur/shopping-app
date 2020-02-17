from model import *

class app:
    choise=0
    prolist=[]
    custlist=[]
    clist=[]
    orlist=[]
    def start(self):
        while True:
            self.printoption()
            if app.choise==1:
                self.addcategory()
            elif app.choise==2:
                self.catlisting()
            elif app.choise==3:
                self.addproduct()
            elif app.choise==4:
                self.productlisting()
            elif app.choise==5:
                self.addcustomer()
            elif app.choise==6:
                self.customerlisting()
            elif app.choise==7:
                self.catwise()
            elif app.choise==8:
                self.addorder()
            elif app.choise==9:
                self.orderhis()
            elif app.choise==10:
                break

            


    def printoption(self):
        print("1. add category")
        print("2. category listing")
        print("3. add product")
        print("4. product listing")
        print("5. add customer")
        print("6. customer listing")
        print("7. category-wise listing")
        print("8. order")
        print("9. order history")
        print("10. exit")

        app.choise=int(input("enter choise num"))

    
    def addcategory(self):
        ide=int(input("enter category id"))
        nm=input("enter category name")
        c=category()
        c.setcatid(ide)
        c.setcatname(nm)
        app.clist.append(c)
        print("category added")

        
    def catlisting(self):
        j=1
        for i in app.clist:
            print(j,i.getcatname())
            j+=1
    def catfinding(self,i):
        for j in app.clist:
            if j.getcatid()==i.getcatid():
                return j.getcatname()


    def addproduct(self):
        self.catlisting()
        i=int(input("enter your choise"))
        ide=int(input("enter the id"))
        nm=input("enter product name")
        price=int(input("enter product price"))

        p = product()
        p.setcatid(app.clist[i-1].getcatid())
        p.setproid(ide)
        p.setproname(nm)
        p.setproprice(price)
        app.prolist.append(p)

    def productlisting(self):
        j=1
        for i in app.prolist:
            
            p=self.catfinding(i)
            print(j,p,i.getproname(),i.getproprice())
            j+=1

    def addcustomer(self):
        list1=['seller','buyer']
        j=1
        for i in list1:
            print(j,i)
            j+=1
        ty=int(input("choise the option"))
        ide=int(input("enter the customer id"))
        nm=input("enter the customer name")
        pas=input("enter your password")
        add=input("enter your address")
        pin=int(input("enter your pincode"))

        c=cust()
        c.setcusttype(list1[ty-1])
        c.setcustid(ide)
        c.setcustname(nm)
        c.setcustpass(pas)
        c.setaddress(add)
        c.setpincode(pin)
        app.custlist.append(c)

    def customerlisting(eslf):
        for i in app.custlist:
            print(i.getcusttype(),i.getcustname(),i.getaddress(),i.getpincode())

    def catwise(self):
        self.catlisting()
        p=int(input("enter your choise- "))
        p=app.clist[p-1]
        print(p.getcatname())
        p=p.getcatid()
        for i in app.prolist:
            if p==i.getcatid():
                print(i.getproname(),i.getproprice())

    def addorder(self):
        o=order()
        x=int(input("enter order id"))
        o.setorderid(x)

        cs=int(input("enter custmer id"))
        
        for i in app.custlist:
            if cs==i.getcustid():
                o.setcustid(i.getcustid())
        
        self.catlisting()
        ct=int(input("enter your choise- "))
        ct=app.clist[ct-1].getcatid()
        o.setcatide(ct)
        j=1
        for i in app.prolist:
            
            print(j,i.getproname(),i.getproprice())
            j+=1
        pr=int(input("enter your choise- "))
        o.setproid(app.prolist[pr-1].getproid())

        app.orlist.append(o)

    def orderhis(self):
        custid=int(input("enter customer id"))
        for i in app.orlist:
            if custid==i.getcustid():
                for j in app.custlist:
                    if i.getcustid()==j.getcustid():
                        print(j.getcustname(),j.getaddress())
                for q in app.clist:
                    if i.getcatide()==q.getcatid():
                        print(q.getcatname())
                for w in app.prolist:
                    if i.getproid()==w.getproid():
                        print(w.getproname(),w.getproprice())
    
    








call=app()
call.start()






