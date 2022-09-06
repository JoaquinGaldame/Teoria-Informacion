import os
from os import system
from time import sleep

class Persona:

    def __init__(self, nya:str, direccion:str, dni:str, estudiosP:bool, estudiosS:bool, estudiosU:bool, viviendaP:bool, obraSocial:bool, trabaja:bool, a:bool, b:bool):
        self.nya            = nya.ljust(40)[0:40].rstrip()       # Nombre y Apellido
        self.direccion      = direccion.ljust(40)[0:40].rstrip() # Direccion
        self.dni            = dni.ljust(40)[0:40].rstrip()       # DNI
        self.estudiosP      = estudiosP                          # Estudios primarios (Y/N)
        self.estudiosS      = estudiosS                          # Estudios secundarios (Y/N)
        self.estudiosU      = estudiosU                          # Estudios universitarios (Y/N)
        self.viviendaP      = viviendaP                          # Tiene vivienda propia (Y/N)
        self.obraSocial     = obraSocial                         # Obra social (Y/N)
        self.trabaja        = trabaja                            # Trabaja (Y/N)
        self.a              = a                                  # (Y/N)
        self.b              = b                                  # (Y/N)

    def ToBytesLongitudFija(self):
        bytes = []
        bytes += bytearray(self.nya.ljust(40), "UTF-8")
        bytes += bytearray(self.direccion.ljust(40), "UTF-8")
        bytes += bytearray(self.dni.ljust(40), "UTF-8")
        bytes += self.estudiosP.to_bytes(1, byteorder='big')
        bytes += self.estudiosS.to_bytes(1, byteorder='big')
        bytes += self.estudiosU.to_bytes(1, byteorder='big')
        bytes += self.viviendaP.to_bytes(1, byteorder='big')
        bytes += self.obraSocial.to_bytes(1, byteorder='big')
        bytes += self.trabaja.to_bytes(1, byteorder='big')
        bytes += self.a.to_bytes(1, byteorder='big')
        bytes += self.b.to_bytes(1, byteorder='big')
        return bytes

    def ToBytesLongitudVariable(self):
        bytes = []
        bytes += len(self.nya).to_bytes(1, byteorder='big')         + bytearray(self.nya, "UTF-8")
        bytes += len(self.direccion).to_bytes(1, byteorder='big')   + bytearray(self.direccion, "UTF-8")
        bytes += len(self.dni).to_bytes(1, byteorder='big')         + bytearray(self.dni, "UTF-8")
        byteSINO = 0
        if(self.estudiosP): byteSINO += 128
        if(self.estudiosS): byteSINO += 64
        if(self.estudiosU): byteSINO += 32
        if(self.viviendaP): byteSINO += 16
        if(self.obraSocial):byteSINO += 8
        if(self.trabaja):   byteSINO += 4
        if(self.a):         byteSINO += 2
        if(self.b):         byteSINO += 1
        bytes += byteSINO.to_bytes(1, byteorder='big')
        return bytes
    
    def printPersona(self):
        print('-'*60)
        print(' Nombre: '                   + self.nya)
        print(' Direccion: '                + self.direccion)
        print(' DNI: '                      + self.dni)
        print(' Estudios primarios: '       + str(self.estudiosP).replace('True','Si').replace('False','No'))
        print(' Estudios secundarios: '     + str(self.estudiosS).replace('True','Si').replace('False','No'))
        print(' Estudios universitarios: '  + str(self.estudiosU).replace('True','Si').replace('False','No'))
        print(' Tiene vivienda propia: '    + str(self.viviendaP).replace('True','Si').replace('False','No'))
        print(' Obra social: '              + str(self.obraSocial).replace('True','Si').replace('False','No'))
        print(' Trabaja: '                  + str(self.trabaja).replace('True','Si').replace('False','No'))
        print(' A: '                        + str(self.a).replace('True','Si').replace('False','No'))
        print(' B: '                        + str(self.b).replace('True','Si').replace('False','No'))
        print('-'*60)

