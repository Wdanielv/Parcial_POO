import sqlite3 #Importamos SQLite
from sqlite3 import Error #De SQLite se importa Error

def conexionBD():
    try:
        con = sqlite3.connect('BDEjam.db')
        #establece el objeto conexion y crea contenedor de la BD
        return con #retorna la conexion
    except Error: 
        print(Error)
        #si hay error lo imprime

def cerrarConexionBD(con):
    con.close()
    print("\nConexion con la BD cerrada exitosamente")
    #cierra la conexion con la BD 

#MODULO PRODUCTOS

def crearTablaProductos(con):
    try:
        cursorObj = con.cursor()
        #recorre la BD con el objeto conexion
        crearTablaProd = '''CREATE TABLE IF NOT EXISTS productos(
        noIdProducto INTEGER NOT NULL,
        nomProducto TEXT NOT NULL,
        medida REAL NOT NULL,
        fecVencimiento DATE NOT NULL,
        precioCpra REAL NOT NULL,
        precioVta REAL NOT NULL,
        PRIMARY KEY(noIdProducto))'''
        cursorObj.execute(crearTablaProd)
        #Se crea la tabla productos mediante la variable crearTablaProd y se ejecuta
        con.commit()
        #Se asegura la persistencia de la tabla
    except Error:
        print(Error)
    
def leerProducto(con): 
    noIdProducto = int(input('\n  Ingrese un número entero que será\n  el número único de Identificación del producto: '))
    #noIdProducto = noIdProducto.rjust(12)
    nomProducto = input('\n  Ingrese el Nombre del producto: ')
    nomProducto = nomProducto.rjust(12)
    medida = float(input('\n  Medidas del producto: '))
    #medida = medida.rjust(12)
    fecVencimiento = input('\n  Ingrese la Fecha de vencimiento del\n  producto, sólo en este formato (AAAA-MM-DD): ')
    fecVencimiento = fecVencimiento.rjust(12)
    precioCpra = float(input('\n  Igrese el Precio de compra del producto\n  (utilize el punto sólo para indicar centavos): '))
    #precioCpra = precioCpra.rjust(12)
    precioVta = float(input('\n  Ingrese el Precio de venta del producto\n  (utilize el punto sólo para indicar centavos): '))
    #precioVta = precioVta.rjust(12)
    # Devolvemos la información del producto como una tupla
    miproducto = (noIdProducto, nomProducto, medida, fecVencimiento, precioCpra, precioVta)
    return miproducto

def crearProducto(con):
    try:
        cursorObj = con.cursor()
        #se crea el objeto cursor
        miproducto = leerProducto(con)
        crearProd='''INSERT INTO productos(noIdProducto,nomProducto,medida,fecVencimiento,precioCpra,precioVta)
        VALUES(?,?,?,?,?,?)'''
        cursorObj.execute(crearProd,miproducto)
        #Se crea la tabla productos y se ejecuta
        con.commit()
        #Se asegura la persistencia
        print('\nProducto creado con exito')
    except Error:
        print(Error)

def actualizarProducto(con):
    try:
        cursorObj=con.cursor()
        #se crea el objeto cursor
        idProd=input("\n  Ingrese el número de identificación\n  del producto que quiere cambiar: ")
        parametroProd=input("\n  Ingrese el parametro que quiere cambiar\n\n  las opciones son:\n\n  'nomProducto'\n  'medida' (debe ser un número)\n  'fecVencimiento'\n  'precioCpra' (debe ser un número, use el punto sólo para indicar centavos)\n  'precioVta' (debe ser un número, use el punto sólo para indicar centavos)\n  Ingrese sólo los parámetros válidos señalados en comillas, sin usar las comillas: ")
        actualizacion=input("\n  Ingrese nuevo valor de acuerdo a las indicaciones anteriores: ")
        #ingresa el producto a actualizar
        actuProd='UPDATE productos SET '+parametroProd+'="'+actualizacion+'" WHERE noIdProducto='+idProd
        actuProd=actuProd.rjust(12)
        #print("la cadena que se ejecuta es: ",actuProd)
        cursorObj.execute(actuProd)
        #se ejecuta la actualizacion
        con.commit()
        #se asegura la persistencia de la actualizacion
        print("\n  Producto actualizado con exito")
    except Error:
        print(Error)

