import sqlite3 #Importamos SQLite
from sqlite3 import Error #De SQLite se importa Error

def conexionBD():
    try:
        con = sqlite3.connect('BDEjam.db')
        #se establece conexion
        # se crea contenedor
        return con
    except Error:
        print(Error)
def cerrarConexionBD(con):
    con.close()
    #Se cierra la conexion con la base de datos   
def crearTablaProducto(con):
    cursorObj=con.cursor()
    #Se crea el objeto cursor
    crearTablaProd='''CREATE TABLE IF NOT EXISTS productos(
        noIdProducto interger NOT NULL,
        nomProducto text NOT NULL,
        medida float NOT NULL,
        fecVencimiento date NOT NULL,
        precioCpra float NOT NULL,
        precioVta float NOT NULL,
        PRIMARY KEY(noIdProducto))'''
    cursorObj.execute(crearTablaProd)
    #Se crea la tabla productos y se ejecuta
    con.commit()
    #Se asegura la persistencia
def crearTablaCliente(con):
    cursorObj=con.cursor()
    #Se crea el objeto cursor
    crearTablaCli='''CREATE TABLE IF NOT EXISTS clientes(
        noIdCliente interger NOT NULL,
        nomCliente text NOT NULL,
        apellCliente text NOT NULL,
        direccion text NOT NULL,
        telefono interger NOT NULL,
        emailCliente text NOT NULL,
        PRIMARY KEY(noIdCliente))'''
    cursorObj.execute(crearTablaCli)
    #Se crea la tabla clientes y se ejecuta
    con.commit()
    #Se asegura la persistencia
def leerProducto(con):
    noIdProducto=input('Identificacion del producto:')
    noIdProducto=noIdProducto.rjust(12)
    nomProducto=input('Nombre del producto:')
    nomProducto=nomProducto.rjust(12)
    medida=input('Medidas del producto: ')
    medida=medida.rjust(12)
    fecVencimiento= input('Fecha de vencimiento (AAAA-MM-DD): ')
    fecVencimiento=fecVencimiento.rjust(12)
    precioCpra=input('Precio de compra: ')
    precioCpra=precioCpra.rjust(12)
    precioVta=input('Precio de venta: ')
    precioVta=precioVta.rjust(12)
    producto=(noIdProducto,nomProducto,medida,fecVencimiento,precioCpra,precioVta)
    return producto
def leerCliente(con):
    noIdCliente=input('Identificacion del cliente:')
    noIdCliente=noIdCliente.rjust(12)
    nomCliente=input('Nombre del cliente:')
    nomCliente=nomCliente.rjust(12)
    apellCliente=input('Apellido del cliente: ')
    apellCliente=apellCliente.rjust(12)
    direccion= input('Direccion del cliente: ')
    direccion=direccion.rjust(12)
    telefono=input('Telefono del cliente')
    telefono=telefono.rjust(12)
    emailCliente=input('Correo electronico del cliente: ')
    emailCliente=emailCliente.rjust(12)
    cliente=(noIdCliente,nomCliente,apellCliente,direccion,telefono,emailCliente)
    return cliente
def crearProducto(con,miproducto):
    cursorObj=con.cursor()
    #crear el primer producto
    crearProd='INSERT INTO productos VALUES(?,?,?,?,?,?)'
    print("la cadena que se ejecuta es: ",crearProd)
    cursorObj.execute(crearProd,miproducto)
    con.commit()
def crearCliente(con,miCliente):
    cursorObj=con.cursor()
    #crear el primer producto
    crearClie='INSERT INTO clientes VALUES(?,?,?,?,?,?)'
    print("la cadena que se ejecuta es: ",crearClie)
    cursorObj.execute(crearClie,miCliente)
    con.commit()
def actualizarProducto(con):
    cursorObj=con.cursor()
    idProd=input("Ingrese el id del producto que quiere cambiar: ")
    parametroProd=input("Ingrese el parametro que quiera cambiar: ")
    actualizacion=input("Ingrese nuevo valor: ")
    #actualizar el primer producto
    actuProd='UPDATE productos SET '+parametroProd+'="'+actualizacion+'" WHERE noIdProducto='+idProd
    actuProd=actuProd.rjust(12)
    print("la cadena que se ejecuta es: ",actuProd)
    cursorObj.execute(actuProd)
    con.commit()
    #actualizamos el producto en la base de datos
def actualizarCliente(con):
    cursorObj=con.cursor()
    #actualizar el primer producto
    actuclie='''UPDATE productos SET nomProducto="Chetos" WHERE noIdProducto in (2,3) '''
    print("la cadena que se ejecuta es: ",actuClie)
    cursorObj.execute(actuClie)
    con.commit()
    #actualizamos el producto en la base de datos
def consultarProducto(con):
    cursorObj=con.cursor()
    #crear el primer producto
    noIdProd=input("Ingrese el numero de producto: ")
    #consultarProd='SELECT noIdProducto, nomProducto FROM productos WHERE noIdProducto= '+noIdProd
    #consultarProd='SELECT noIdProducto, nomProducto FROM productos'
    #consultarProd='SELECT * FROM productos'
    #consultarProd='SELECT count(*) FROM productos WHERE noIdProducto= '+noIdProd
    consultarProd='SELECT sum(noidproducto) FROM productos'
    print("la cadena que se ejecuta es: ",consultarProd)
    cursorObj.execute(consultarProd)
    filas=cursorObj.fetchall()
    print("el tipo de dato de filas: ",type(filas))
    suma=filas[0][0]
    print("El producto suma", suma)
    #if cantidad ==0:
    #    print("Lo sentimos, el producto no esta en la base de datos :(")
    #else:
    #    print("El producto esta ",cantidad," en la base de datos")
    #for row in filas:
    #   idProd=row[0]
    #   nomProd=row[1]
    #   print("La identificacion del producto es:",idProd)
    #   print("El nombre del producto es:",nomProd)
    #print("La fila",row)
def borrarProducto(con):
    cursorObj=con.cursor()
    noIdProd=input("Ingrese el numero de producto: ")
    borrarProd='DELETE FROM productos WHERE noIdProducto='+noIdProd
    print("la cadena que se ejecuta es: ",borrarProd)
    cursorObj.execute(borrarProd)
    con.commit()
def borrarTablaProducto(con):
    cursorObj=con.cursor()
    #recorremos la base de datos con el objeto de conexion
    borrar='''DROP TABLE productos'''
    cursorObj.execute(borrar)
    con.commit()

def main():
    miCon=conexionBD()
    crearTablaProducto(miCon)
    crearTablaCliente(miCon)
    #productoLeido=leerProducto(miCon)
    #crearProducto(miCon,productoLeido)
    #clienteLeido=leerCliente(miCon)
    #crearCliente(miCon,clienteLeido)

    actualizarProducto(miCon)
    #consultarProducto(miCon)
    #borrarProducto(miCon)
    #borrarTablaProducto(miCon)
    cerrarConexionBD(miCon)
    
main()