def writeBytes(filename, bytes):
    with open(filename,'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder='big'))

def readBytes(filename):
    bytes = []
    with open(filename,'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))
    return bytes

def printBytesLongFija(bytes):
    print('-'*60)
    print(' >> Datos Longitud Fija <<')
    print(' Nombre: '                   + ''.join(map(chr,bytes[0:39])))
    print(' Direccion: '                + ''.join(map(chr,bytes[40:79])))
    print(' DNI: '                      + ''.join(map(chr,bytes[80:119])))
    print(' Estudios primarios: '       + str(bool(bytes[120])).replace('True','Si').replace('False','No'))
    print(' Estudios secundarios: '     + str(bool(bytes[121])).replace('True','Si').replace('False','No'))
    print(' Estudios universitarios: '  + str(bool(bytes[122])).replace('True','Si').replace('False','No'))
    print(' Tiene vivienda propia: '    + str(bool(bytes[123])).replace('True','Si').replace('False','No'))
    print(' Obra social: '              + str(bool(bytes[124])).replace('True','Si').replace('False','No'))
    print(' Trabaja: '                  + str(bool(bytes[125])).replace('True','Si').replace('False','No'))
    print(' A: '                        + str(bool(bytes[126])).replace('True','Si').replace('False','No'))
    print(' B: '                        + str(bool(bytes[127])).replace('True','Si').replace('False','No'))
    print('-'*60)

def printBytesLongVariable(bytes):
    print('-'*60)
    print(' >> Datos Longitud Variable <<')
    puntero = 0
    nCaracteres = bytes[puntero]
    siguiente = puntero + nCaracteres + 1
    print(' Nombre: '                   + ''.join(map(chr,bytes[puntero+1:siguiente])))
    puntero = siguiente
    nCaracteres = bytes[puntero]
    siguiente = puntero + nCaracteres + 1
    print(' Direccion: '                + ''.join(map(chr,bytes[puntero+1:siguiente])))
    puntero = siguiente
    nCaracteres = bytes[puntero]
    siguiente = puntero + nCaracteres + 1
    print(' DNI: '                      + ''.join(map(chr,bytes[puntero+1:siguiente])))
    puntero = siguiente
    nCaracteres = bytes[puntero]
    print(' Estudios primarios: '       + str(bool(nCaracteres&128)).replace('True','Si').replace('False','No'))
    print(' Estudios secundarios: '     + str(bool(nCaracteres&64)).replace('True','Si').replace('False','No'))
    print(' Estudios universitarios: '  + str(bool(nCaracteres&32)).replace('True','Si').replace('False','No'))
    print(' Tiene vivienda propia: '    + str(bool(nCaracteres&16)).replace('True','Si').replace('False','No'))
    print(' Obra social: '              + str(bool(nCaracteres&8)).replace('True','Si').replace('False','No'))
    print(' Trabaja: '                  + str(bool(nCaracteres&4)).replace('True','Si').replace('False','No'))
    print(' A: '                        + str(bool(nCaracteres&2)).replace('True','Si').replace('False','No'))
    print(' B: '                        + str(bool(nCaracteres&1)).replace('True','Si').replace('False','No'))
    print('-'*60)       

def validarInputSINO(indicadorEntrada:str):
    while(True):
        sino = input(indicadorEntrada).strip().lower()[0]
        if sino in {'s','n'} :
            sino = bool(sino.replace('n',''))
            return sino
        else:
            print(" ** El valor debe ser SI/NO **")
            sleep(1)

def ingresarPersona(personas:list):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Ingresar nueva persona]')
    print(' Datos de la persona: ')

    nya         = input(' # Nombre y Apellido: ').strip()
    direccion   = input(' # Direccion: ').strip()
    dni         = input(' # DNI: ').strip()
    
    estudiosP   = validarInputSINO(' # Estudios primarios (SI/NO): ')
    estudiosS   = validarInputSINO(' # Estudios secundarios (SI/NO): ')
    estudiosU   = validarInputSINO(' # Estudios universitarios (SI/NO): ')
    viviendaP   = validarInputSINO(' # Tiene vivienda propia (SI/NO): ')
    obraSocial  = validarInputSINO(' # Obra social (SI/NO): ')
    trabaja     = validarInputSINO(' # Trabaja (SI/NO): ')
    a           = validarInputSINO(' # A (SI/NO): ')
    b           = validarInputSINO(' # B (SI/NO): ')
    try:
        nuevaPersona = Persona(nya,direccion,dni,estudiosP,estudiosS,estudiosU,viviendaP,obraSocial,trabaja,a,b)
        nuevaPersona.printPersona()
        if validarInputSINO(' # Desea cargar esta persona? (SI/NO): '):
            personas.append(nuevaPersona)
            print(' ** Nueva persona cargada de forma correcta **')
        else: print(' ** Nueva persona no fue cargada **')
    except:
        print(" ** Error al cargar nueva persona **")
    sleep(1)
    input(' ** Enter para regresar al menu **')

def guardarPersonasLongFija(personas):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Guardar datos en archivo de longitud fija]')

    if(len(personas) == 0):
        print(' ** No hay personas cargadas **')
        sleep(1)
        input(' ** Enter para regresar al menu **')
    else:
        #-- Directorio de trabajo.
        try:
            basePath = os.getcwd()
            filePathFijos   = rf'{basePath}\fijos.dat'

            bytes = []
            for p in map(Persona.ToBytesLongitudFija, personas) : bytes+=p
            writeBytes(filePathFijos, bytes)

            print(' ** Se guardaron los datos de forma correcta **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **')
        except: 
            print(' ** Error al escribir el archivo **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **')