def consultarProducto(con, id_producto):
    try:
        cursorObj = con.cursor()

        id_producto = int(id_producto)

        # Ejecuta una consulta SQL para seleccionar un producto específico por su ID
        cursorObj.execute("SELECT * FROM productos WHERE noIdProducto = ?", (id_producto,))
        
        # Recupera el resultado
        producto = cursorObj.fetchone()

        if producto:
            # Si se encontró el producto, imprime sus detalles
            print(f"\nInformación del Producto con número de identificación {id_producto}:")
            print(f"\n  Nombre: {producto[1]}")
            print(f"  Medida: {producto[2]}")
            print(f"  Fecha de Vencimiento: {producto[3]}")
            print(f"  Precio de Compra: {producto[4]}")
            print(f"  Precio de Venta: {producto[5]}\n")
        else:
            print(f"\nNo se encontró un producto con número de identificación {id_producto}.")
    except Error:
        print(Error)

#MODULO CLIENTES

def crearTablaClientes(con):
    try:
        cursorObj = con.cursor()
        #recorre la BD con el objeto conexion
        crearTablaCli='''CREATE TABLE IF NOT EXISTS clientes(
        noIdCliente interger NOT NULL,
        nombreCliente text NOT NULL,
        apellidoCliente text NOT NULL,
        dirrecionCliente text NOT NULL,
        telefonoCliente text NOT NULL,
        emailCliente text NOT NULL,
        PRIMARY KEY(noIdCliente))'''
        cursorObj.execute(crearTablaCli)
        #Se crea la tabla clientes mediante la variable crearTablaCli y se ejecuta
        con.commit()
        #Se asegura la persistencia de la tabla
    except Error:
        print(Error)

def leerCliente(con): 
    noIdCliente = int(input('\n  Ingrese un número entero que será\n  el número único de Identificación del cliente: '))
    #noIdCliente = noIdCliente.rjust(12)
    nombreCliente = input('\n  Ingrese los Nombres del cliente: ')
    nombreCliente = nombreCliente.rjust(12)
    apellidoCliente = input('\n  Ingrese los Apellidos del cliente: ')
    apellidoCliente = apellidoCliente.rjust(12)
    dirrecionCliente = input('\n  Ingrese la Dirreción del cliente: ')
    dirrecionCliente = dirrecionCliente.rjust(12)
    telefonoCliente = input('\n  Ingrese el Teléfono del cliente: ')
    telefonoCliente = telefonoCliente.rjust(12)
    emailCliente = input('\n  Ingrese el Email del cliente: ')
    emailCliente = emailCliente.rjust(12)
    # Devolvemos la información del cliente como una tupla
    micliente = (noIdCliente, nombreCliente, apellidoCliente, dirrecionCliente, telefonoCliente, emailCliente)
    return micliente

def crearCliente(con):
    try:
        cursorObj = con.cursor()
        #se crea el objeto cursor
        micliente = leerCliente(con)
        crearCli='''INSERT INTO clientes(noIdCliente,nombreCliente,apellidoCliente,dirrecionCliente,telefonoCliente,emailCliente)
        VALUES(?,?,?,?,?,?)'''
        cursorObj.execute(crearCli,micliente)
        #Se crea el cliente nuevo en la tabla clientes y se ejecuta
        con.commit()
        #Se asegura la persistencia del cliente nuevo
        print('\n  Cliente creado con exito')
    except Error:
        print(Error)

def actualizarCliente(con):
    try:
        cursorObj=con.cursor()
        #se crea el objeto cursor
        idCli=input("\n  Ingrese el número de identificación\n  del cliente que quiere cambiar: ")
        parametroCli=input("\n  Ingrese el parametro que quiere cambiar\n\n  las opciones son:\n\n  'nombreCliente'\n  'apellidoCliente'\n  'dirrecionCliente'\n  'telefonoCliente'\n  'emailCliente'\n  Ingrese sólo los parámetros válidos señalados en comillas, sin usar las comillas: ")
        actualizacion=input("\n  Ingrese nuevo valor de acuerdo a las indicaciones anteriores: ")
        #ingresa el cliente a actualizar
        actuCli='UPDATE clientes SET '+parametroCli+'="'+actualizacion+'" WHERE noIdCliente='+idCli
        actuCli=actuCli.rjust(12)
        #print("la cadena que se ejecuta es: ",actuCli)
        cursorObj.execute(actuCli)
        #se ejecuta la actualizacion
        con.commit()
        #se asegura la persistencia de la actualizacion
        print("\n  Cliente actualizado con exito")
    except Error:
        print(Error)

