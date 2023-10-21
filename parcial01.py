import sqlite3
from sqlite3 import Error
from datetime import datetime

class Evento:                               #se crea la clase Evento para agrupar variables y funciones relacionadas de un objeto   
    def __init__(self):
        self.__Numero_evento=None
        self.__Año=None
        self.__premio_primer_puesto=None
        self.__premio_segundo_puesto=None
        self.__premio_tercer_puesto=None
       
    def setNumero_evento(self):
        self.__Numero_evento = input("Numero de evento: ")
        #self.__Numero_evento=self.__Numero_evento.ljust(12)  #el numero es el campo al cual se va a ajustar
    def setAño(self):
        self.__Año = input("Años en que se realiza la Carrera: ")
        #self.__Año =self.__Año.ljust(12) 
    def setpremio_primer_puesto(self):
        self.__premio_primer_puesto = input("Valor del permio del primer puesto: ")
    def setpremio_segundo_puesto(self):
        self.__premio_segundo_puesto = input("Valor del permio del segundo puesto: ")
    def setpremio_tercer_puesto(self):
        self.__premio_tercer_puesto = input("Valor del permio del tercer puesto: ")
    def armarTupla(self):
        Evento=( self.__Numero_evento,self.__Año,self.__premio_primer_puesto,self.__premio_segundo_puesto,self.__premio_tercer_puesto)
        return Evento

    def insertarTablaEvento (self,con,miEvento):
        cursorObj=con.cursor() 
        #recorremos la base de datos con el objeto de conexion
        cad='''INSERT INTO Evento VALUES(?, ?, ?, ?, ?)
        '''
        cursorObj.execute(cad,miEvento)   #insertar informacion en la tabla carrera
        con.commit ()
        print("Ejecuto")

    def insertarTablaEvento2(self,con):
        cursorObj=con.cursor()
        #recorremos la base de datos con el objetivo de conexion
        Numero_evento =input("Numero de evento: ")
        #Numero_evento =Numero_evento.ljust(12)
        Año = input("Años en que se realiza la Carrera: ")
        #Año = Año.ljust(12)
        cad='INSERT INTO Evento VALUES ('+Numero_evento+','+año+',"NN","AP","2010-01-2:")'
        print("La cadena es:  ",cad)#Insertar inf en la tabla Carrera
        con.commit()
    
