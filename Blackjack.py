from behave import given,then.when
import random

Enjuego=False
EnjuegoIA=False
mano_jugador=[]
mano_IA=[]
Baraja=[]

@given("Quiere {respuesta} jugar")
def Quiere_respuesta_jugar(context,respuesta):
    if .format(respuesta)=='S':
        Enjuego=True

@given("Mano jugador")
def Juego_jugador(context):
    return mano_jugador

@given("Confirmar carta extra {respuesta}")
def Confirmar_carta_extra(context,respuesta):
    if .format(respuesta)=='S':
        Enjuego=True
    else:
          if .format(respuesta)=='N':
            Enjuego=False

@given("Juego IA")
def Juego_IA(context):
    return mano_IA

@when("Crea naipes")
def Crea_naipes(context):
    Baraja=hacerpinta("diamante",1)+hacerpinta("corazones",1)+hacerpinta("picas",1)+hacerpinta("trebol",1)
    barajar(Baraja)

@when("Mano jugador no vacia")
def Mano_vacia(context,Mano):
    if Mano_jugador==[]:
        return []
    else:
        return Mano_jugador
@when("Planta jugador")
def Planta_jugador(context):
    Enjuego=False

@when("Planta IA")
def Planta_IA(context):
    EnjuegoIA=False

then("Reparte jugador")
def  Reparte_jugador(context):
    mano_jugador.extend(sacarprimeracarta(Baraja))
    mano_IA.extend(sacarprimeracarta(Baraja))
    mano_jugador.extend(sacarprimeracarta(Baraja))
    mano_IA.extend(sacarprimeracarta(Baraja))

@then("Pregunta valor")
def hacercuentaconaces(context):
    if sacardelista(mano_jugador, 0)!=0:
        return sacardelista(mano_jugador,0)-1)+(sacardelistasumar(mano_jugador,0)-((sacardelista(mano_jugador,0)-1)*11)
    else:
        return sacardelista(mano_jugador,0)+(sacardelistasumar(mano_jugador,0)-(sacardelista(mano_jugador,0)*11)

@then("Contar mano")
def Contar(context):
    sacardelistasumar(mano_jugador,0)

@Then("Planta jugador")
def planta_jugador(context):
    Enjuego=False
                                             
                                


def sacarprimeracarta(baraja):
    return [baraja.pop(0)]

def hacerpinta(pinta, numero):
    if numero <= 10 and numero > 1:
        return [[numero, pinta]]+hacerpinta(pinta, numero+1)
    else:
        if numero == 1:
            return[["A", pinta]]+hacerpinta(pinta, numero+1)
        else:
             if numero > 10:
                  if numero == 11:
                        return [["J", pinta]]+hacerpinta(pinta, numero+1)
                  else:
                        if numero == 12:
                             return [["Q", pinta]]+hacerpinta(pinta, numero+1)
                        else:
                            if numero ==13:
                                 return [["K", pinta]]+hacerpinta(pinta, numero+1)
                            else:
                                if numero >= 14:
                                    return []


def barajar(baraja):
    random.shuffle(baraja)

def sacardelista(lista, n):
    if n < len(lista):
        return contarrecursivo(lista[n], "A")+sacardelista(lista, n+1)
    else:
        if n >= len(lista):
            return 0

def sacardelistasumar(lista, n):
    if n < len(lista):
        return sacarvalor(lista[n])+sacardelistasumar(lista, n+1)

def contarrecursivo(mano, objeto):
    if mano[0]== objeto:
        return 1
    else:
        return 0

def sacarvalor(lista):
    if lista[0]=="J" or lista[0]=="Q" or lista[0]=="K":
        return 10
    else:
        if lista[0]=="A":
            return 11
        else:
            return lista[0]

def verificar(lista,baraja):
    
    
            

    



    
    