def consultarCliente(con, id_cliente):
    try:
        cursorObj = con.cursor()

        id_cliente = int(id_cliente)

        # Ejecuta una consulta SQL para seleccionar un cliente específico por su ID
        cursorObj.execute("SELECT * FROM clientes WHERE noIdCliente = ?", (id_cliente,))
        
        # Recupera el resultado
        cliente = cursorObj.fetchone()

        if cliente:
            # Si se encontró el cliente, imprime sus detalles
            print(f"\nInformación del Cliente con número de identificación {id_cliente}:")
            print(f"\n  Nombres: {cliente[1]}")
            print(f"  Apellidos: {cliente[2]}")
            print(f"  Dirreción: {cliente[3]}")
            print(f"  Teléfono: {cliente[4]}")
            print(f"  Email: {cliente[5]}\n")
        else:
            print(f"\nNo se encontró un cliente con número de identificación {id_cliente}.")
    except Error:
        print(Error)

#MODULO VENTAS

def crearTablaVentas(con):
    try:
        cursorObj = con.cursor()
        crearTablaVent = '''CREATE TABLE IF NOT EXISTS ventas(
        noFactura INTEGER NOT NULL,
        noIdCliente INTEGER NOT NULL,
        noIdProducto INTEGER NOT NULL,
        cantidadProducto INTEGER NOT NULL,
        PRIMARY KEY(noFactura))'''
        cursorObj.execute(crearTablaVent)
        con.commit()
    except Error:
        print(Error)

