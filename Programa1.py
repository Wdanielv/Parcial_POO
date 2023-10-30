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
    
def crearProducto(con,miproducto):
    cursorObj=con.cursor()
    #crear el primer producto
    crearProd='INSERT INTO productos VALUES(?,?,?,?,?,?)'
    print("la cadena que se ejecuta es: ",crearProd)
    cursorObj.execute(crearProd,miproducto)
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

def crearCliente(con,miCliente):
    cursorObj=con.cursor()
    #crear el primer producto
    crearClie='INSERT INTO clientes VALUES(?,?,?,?,?,?)'
    print("la cadena que se ejecuta es: ",crearClie)
    cursorObj.execute(crearClie,miCliente)
    con.commit()

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
    
def actualizarCliente(con):
    cursorObj=con.cursor()
    #actualizar el primer producto
    actuclie='''UPDATE productos SET nomProducto="Chetos" WHERE noIdProducto in (2,3) '''
    print("la cadena que se ejecuta es: ",actuClie)
    cursorObj.execute(actuClie)
    con.commit()

def actualizarnoIdCliente(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoVa=input(" Nuevo ID cliente: ")
    acidCl='UPDATE clientes SET noIdCliente="'+nuevoVa+'" WHERE noIdCliente="'+valor+'"'
    acidCl=acidCl.rjust(12)
    cursorObj.execute(acidCl)
    con.commit()
    print ("            ID Cliente Actualizado")
    return(valor)
    #dfghgfdsdfghgfd

def actualizarnomCliente(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoEv=input(" Nuevo Nombre del cliente: ")
    acnomCl='UPDATE clientes SET nomCliente="'+nuevoEv+'" WHERE noIdCliente="'+valor+'"'
    acnomCl=acnomCl.rjust(12)
    cursorObj.execute(acnomCl)
    con.commit()
    print ("            Nombre del cliente Actualizado")

def actualizarapeCliente(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoEv=input(" Nuevo Apellido del cliente")
    acApCl='UPDATE clientes SET apeCliente="'+nuevoEv+'" WHERE noIdCliente="'+valor+'"'
    acApCl=acApCl.rjust(12)
    cursorObj.execute(acApCl)
    con.commit()
    print ("            Apellido Cliente Actualizado")

def actualizardireccion(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoEv=input(" Nueva Direccion del Cliente: ")
    direc='UPDATE clientes SET direccion="'+nuevoEv+'" WHERE noIdCliente="'+valor+'"'
    cursorObj.execute(direc)
    con.commit()
    print ("      Direccion del cliente Actualizado")

def actualizartelefono(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoEv=input(" Nuevo telefono Cliente: ")
    telefono='UPDATE clientes SET telefono="'+nuevoEv+'" WHERE noIdCliente="'+valor+'"'
    cursorObj.execute(telefono)
    con.commit()
    print ("            telefono Cliente Actualizado")

def actualizaremailCliente(con):
    cursorObj=con.cursor()
    valor=input("no Id cliente: ")
    filas=cursorObj.fetchall()
    nuevoEv=input(" Nuevo emailCliente: ")
    emailCl='UPDATE clientes SET emailCliente="'+nuevoEv+'" WHERE noIdCliente="'+valor+'"'
    cursorObj.execute(emailCl)
    con.commit()
    print ("            emailCliente Actualizado")

def consultarCliente(con):
    cursorObj=con.cursor()
    valor=input("noIdcliente: ")
    cad='SELECT  * FROM clientes WHERE noIdCliente="'+valor+'"'
    print("La cadena es:  ",cad)
    cursorObj.execute(cad)#Consultar inf en la tabla atleta
    filas=cursorObj.fetchall()
    print ("El tipo de datos de filas es: ", type(filas))
    for row in filas:
        IdCliente=row[0]
        nomCliente=row[1]
        print("La informacion del id del cliente es: ",IdCliente)
        print("La informacion del nombre del cliente es: ",nomCliente)      
    print(row)        
    #actualizamos el producto en la base de datos

def crearTablaVentas(con):
    cursorObj = con.cursor()
    # Se crea el objeto cursor
    crearTablaVentas = '''CREATE TABLE IF NOT EXISTS ventas(
        noFactura INTEGER PRIMARY KEY AUTOINCREMENT,
        noIdCliente INTEGER NOT NULL,
        noIdProducto INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precioTotal REAL NOT NULL,
        FOREIGN KEY (noIdCliente) REFERENCES clientes (noIdCliente),
        FOREIGN KEY (noIdProducto) REFERENCES productos (noIdProducto))'''
    cursorObj.execute(crearTablaVentas)
    # Se crea la tabla ventas y se ejecuta
    con.commit()

def crearVenta(con,miCliente):
    cursorObj=con.cursor()
    #crear el primer producto
    crearClie='INSERT INTO clientes VALUES(?,?,?,?,?,?)'
    print("la cadena que se ejecuta es: ",crearClie)
    cursorObj.execute(crearClie,miCliente)
    con.commit()

def venderProducto(con):
    cursorObj = con.cursor()
    
    # Solicitar información de la venta
    noIdCliente = input("Identificación del cliente: ")
    noIdProducto = input("Identificación del producto: ")
    cantidad = int(input("Cantidad a vender: "))
    
    # Consultar el producto en la base de datos
    cursorObj.execute('SELECT nomProducto, precioVta FROM productos WHERE noIdProducto = ?', (noIdProducto,))
    producto = cursorObj.fetchone()
    
    if producto:
        nomProducto, precioVta = producto
        precioTotal = precioVta * cantidad
        
        # Registrar la venta en la base de datos
        cursorObj.execute
        ('INSERT INTO ventas (noIdCliente, noIdProducto, cantidad, precioTotal)) (VALUES (?, ?, ?, ?)', (noIdCliente, noIdProducto, cantidad, precioTotal)
        con.commit()
        
        print("Venta realizada con éxito.")
    else:
        print("Producto no encontrado en la base de datos.")

def quitarProducto(con):
    cursorObj = con.cursor()
    
    # Solicitar información de la devolución
    noIdCliente = input("Identificación del cliente: ")
    noIdProducto = input("Identificación del producto: ")
    cantidad = int(input("Cantidad a devolver: "))
    
    # Consultar la venta en la base de datos
    cursorObj.execute('SELECT cantidad, precioTotal FROM ventas WHERE noIdCliente = ? AND noIdProducto = ?',
                      (noIdCliente, noIdProducto))
    venta = cursorObj.fetchone()
    
    if venta:
        ventaCantidad, precioTotal = venta
        if cantidad <= ventaCantidad:
            nuevoPrecioTotal = precioTotal * (1 - cantidad / ventaCantidad)
            cursorObj.execute('UPDATE ventas SET cantidad = ?, precioTotal = ? WHERE noIdCliente = ? AND noIdProducto = ?',
                              (ventaCantidad - cantidad, nuevoPrecioTotal, noIdCliente, noIdProducto))
            con.commit()
            print("Devolución realizada con éxito.")
        else:
            print("La cantidad a devolver es mayor que la cantidad vendida.")
    else:
        print("Venta no encontrada en la base de datos.")

def imprimirFactura(con, numFactura):
    cursorObj = con.cursor()
    
    # Obtener información de la factura
    cursorObj.execute('SELECT ventas.noIdCliente, clientes.nomCliente, clientes.apellCliente, clientes.direccion, clientes.telefono, ventas.noIdProducto, productos.nomProducto, ventas.cantidad, productos.precioVta, ventas.precioTotal FROM ventas JOIN clientes ON ventas.noIdCliente = clientes.noIdCliente JOIN productos ON ventas.noIdProducto = productos.noIdProducto WHERE ventas.noFactura = ?',
                      (numFactura,))
    facturaInfo = cursorObj.fetchall()
    
    if facturaInfo:
        # Imprimir encabezado
        noIdCliente, nomCliente, apellCliente, direccion, telefono = facturaInfo[0][:5]
        print(f"Número de Factura: {numFactura}")
        print(f"Nombre del Cliente: {nomCliente} {apellCliente}")
        print(f"Dirección del Cliente: {direccion}")
        print(f"Teléfono del Cliente: {telefono}")
        
        # Imprimir cuerpo de la factura
        print("\nCuerpo de la Factura:")
        totalFactura = 0
        for row in facturaInfo:
            noIdProducto, nomProducto, cantidad, precioUnitario, precioTotal = row[5:]
            print(f"{nomProducto} - Cantidad: {cantidad} - Precio Unitario: {precioUnitario} - Precio Total: {precioTotal}")
            totalFactura += precioTotal
        
        # Imprimir pie final
        print("\nTotal a pagar: ", totalFactura)
    else:
        print(f"No se encontró la factura con el número {numFactura}.")

# Modifica tu función main para incluir la venta y la impresión de facturas

def main():
    miCon = conexionBD()
    crearTablaProducto(miCon)
    crearTablaCliente(miCon)
    crearTablaVentas(miCon)  # Agrega una tabla 'ventas' para registrar las ventas
    numFactura = 1  # Número de factura (puedes implementar la generación automática)
    
    while True:
        print("\nMenú:")
        print("1. Vender producto")
        print("2. Quitar producto (devolución)")
        print("3. Imprimir factura")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            venderProducto(miCon)
        elif opcion == "2":
            quitarProducto(miCon)
        elif opcion == "3":
            numFactura = int(input("Ingrese el número de factura a imprimir: "))
            imprimirFactura(miCon, numFactura)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")
    
def main():
    miCon=conexionBD()
    crearTablaProducto(miCon)
    crearTablaCliente(miCon)
    crearTablaVentas(miCon)
    #productoLeido=leerProducto(miCon)
    #crearProducto(miCon,productoLeido)
    #actualizarProducto(miCon)
    #consultarProducto(miCon)
    #borrarProducto(miCon)
    #borrarTablaProducto(miCon)    
    #clienteLeido=leerCliente(miCon)
    #crearCliente(miCon,clienteLeido)
    #actualizarnoIdCliente(miCon)
    #actualizarnomCliente(miCon)
    #actualizarapeCliente(miCon)
    #actualizardireccion(miCon)
    #actualizartelefono(miCon)
    #actualizaremailCliente(miCon)
    #consultarCliente(miCon)
    cerrarConexionBD(miCon)
    
main()
