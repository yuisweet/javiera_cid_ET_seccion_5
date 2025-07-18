productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'C-123': [387990,10], 
        'C-111': [327990,4], 
        'C-234': [424990,1],
        'C-456': [664990,21], 
        'C-477': [290890,32], 
        'C-334': [444990,7],
        'C-1222': [749990,2], 
        'C-2906': [349990,1]}
#Consultar stok total de una marca especifica
#El sistema debe permitir al usuario ingresar una marca ,
#y mostar cuantas unidades hay disponibles para esa marca
def stok_marca(lst_productos: dict, lst_stok: dict, marca_buscada:str)->int:
        for lst_stok in lst_productos:
                if lst_productos[marca_buscada][lst_stok]:
                        print()
def busqueda_precio(lst_productos: dict, lst_stok: dict, p_mi: int, p_max: int)->None:
#Buscar productos por rango de precio. 
#Se debe ingresar un precio minimo y uno maximo. 
#El sistema debe listar los codigos y marcas de los productos que se encuentran en este rango de precio y tengan stok disponibles.
def actualizar_precio(lst_stok: dict, codigo: str, nuevo_precio: int)->bool:
def menu():
        while True: 
                print("\nMENU:")
                print("1. Consultar stok total de una marca específica.")
                print("2. Buscar productos por rango de precio.")
                print("3. Actualizar precio de un producto.")
                print("4. Salir")
                opcion=input("Escoje una opcion: ")
                
                if opcion=="1":
                elif opcion=="2":
                elif opcion=="3":
                elif opcion=="4":
                        break
menu()