def guardarPersonasLongVariable(personas):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Guardar datos en archivo de longitud variabl]')
    
    if(len(personas) == 0):
        print(' ** No hay personas cargadas **')
        sleep(1)
        input(' ** Enter para regresar al menu **')
    else:
        #-- Directorio de trabajo.
        try:
            basePath = os.getcwd()
            filePathVariables   = rf'{basePath}\variables.dat'

            bytes = []
            for p in map(Persona.ToBytesLongitudVariable, personas) : bytes+=p
            writeBytes(filePathVariables, bytes)

            print(' ** Se guardaron los datos de forma correcta **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **')
        except: 
            print(' ** Error al escribir el archivo **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **')

def cargarPersonasLongFija(personas):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Cargar datos desde el archivo de longitud fija]')
    
    #-- Directorio de trabajo.
    try:
        basePath = os.getcwd()
        filePathFijos       = rf'{basePath}\fijos.dat'
        bytes = readBytes(filePathFijos)
    except: 
        print(' ** Error al leer el archivo **')
        print('[dirPath]: ' + filePathFijos)
        sleep(1)
        input(' ** Enter para regresar al menu **') 
        return []
    
    siguiente = 0
    while siguiente < len(bytes):
        try:
            puntero = siguiente
            nCaracteres = 40
            siguiente = puntero + nCaracteres
            nya            = ''.join(map(chr,bytes[puntero:siguiente]))

            puntero = siguiente
            siguiente = puntero + nCaracteres
            direccion      = ''.join(map(chr,bytes[puntero:siguiente]))

            puntero = siguiente
            siguiente = puntero + nCaracteres
            dni            = ''.join(map(chr,bytes[puntero:siguiente]))

            puntero = siguiente
            estudiosP      = bool(bytes[puntero])
            estudiosS      = bool(bytes[puntero+1])
            estudiosU      = bool(bytes[puntero+2])
            viviendaP      = bool(bytes[puntero+3])
            obraSocial     = bool(bytes[puntero+4])
            trabaja        = bool(bytes[puntero+5])
            a              = bool(bytes[puntero+6])
            b              = bool(bytes[puntero+7])
            siguiente = puntero + 8

            personas.append(Persona(nya.strip(),direccion.strip(),dni.strip(),estudiosP,estudiosS,estudiosU,viviendaP,obraSocial,trabaja,a,b))
        except:
            print(' ** Error al leer el archivo **')
            print('[dirPath]: ' + filePathFijos)
            sleep(1)
            input(' ** Enter para regresar al menu **') 
            return []
    
    print(' ** Se cargaron los datos de forma correcta **')
    print('[dirPath]: ' + filePathFijos)
    sleep(1)
    input(' ** Enter para regresar al menu **')        
    return personas

