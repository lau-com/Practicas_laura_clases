from operator import truediv
from xml.dom import minicompat


class plato_de_comida:
    def __init__(self,verduras, frutas, cereales, tuberculos, lacteos, proteina, frutos_secos, tamaño_del_plato,tipo_de_plato,postre , bebida, maridaje, menu_dietetico, salsas):
        self.verduras= verduras
        self.frutas= frutas 
        self.cereales= cereales
        self.tuberculos= tuberculos
        self.lacteos= lacteos
        self.proteina= proteina
        self.frutos_secos= frutos_secos
        self.tamaño_del_plato= tamaño_del_plato
        self.tipo_de_plato= tipo_de_plato
        self.postre= postre 
        self.bebida= bebida
        self.maridaje= maridaje
        self.menu_dietetico= menu_dietetico
        self.salsas= salsas

    def mostrar_tamaño_del_plato (self):
        print(self.tamaño_del_plato)
 
    

    def Calcular_calorias(self,caloriasmin):
        calorias=0
        if self.verduras==True:
            calorias=calorias+10
        if self.verduras==True:
            calorias=calorias+50
        if self.cereales==True:
            calorias=calorias+15
        if self.tuberculos==True:
            calorias=calorias+20
        if self.lacteos==True:
            calorias=calorias+17
        if self.proteina==True:
            calorias=calorias+75
        if self.frutos_secos==True:
            calorias=calorias+6
        if self.tipo_de_plato=="Plato fuerte":
            calorias=calorias+130
        if self.tipo_de_plato=="postre":
            calorias=calorias+210
        if self.tipo_de_plato=="Bebida":
            calorias=calorias+60
        if self.tamaño_del_plato=="mediano":
            calorias=calorias+60
        if self.tamaño_del_plato=="pequeño":
            calorias=calorias+41
        if self.tamaño_del_plato=="Grande":
            calorias=calorias+80
        if self.postre==True:
            calorias=calorias+100
        if self.bebida==True:
            calorias=calorias+60
        if self.maridaje==True:
            calorias=calorias+50
        if self.menu_dietetico=="aplica":
            calorias=calorias/2
        if self.salsas==True:
            calorias=calorias+48
        if calorias<caloriasmin:
            calorias=caloriasmin

        print(calorias)




Salmon_salteado=plato_de_comida(True,False,True,False,False,True,False,"mediano","Plato fuerte", False,False,False,"no aplica",False )
Volcan_de_chocolate=plato_de_comida(False,False,True,False,True,True,False,"pequeño","postre",True,False,False,"opcional",True)
Sushi=plato_de_comida(True,False,True,True,False,True,True,"Grande","Plato fuerte",False,False,False,"opcional",True)
Mojito=plato_de_comida(False,True,False,False,False,False,True,"pequeño","Bebida",False,True,True,"no aplica",False)

Salmon_salteado.mostrar_tamaño_del_plato()
Volcan_de_chocolate.mostrar_tamaño_del_plato()
Sushi.mostrar_tamaño_del_plato()
Mojito.mostrar_tamaño_del_plato()


Salmon_salteado.Calcular_calorias(380)
Volcan_de_chocolate.Calcular_calorias(80)
Sushi.Calcular_calorias(70)
Mojito.Calcular_calorias(40)