class Atleta:                             #se crea la clase Atleta para agrupar variables y funciones relacionadas de un objeto 
    def __init__(self):
        self.__noidAtleta=None
        self.__noInscripcion=None
        self.__nombre=None
        self.__apellido=None
        self.__fechaNacimiento=None
        self.__paisOrigen=None
        self.__ciudadOrigen=None

    def setnoidAtleta(self):
        self.__noidAtleta = input("Identificacion del Atleta ")
        #self.__noidAtleta=self.__noidAtleta.ljust(12)  #el numero es el campo al cual se va a ajustar
    def setnoInscripcion(self):
        self.__noInscripcion = input("Numero de Inscripcion ")
    def setnombre(self):
        self.__nombre = input("Nombre del Atleta: ")
    def setapellido(self):
        self.__apellido = input("Apellido del Atleta ")
    def setfechaNacimiento(self):
        FN = input("Fecha de Nacimiento del Atleta  (AAAA-MM-DD)" )
        self.__fechaNacimiento=datetime.strptime(FN,'%Y-%m-%d').date()
    def setpaisOrigen(self):
        self.__paisOrigen = input("Pais de Origen ")
    def setciudadOrigen(self):
        self.__ciudadOrigen = input("Ciudad de Origen ")
    def armarTupla(self):
        atleta=( self.__noidAtleta,self.__noInscripcion,self.__nombre,self.__apellido,self.__fechaNacimiento,self.__paisOrigen,self.__ciudadOrigen)
        return atleta   

    def insertarTablaAtleta(self,con,miAtleta):
        cursorObj=con.cursor()
        cad='''INSERT INTO ATLETA VALUES(?,?,?,?,?,?,?)'''
        cursorObj.execute(cad,miAtleta)
        con.commit()
        print(" Nuevo Atleta Creado")

    def insertarTablaAtleta2(self,con):
        cursorObj=con.cursor()
        noidAtleta = input("Identificacion del Atleta ")
        #noidAtleta=noidAtleta.ljust(12)  #el numero es ekl campo al cual se va a ajustar
        noInscripcion = input("Numero de Inscripcion ")
        cad='INSERT INTO ATLETA VALUES('+noidAtleta+','+noInscripcion+',"NN","AP","2010-01-23","COL","VILLAV")'
        print ("La cadena es ", cad)
        cursorObj.execute(cad)
        con.commit()

    def consultaTablaAtleta(self,con):
        cursorObj=con.cursor()
        #cad='SELECT noidAtleta, noInscripcion FROM atleta'
        #cad='SELECT * FROM atleta WHERE apellido LIKE "A%"'
        valor=input("No ID Atleta")
        cad='SELECT * FROM atleta WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(cad)
        filas=cursorObj.fetchall()
        for row in filas:
            idAtleta=row[0]
            inscripcion=row[1]
            nombre=row[2]
            apellido=row[3]
            fechaNacimiento=row[4]
            paisOrigen=row[5]
            ciudadOrigen=row[6]
            print("ID :                    ",idAtleta)
            print("Numero de inscripcion : ", inscripcion)
            print("NOMBRE :                ",nombre)
            print("APELLIDO :              ",apellido)
            print("FECHA DE NACIMIENTO :   ",fechaNacimiento)
            print("PAIS :                  ",paisOrigen)
            print("CIUDAD :                ",ciudadOrigen)
            

    def otroTipoConsulta(self,con):
        cursorObj=con.cursor()
        cad='SELECT count(*) FROM atleta'
        cursorObj.execute(cad)
        cantidadAtletas=cursorObj.fetchall()
        print("El tipo de dato de cantidad de atletas es: ",type(cantidadAtletas))
        for row in  cantidadAtletas:
            cantidad=row[0]
        print ("La cantidad de atletas en la base de datos es: ",cantidad)
        con.commit()

    def sumaColumna(self,con):
        cursorObj=con.cursor()
        cad='SELECT count(*) FROM atleta'
        cursorObj.execute(cad)
        cantidadAtletas=cursorObj.fetchall()
        print("El tipo de dato de cantidad de atletas es: ",type(cantidadAtletas))
        for row in  cantidadAtletas:
            cantidad=row[0]
        print ("La cantidad de atletas en la base de datos es: ",cantidad)
        cad='SELECT sum (noInscripcion) FROM atleta'
        cursorObj.execute(cad)
        sumaNoInscripcion=cursorObj.fetchall()
        for row in sumaNoInscripcion :
            cantidad=row[0]
        print ("La suma de  en la base de datos es: ",cantidad)
        con.commit()
        
        #rertytre
    def actualizarAtletaID(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nuevo ID Atleta")
        event='UPDATE atleta SET noidAtleta="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            ID Atleta Actualizado")
        return(valor)
        #dfghgfdsdfghgfd

    def actualizarAtletaInscripcion(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nuevo Numero Inscripcion Atleta")
        event='UPDATE atleta SET noInscripcion="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("             Numero Inscripcion Atleta Actualizado")

    def actualizarAtletaNombre(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nuevo Nombre Atleta")
        event='UPDATE atleta SET nombre="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            Nombre Atleta Actualizado")

    def actualizarAtletaApellido(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nuevo Apellido Atleta")
        event='UPDATE atleta SET apellido="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            Apellido Atleta Actualizado")

    def actualizarAtletaNac(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Fecha Nacimiento ID Atleta")
        event='UPDATE atleta SET fechaNacimiento="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            fecha Nacimiento Atleta Actualizado")

    def actualizarAtletaPais(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nuevo Pais Atleta")
        event='UPDATE atleta SET paisOrigen="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            Pais Atleta Actualizado")

    def actualizarAtletaCiudad(self,con):
        cursorObj=con.cursor()
        valor=input("No ID Atleta")
        filas=cursorObj.fetchall()
        nuevoEv=input(" Nueva Ciudad Atleta")
        event='UPDATE atleta SET ciudadOrigen="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
        cursorObj.execute(event)
        con.commit()
        print ("            ciudad Origen Atleta Actualizado")
        
        
    def actualizarTablaAtleta(self,con):
        cursorObj=con.cursor()
        cad='UPDATE atleta SET nombre="carlos" WHERE apellido="gil"'
        print (cad)
        cursorObj.execute(cad)
        con.commit()
        print("       Atleta Actualizado     ")
        

def creartablaCarrera(con):
    cursorObj=con.cursor()
    cad='''CREATE TABLE IF NOT EXISTS carrera(
    noEvento text NOT NULL,
    noidAtleta integer NOT NULL,
    PosicionAtleta text NOT NULL,
    Nombre text,
    Apellido text,
    tiempoEmpleado text, 
    EstadoAtleta text,
    PRIMARY KEY (noidAtleta,noEvento)
    )
    '''
    cursorObj.execute(cad)
    con.commit()

def actCarrera(con):
    cursorObj=con.cursor()
    valor=input("No ID del Atleta   ")
    cad='SELECT * FROM atleta WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for row in filas:
        idAtleta=row[0]
        NoEventoc="01"
        Posicion="01"
        nombrecar=row[2]
        apellidot=row[3]
        tiempo="00:00"
        EstadoAtleta="Activo"
        care=(NoEventoc,idAtleta,Posicion,nombrecar,apellidot,tiempo,EstadoAtleta)
    carr=care
    return carr

def consultaTablaCarreras(con):
    cursorObj=con.cursor()
    valor=input("ID Atleta")
    cad='SELECT * FROM carrera WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for row in filas:
        event=row[0]
        idatle=row[1]
        posicion=row[2]
        nombree=row[3]
        apellidoo=row[4]
        tiempo=row[5]
        estado=row[6]
        print("Evento numero :  ", event)
        print("Numero de ID :   ", idatle)
        print("Posicion :       ", posicion)
        print("NOMBRE :         ", nombree)
        print("APELLIDO :       ", apellidoo)
        print("TIEMPO :         ", tiempo)
        print("ESTADO :         ", estado)
    
def consultarCarreraInscripcion(con,infoCarrera):
    cursorObj=con.cursor()
    info='''INSERT INTO carrera VALUES(?,?,?,?,?,?,?)'''
    cursorObj.execute(info,infoCarrera)
    print("                        Atleta en Carrera Creado")
    con.commit()


def actualizarCarreraEvento(con):
    cursorObj=con.cursor()
    valor=input("No ID Atleta")
    filas=cursorObj.fetchall()
    nuevoEv=input("Numero Evento a Modificar")
    event='UPDATE carrera SET noEvento="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(event)
    con.commit()
    print ("             Numero Evento Actualizado")

def actualizarCarreraTiempo(con):
    cursorObj=con.cursor()
    valor=input("No ID Atleta")
    filas=cursorObj.fetchall()
    nuevoEv=input("Tiempo Atleta a Modificar")
    event='UPDATE carrera SET tiempoEmpleado="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(event)
    con.commit()
    print ("            Tiempo Atleta Actualizado")


def actualizarCarreraPosicion(con):
    cursorObj=con.cursor()
    valor=input("No ID Atleta")
    filas=cursorObj.fetchall()
    nuevoEv=input("Posicion Atleta a Modificar")
    event='UPDATE carrera SET PosicionAtleta="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(event)
    con.commit()
    print ("           Posicion Atleta Actualizado")


def actualizarCarreraEstado(con):
    cursorObj=con.cursor()
    valor=input("No ID Atleta")
    filas=cursorObj.fetchall()
    nuevoEv=input("Estado Atleta a Modificar")
    event='UPDATE carrera SET EstadoAtleta="'+nuevoEv+'" WHERE noidAtleta="'+valor+'"'
    cursorObj.execute(event)
    con.commit()
    print ("           Estado Atleta Actualizado")

    
def borrarInfoCarrera(con):
    cursorObj=con.cursor()
    EstadoAtleta=input("Ciudad: ")
    cad='DELETE FROM carrera WHERE EstadoAtleta LIKE "'+EstadoAtleta+'%"'
    print (cad)
    cursorObj.execute(cad)
    con.commit()
    print("Borrar info Tabla")

def borrarTablaCarrera(con):
    cursorObj=con.cursor()
    cad='DROP TABLE resultado'
    print (cad)
    cursorObj.execute(cad)
    con.commit()
    print("Borrar Tabla de Carrera")


def creartablaResultados(con):
    cursorObj=con.cursor()
    cad='''CREATE TABLE IF NOT EXISTS resultado(
    noInscripcion text NOT NULL,
    Nombre text,
    Apellido text,
    Fecha Nacimiento text,
    Pais Origen text,
    ciudad de Origen text,
    tiempoEmpleado text, 
    PRIMARY KEY (noInscripcion)
    )
    '''
    cursorObj.execute(cad)
    con.commit()

def actResultado(con):
    cursorObj=con.cursor()
    valor=input("No Inscripcion del Atleta a consultar  ")
    cad='SELECT * FROM atleta WHERE noInscripcion="'+valor+'"'
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for row in filas:
        noInscripcion=row[1]
        Nombre=row[2]
        Apellido=row[3]
        fecha=row[4]
        PaisOrigen=row[5]
        ciudaddeOrigen=row[6]
        
    cada='SELECT * FROM carrera WHERE Nombre="'+Nombre+'"'
    cursorObj.execute(cada)
    filass=cursorObj.fetchall()
    for row in filass:
        tiempo=row[5]
    care=(noInscripcion,Nombre,Apellido,fecha,PaisOrigen,ciudaddeOrigen,tiempo)
    carr=care
    return carr

def consultaTablaResultado(con):
    cursorObj=con.cursor()
    valor=input("Numero Incripcion")
    cad='SELECT * FROM resultado WHERE noInscripcion="'+valor+'"'
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for row in filas:
        event=row[0]
        nombree=row[1]
        apellidoo=row[2]
        fechaa=row[3]
        paisOrigen=row[4]
        ciudadOrigen=row[5]
        tiempo=row[6]
        print("noInscripcion :      ", event)
        print("NOMBRE :             ", nombree)
        print("APELLIDO :           ", apellidoo)
        print("fecha de Nacimiento :", fechaa)
        print("Pais de Origen :     ", apellidoo)
        print("ciudad de Origen :   ", ciudadOrigen)
        print("Tiempo    :          ", tiempo)
    
def consultarCarreraResultado(con,infoCarrera):
    cursorObj=con.cursor()
    info='''INSERT INTO resultado VALUES(?,?,?,?,?,?,?)'''
    cursorObj.execute(info,infoCarrera)
    print("                       resultado Atleta")
    con.commit()
    
class clasificacion:
    def __init__(self, con):
        self.con = con

    def ordenar_clasificacion(self, campo, orden):
        cursor = self.con.cursor()
        cursor.execute(f'SELECT * FROM clasificacionfinalyess ORDER BY {campo} {orden}')
        return cursor.fetchall()

    def actualizar_clasificacion(self):
        campoCreado = input("Ingrese el campo por el que desea ordenar la clasificación: ")
        ordenCreado = input("Ingrese el orden en el que desea ordenar la clasificación (ASC o DESC): ")

        cursor = self.con.cursor()

        cursor.execute(
            'SELECT noInscripcion, nombre, apellido, fechaNacimiento, paisOrigen, ciudadOrigen FROM atleta'
        )
        atleta_rows = cursor.fetchall()

        cursor.execute(
            'SELECT tiempoEmpleado FROM carrera'
        )
        carrera_rows = cursor.fetchall()

        rows = []

        min_rows = min(len(atleta_rows), len(carrera_rows))
        for i in range(min_rows):
            atleta_data = atleta_rows[i]
            carrera_data = carrera_rows[i]
            row = atleta_data + carrera_data
            rows.append(row)

        field_index = {
            'noInscripcion': 0,
            'nombre': 1,
            'apellido': 2,
            'FechaNacimiento': 3,
            'paisOrigen': 4,
            'ciudadOrigen': 5,
            'tiempoEmpleado': 6
        }

        sorted_rows = sorted(rows, key=lambda row: row[field_index[campoCreado]], reverse=(ordenCreado == 'DESC'))

        cursor.execute('DELETE FROM clasificacionfinalyess')

        cursor.executemany(
            'INSERT INTO clasificacionfinalyess (noInscripcion, nombre, apellido, fechaNacimiento, paisOrigen, ciudadOrigen, tiempoEmpleado) VALUES (?, ?, ?, ?, ?, ?, ?)',
            sorted_rows
        )

        self.con.commit()
        print("Clasificación actualizada.")

class Enunciado:
    def Saludo(self):
        print('''Bienvenido Señor usuario, para nosotros es muy grata su visita.
              Seleccione la opcion de su preferencia....''')
    def Despedida(self):
        print('''Fue un gusto atender tu solicitud,espero haber hecho bien mi trabajo.
              Hasta luego...''')
class Mensajes(Enunciado):#clase que recibe herencia de la clase enunciado
    pass


def menu(con,atletaParticipanteRecibido,EventoPRecibido,clasificacionA):
    salirPrincipal=False
    Usuario=Mensajes()
    Usuario.Saludo()
    while not salirPrincipal:
        opePrincipal=input('''
                 Menu Principal

                 1. Menu de gestion de Carrera
                 2. Menu Gestíon de Atletas
                 3. Menu Administracion Resultado de Carrera
                 4. Clasificacion Final de la Carrera
                 5. Salir

                 Seleccione una Opción>>>:   ''')
        if (opePrincipal=='1'):
            salirEvento=False        
            while not salirEvento:
                opeEvento=input('''
                    Menú de Gestión de Carrera

                    1.  Crear Evento Nuevo teclado
                    2.  Salir

                    Seleccione una Opción>>>:  ''')
                if (opeEvento=='1'):
                    
                    #eventoCreado=EventoPRecibido.leerEvento()
                    EventoPRecibido.setNumero_evento()
                    EventoPRecibido.setAño()
                    EventoPRecibido.setpremio_primer_puesto()
                    EventoPRecibido.setpremio_segundo_puesto()
                    EventoPRecibido.setpremio_tercer_puesto()
                    tuplaParametro=EventoPRecibido.armarTupla()
                    
                    EventoPRecibido.insertarTablaEvento(con,tuplaParametro)
                elif (opeEvento=='2'):
                    salirEvento=True

        elif (opePrincipal=='2'):
            salirAtletas=False
            while not salirAtletas:
                opeAtletas=input('''
                 Menú Gestíon de Atletas

                 1. Crear Atleta Nuevo teclado
                 2. Modificar Informacion Atleta
                 3. Consultar Informacion de Atleta
                 4. Salir

                 Seleccione una Opción>>>:   ''')
                
                if (opeAtletas=='1'):
                    #atletaCreado=atletaParticipanteRecibido.leerAtleta()
                    atletaParticipanteRecibido.setnoidAtleta()
                    atletaParticipanteRecibido.setnoInscripcion()
                    atletaParticipanteRecibido.setnombre() 
                    atletaParticipanteRecibido.setapellido()
                    atletaParticipanteRecibido.setfechaNacimiento()
                    atletaParticipanteRecibido.setpaisOrigen()
                    atletaParticipanteRecibido.setciudadOrigen()
                    tuplaParametro=atletaParticipanteRecibido.armarTupla()
                    
                    atletaParticipanteRecibido.insertarTablaAtleta(con,tuplaParametro)

                elif (opeAtletas=='2'):
                    #consultaTablaAtleta(con)
                    atletaParticipanteRecibido.consultaTablaAtleta(con)
                    salirmodAtletas=False
                    while not salirmodAtletas:
                        opeMod=input('''
                 Menú Modificacion de Atletas

                 1. Numero ID
                 2. Numero Inscripcion
                 3. Nombre
                 4. Apellido
                 5. Fecha Nacimiento
                 6. Pais
                 7. Ciudad
                 8. Salir

                 Seleccione una Opción>>>:   ''')
                        if(opeMod=='1'):
                            atletaParticipanteRecibido.actualizarAtletaID(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif(opeMod=='2'):
                            atletaParticipanteRecibido.actualizarAtletaInscripcion(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif (opeMod=='3'):
                            atletaParticipanteRecibido.actualizarAtletaNombre(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif (opeMod=='4'):
                            atletaParticipanteRecibido.actualizarAtletaApellido(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif (opeMod=='5'):
                            atletaParticipanteRecibido.actualizarAtletaNac(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif (opeMod=='6'):
                            atletaParticipanteRecibido.actualizarAtletaPais(con)
                            atletaParticipanteRecibido.consultaTablaAtleta(con)

                        elif (opeMod=='7'):
                            actualizarAtletaCiudad(con)
                            consultaTablaAtleta(con)
                                                   
                        elif(opeMod=='8'):
                            salirmodAtletas=True
                            
                            
                            
                    
                    
                elif (opeAtletas=='3'):
                    atletaParticipanteRecibido.consultaTablaAtleta(con)
                    
                    
                    
                elif (opeAtletas=='4'):
                    salirAtletas=True
                    
                    
        elif (opePrincipal=='3'):
            salirCarrera=False
            while not salirCarrera:
                opeCarrera=input('''

                 Menu Administración Resultado de Carrera

                 1. Creacion Atleta en carrera
                 2. Gestionar Resultados
                 3. Consultar resultados de Carreras
                 4. Salir

                 Seleccione una Opción>>>:   ''')
                
                
                if (opeCarrera=='1'):
                    infoCarrera=actCarrera(con)
                    consultarCarreraInscripcion(con,infoCarrera)
                    
                    
                elif (opeCarrera=='2'):
                    salirGestion=False
                    while not salirGestion:
                        opegestion=input('''
                    Menu Gestion de Resultados

                    1. Modificar Numero de Evento
                    2. Modificar Posicion
                    3. Modificar Tiempo
                    4. Modificar Estado 
                    5. Salir

                         Seleccione una Opción>>>:   ''')
                        if (opegestion=='1'):
                            actualizarCarreraEvento(con)
                                                        

                        elif (opegestion=='2'):
                            actualizarCarreraPosicion(con)
                            

                        elif (opegestion=='3'):
                            actualizarCarreraTiempo(con)
                            
                        elif (opegestion=='4'):
                            actualizarCarreraEstado(con)
                            
                        elif (opegestion=='5'):
                              salirGestion=True
                              
                elif (opeCarrera=='3'):
                    consultaTablaCarreras(con)

                elif (opeCarrera=='4'):
                    salirCarrera=True
                    
                
        elif (opePrincipal=='4'):
            salirClasificacion=False
            while not salirClasificacion:
                opeClasificacion=input('''

                 Menu Clasificacion Final de la Carrera

                 1. Consultar Clasificacion Final de la Carrera
                 2. Clasificacion ordenada
                 2. Salir

                 Seleccione una Opción>>>:   ''')
                
                if (opeClasificacion=='1'):
                    infoRR=actResultado(con)
                    consultarCarreraResultado(con,infoRR)
                    consultaTablaResultado(con)
                    
                elif (opeClasificacion=='2'):
                    
                    clasificacionA.actualizar_clasificacion()
                elif (opeClasificacion=='3'):
                    salirClasificacion=True
        elif (opePrincipal=='5'):
            salirPrincipal=True
            Usuario=Mensajes()
            Usuario.Despedida()

def conexionBD ():
    try:
        con=sqlite3.connect("Basejercicio.db")
        return con
    except Error:
        print (Error)
        
def creartablaAtleta(con):     #Crea una tabla llamada "atleta" en la base de datos si no existe 

    cursorObj=con.cursor()
    cad='''CREATE TABLE IF NOT EXISTS atleta(
    noidAtleta text NOT NULL,
    noInscripcion integer NOT NULL,
    nombre text,
    apellido text,
    fechaNacimiento date, 
    paisOrigen text,
    ciudadOrigen text,
    PRIMARY KEY (noidAtleta,noInscripcion)
    )
    '''
    cursorObj.execute(cad)
    con.commit()

def crearTablaEvento (con):  #Crea una tabla llamada "Evento" en la base de datos si no existe
    cursorObj=con.cursor()
    #recorremos la base de datos con el objeto de conexion
    cad='''CREATE TABLE IF NOT EXISTS Evento(
    Numero_evento texto NOT NULL,
    Año integer NOT NULL,
    premio_primer_puesto text,
    premio_segundo_puesto text,
    premio_tercer_puesto text,
    PRIMARY KEY(Numero_evento, Año))
    '''
    cursorObj.execute(cad)   #creamos la tabla carrera
    con.commit()

def creartablaclasificacion(con):
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clasificacionfinalyess (
        noInscripcion TEXT,
        nombre TEXT,
        apellido TEXT,
        fechaNacimiento TEXT,
        paisOrigen TEXT,
        ciudadOrigen TEXT,
        tiempoEmpleado TEXT
    )''')
    con.commit()
    
def conexionBDclose (con):
    con.close()
    
def main ():
    miCon=conexionBD()
    crearTablaEvento(miCon)
    creartablaAtleta(miCon)
    creartablaCarrera(miCon)
    creartablaResultados(miCon)
    creartablaclasificacion(miCon)
    atletaParticipante=Atleta()
    EventoP=Evento()
    clasificacionA=clasificacion(miCon)
    menu(miCon,atletaParticipante,EventoP,clasificacionA)
    conexionBDclose (miCon)

main()

        