def cargarPersonasLongVariable(personas:list):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Cargar datos desde el archivo de longitud variable]')
    
    #-- Directorio de trabajo.
    try:
        basePath = os.getcwd()
        filePathVariables   = rf'{basePath}\variables.dat'
        bytes = readBytes(filePathVariables)
    except: 
        print(' ** Error al leer el archivo **')
        print('[dirPath]: ' + filePathVariables)
        sleep(1)
        input(' ** Enter para regresar al menu **') 
        return []
    
    siguiente = 0
    while siguiente < len(bytes):
        try:
            puntero = siguiente
            nCaracteres = bytes[puntero]
            siguiente = puntero + nCaracteres + 1
            nya            = ''.join(map(chr,bytes[puntero+1:siguiente]))

            puntero = siguiente
            nCaracteres = bytes[puntero]
            siguiente = puntero + nCaracteres + 1
            direccion      = ''.join(map(chr,bytes[puntero+1:siguiente]))

            puntero = siguiente
            nCaracteres = bytes[puntero]
            siguiente = puntero + nCaracteres + 1
            dni            = ''.join(map(chr,bytes[puntero+1:siguiente]))

            puntero = siguiente
            nCaracteres = bytes[puntero]
            siguiente = puntero + 1

            estudiosP      = bool(nCaracteres&128)
            estudiosS      = bool(nCaracteres&64)
            estudiosU      = bool(nCaracteres&32)
            viviendaP      = bool(nCaracteres&16)
            obraSocial     = bool(nCaracteres&8)
            trabaja        = bool(nCaracteres&4)
            a              = bool(nCaracteres&2)
            b              = bool(nCaracteres&1)

            personas.append(Persona(nya,direccion,dni,estudiosP,estudiosS,estudiosU,viviendaP,obraSocial,trabaja,a,b))
        except:
            print(' ** Error al leer el archivo **')
            print('[dirPath]: ' + filePathVariables)
            sleep(1)
            input(' ** Enter para regresar al menu **') 
            return []
    
    print(' ** Se cargaron los datos de forma correcta **')
    print('[dirPath]: ' + filePathVariables)
    sleep(1)
    input(' ** Enter para regresar al menu **')       
    return personas

def mostrarPersonas(personas:list):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Mostrar datos persona]')
        
    if(len(personas) == 0):
        print(' ** No hay personas cargadas **')
        sleep(1)
        input(' ** Enter para regresar al menu **')
    else:
        for persona in personas: persona.printPersona()
        input(' ** Enter para regresar al menu **')

def borrarPersonasCargadas(personas):
    os.system("cls")
    print(' >> EJERCICIO 5 <<')
    print(' [Borrar personas cargadas]')
        
    if(len(personas) == 0): print(' ** No hay personas cargadas **')
    else:
        personas = [] 
        print(' ** Se borraron las personas cargadas **')
    sleep(1)
    input(' ** Enter para regresar al menu **')
    return personas

def program():
    personas = []
    while(True):
        os.system("cls")
        print(' >> EJERCICIO 5 <<')
        print(' Menu')
        print(' 0. Salir')
        print(' 1. Ingresar nueva persona')
        print(' 2. Guardar datos en archivo de longitud fija')
        print(' 3. Guardar datos en archivo de longitud variable')
        print(' 4. Cargar datos desde el archivo de longitud fija')
        print(' 5. Cargar datos desde el archivo de longitud variable')
        print(' 6. Mostrar datos persona')
        print(' 7. Borrar personas cargadas')
        
        option = input(" > ")
        try:
            option = int(option)
            if(option in range(0,8)):
                if  (option == 0): break
                elif(option == 1): ingresarPersona(personas)
                elif(option == 2): guardarPersonasLongFija(personas)
                elif(option == 3): guardarPersonasLongVariable(personas)
                elif(option == 4): personas = cargarPersonasLongFija(personas)
                elif(option == 5): personas = cargarPersonasLongVariable(personas)
                elif(option == 6): mostrarPersonas(personas)
                elif(option == 7): personas = borrarPersonasCargadas(personas)
            else: 
                print(' ** Ingrese una opcion valida **')
                sleep(1)
        except:
            print(' ** Ingrese una opcion valida **')
            sleep(1)

program()