def crearVenta(con):
    try:
        cursorObj = con.cursor()

        noFactura = int(input("\nIngrese el número de factura: "))
        noIdCliente = int(input("Ingrese la identificación del cliente: "))
        noIdProducto = int(input("Ingrese la identificación del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        venta = (noFactura, noIdProducto, noIdCliente, cantidad)
        cursorObj.execute("INSERT INTO ventas(noFactura, noIdProducto, noIdCliente, cantidadProducto) VALUES(?,?,?,?)", venta)

        con.commit()

        print("\nVenta realizada con éxito.")
    except Error:
        print(Error)

def actualizarVenta(con):
    try:
        cursorObj = con.cursor()

        noFactura = int(input("\nIngrese el número de factura que desea actualizar: "))
        parametro = input("\nIngrese el parámetro que desea cambiar (noIdCliente, noIdProducto, cantidadProducto): ")
        nuevo_valor = input("\nIngrese el nuevo valor: ")

        actualizacion = f"UPDATE ventas SET {parametro} = ? WHERE noFactura = {noFactura}"
        cursorObj.execute(actualizacion, (nuevo_valor,))

        con.commit()

        print("\nVenta actualizada con éxito.")
    except Error:
        print(Error)

#MODULO FACTURAS

# Módulo Ventas y Facturación

def vender_producto(con):
    noFactura = int(input("\nIngrese el número de factura: "))
    noIdCliente = int(input("Ingrese la identificación del cliente: "))
    noIdProducto = int(input("Ingrese la identificación del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))

    cursorObj = con.cursor()
    venta = (noFactura, noIdProducto, noIdCliente, cantidad)
    cursorObj.execute("INSERT INTO ventas(noFactura, noIdProducto, noIdCliente, cantidadProducto) VALUES(?,?,?,?)", venta)
    con.commit()

    print("\nVenta realizada con éxito.")

def obtener_informacion_venta(con, noFactura):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT noIdCliente, noIdProducto, cantidadProducto FROM ventas WHERE noFactura = ?", (noFactura,))
    venta = cursorObj.fetchone()
    return venta

def imprimir_factura(con, noFactura):
    cursorObj = con.cursor()

    venta = obtener_informacion_venta(con, noFactura)

    if not venta:
        print(f"\nNo se encontró una venta con número de factura {noFactura}.")
        return

    noIdCliente, noIdProducto, cantidad = venta

    cursorObj.execute("SELECT nombreCliente, apellidoCliente, dirrecionCliente, telefonoCliente, emailCliente FROM clientes WHERE noIdCliente = ?", (noIdCliente,))
    cliente = cursorObj.fetchone()

    cursorObj.execute("SELECT nomProducto, precioVta FROM productos WHERE noIdProducto = ?", (noIdProducto,))
    producto = cursorObj.fetchone()

    if not cliente or not producto:
        print("\nNo se encontró información completa para imprimir la factura.")
        return

    nombreCliente, apellidoCliente, dirrecionCliente, telefonoCliente, emailCliente = cliente
    nomProducto, precioVta = producto

    print("\n***** Factura *****")
    print(f"Número de factura: {noFactura}")
    print(f"Nombre del cliente: {nombreCliente}")
    print(f"Apellido del cliente: {apellidoCliente}")
    print(f"Dirección del cliente: {dirrecionCliente}")
    print(f"Teléfono del cliente: {telefonoCliente}")
    #print(f"Email del cliente: {emailCliente}")
    print("\nDetalle de la factura:")
    print(f"Producto: {nomProducto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: {precioVta}")
    print(f"Precio total: {cantidad * precioVta}")

#PRESENTACION Y MENÚS

def presentacion():
    print("\n\n\n***************************************************************")
    print("\n                          Sistema de Gestión\n\n                       Tienda de Barrio LA MEJOR")
    print("\n***************************************************************")
    print("\nEste sistema permite gestionar ventas, imprimir facturas,")
    print("gestionar clientes y productos.")
    input("\nPresione Enter para empezar...")
    # Presentación del sistema

def menu_principal(con):
    con=conexionBD()
    #abre la conexion con la BD
    while True:
        print("\nMenú Principal:")
        print("\n 1. Gestionar Ventas")
        print(" 2. Imprimir Facturas")
        print(" 3. Gestionar Clientes")
        print(" 4. Gestionar Productos")
        print(" 5. Salir")
        
        opcion = input("\nSeleccione una opción (1/2/3/4/5): ")
        
        if opcion == "1":
            menu_ventas(con)
            #abre el menu de ventas
        elif opcion == "2":
            menu_facturas(con)
            #abre el menu facturacion
        elif opcion == "3":
            menu_clientes(con)
            #abre el menu clientes
        elif opcion == "4":
            menu_productos(con)
            #abre el menu productos
        elif opcion == "5":
            cerrarConexionBD(con)
            #cierra la conexion con la BD
            print("\n***************************************************************")
            print("\nGracias por usar el sistema. ¡Hasta Pronto!\n")
            print("\n***************************************************************\n\n")
            #despedida
            return False
            #termina el programa     
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")
            input("\nPresione Enter para continuar...")

def menu_ventas(con):
    while True:
        print("\nMenú Ventas:")
        print("\n 1. Iniciar Venta")
        print(" 2. Modificar Venta")
        print(" 3. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1/2/3):")

        if opcion == "1":
            crearVenta(con)
        elif opcion == "2":
            actualizarVenta(con)
        elif opcion == "3":
            print("\nVolviendo al Menú Principal...")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")
            input("\nPresione Enter para continuar...")


# Menú Facturación

def menu_facturas(con):
    while True:
        print("\nMenú Facturación:")
        print("\n 1. Imprimir Factura")
        print(" 2. Enviar Factura vía Correo Electrónico")
        print(" 3. Volver al Menú Principal")

        opcion = input("\nSeleccione una opción (1/2/3):")

        if opcion == "1":
            noFactura = int(input("\nIngrese el número de factura que desea imprimir: "))
            imprimir_factura(con, noFactura)
        elif opcion == "2":
            print("\nEstamos trabajando en la opción de enviar factura por correo electrónico.")
            input("\nPresione Enter para volver al Menú Facturación...")
        elif opcion == "3":
            print("\nVolviendo al Menú Principal...")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")
            input("\nPresione Enter para continuar...")



def menu_clientes(con):
    con=conexionBD()
    while True:
        print("\nMenú de Clientes:")
        print("\n 1. Crear Cliente")
        print(" 2. Actualizar Cliente")
        print(" 3. Consultar Cliente")
        print(" 4. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (1/2/3/4): ")
        
        if opcion == "1":
            # llama el método para crear un cliente
            crearCliente(con)
        elif opcion == "2":
            # llama el método para actualizar un cliente
            actualizarCliente(con)
        elif opcion == "3":
            # llama el método para consultar un cliente
            consultarCliente(con, id_cliente = input("\n  Ingrese el número de identificación\n  del cliente que quiere consultar: "))
        elif opcion == "4":
            print("\nVolviendo al Menú Principal...")
            menu_principal(con)
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")
            input("\nPresione Enter para continuar...")   

def menu_productos(con):
    con=conexionBD()
    while True:
        print("\nMenú de Productos:")
        print("\n 1. Crear Producto")
        print(" 2. Actualizar Producto")
        print(" 3. Consultar Producto")
        print(" 4. Volver al Menú Principal")
        
        opcion = input("\nSeleccione una opción (1/2/3/4): ")
        
        if opcion == "1":
            # llama el método para crear un producto
            crearProducto(con)
        elif opcion == "2":
            # llama el método para actualizar un producto
            actualizarProducto(con)
        elif opcion == "3":
            # llama el método para consultar un producto
            consultarProducto(con, id_producto = input("\n  Ingrese el número de identificación\n  del producto que quiere consultar: "))
        elif opcion == "4":
            print("\nVolviendo al Menú Principal...")
            menu_principal(con)
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")
            input("\nPresione Enter para continuar...")


#PROGRAMA PRINCIPAL

def main():
    con = conexionBD()
    crearTablaProductos(con)
    crearTablaClientes(con)
    crearTablaVentas(con)
    presentacion()
    menu_principal(con)

main() #Ejecuta el programa principal
