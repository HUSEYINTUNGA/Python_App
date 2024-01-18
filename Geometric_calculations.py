import numpy as np

class Geometric_Calculations:
    def __init__(self,name):
        self.name = name

#Daire Sınıfı       
class Circle(Geometric_Calculations):
    def __init__(self, radius):
        super().__init__("Daire")
        self.radius = radius
            
        
    def Perimeter(self):
        return self.radius*np.pi*2           
    
    def Area(self):
        return np.pi*(self.radius**2)

#Kare Sınıfı    
class Square(Geometric_Calculations):
    def __init__(self,edge_length):
        super().__init__("Kare")
        self.edge=edge_length

    def Area(self):
        return self.edge**2

    def Perimeter(self):
        return self.edge*4

#Dikdörtgen Sınıfı  
class Rectangle(Geometric_Calculations):
    def __init__(self,short_edge,long_edge):
        super().__init__("Dikdortgen")
        self.short=short_edge
        self.long=long_edge
    
    def Area(self):
        return self.short*self.long
    
    def Perimeter(self):
        return 2*(self.short+self.long)

# Düzgün Beşgen Sınıfı   
class Pentagon(Geometric_Calculations):
    def __init__(self, edge_length):
        super().__init__("Beşgen")
        self.edge=edge_length
    
    def Area(self):
        return (5*(self.edge**2))/4*np.tan(np.pi/5)
    
    def Perimeter(self):
        return 5*self.edge
    
#Üçgen Sınıfı                
class Right_Triangle(Geometric_Calculations):
    def __init__(self,height,base_length):
        super().__init__("Üçgen")
        self.height=height
        self.base=base_length
        
    def Area(self):
        return (1/2)*self.base*self.height    

class Cylinder(Geometric_Calculations):
    def __init__(self,height,radius):
        super().__init__("Silindir")
        self.height=height
        self.radius=radius
        self.diameter=2*self.radius

    def SurfaceArea(self):
        return np.pi*self.diameter*(self.radius+self.height)
        
    def LateralArea(self):
        return  np.pi*self.diameter*self.height   

    def Volume(self):
        return np.pi*(self.radius**2)*self.height
        
class Cone(Geometric_Calculations):
    def __init__(self, height, radius):
        super().__init__("Koni")
        self.height=height
        self.radius=radius
        self.a=np.sqrt((self.radius**2)+self.height)
        
    def Volume(self):
        return (1/3)*np.pi*(self.radius**2)*self.height
        
    def SurfaceArea(self):
        return np.pi*(self.radius**2)+(2*np.pi*self.radius*self.a)        
#Diamond,Hexagon,parallelogram,trapezoid

class Cube(Geometric_Calculations):
    def __init__(self,edge_length):
        super().__init__("Küp")
        self.edge=edge_length
        
    def SurfaceArea(self):
        return 6*(self.edge**2)
    
    def Volume(self):
        return self.edge**3    

class Pyramid(Geometric_Calculations):
    def __init__(self,base_edge,height):
        super().__init__("Dörtgen Piramit")
        self.edge=base_edge
        self.height=height
        self.heigtOfTriangle=np.sqrt(((self.edge/2)**2)+(self.height**2))

    def SurfaceArea(self):
        return (self.edge**2) + ((self.edge*self.heightOfTriangle)/2)
    
    def Volume(self):
        return (self.edge*self.height)/3
    
class Trapezoid(Geometric_Calculations):
    def __init__(self,up_base,down_base,height):
        super().__init__("Yamuk")
        self.up=up_base
        self.down=down_base
        self.height=height
        
    def SurfaceArea(self):
        return ((self.up+self.down)/2)*self.height    
    
    
#Yazdığımız sınıfların ve metotların test kısmı

ucgen=Right_Triangle(2,3)
print("{} br yüksekliğe ve {} br taban alanına sahip {}in alanı : {}" .format(ucgen.height,ucgen.base,ucgen.name,ucgen.Area()))

kare=Square(5)
print("{} br kenar uzunluğuna sahip {}nin; \nAlanı : {} \nÇevresi : {}".format(kare.edge,kare.name,kare.Area(),kare.Perimeter()))

daire=Circle(6)
print("{} br yarıçapa sahip {}nin; \nAlanı : {} \nÇevresi : {}".format(daire.radius,daire.name,daire.Area(),daire.Perimeter()))

besgen=Pentagon(10)
print("{} br kenar uzunluğuna sahip düzgün {}in; \nAlanı : {} \nÇevresi : {}".format(besgen.edge,besgen.name,besgen.Area(),besgen.Perimeter()))

dortgen=Rectangle(6,8)
print("{} br kısa kenar uzunluğuna ve {} br uzun kenar uzunluğuna sahip {}in; \nAlanı : {}\nÇevresi : {}".format(dortgen.short,dortgen.long,dortgen.name,dortgen.Area(),dortgen.Perimeter()))


#H.TNG

# Bu programı geliştirmeye devam edeceğim, daha geniş şekil ağı ve hesap yöntemleri ile destekleyerek geliştirmek