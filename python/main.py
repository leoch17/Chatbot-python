import os
import sys
import webbrowser as wb
from registro import Historial

chatbot = Historial()

print("Panda: Hola soy Panda estoy para ayudarte")


def main():

    Peticion = input("Panda: Necesita una carpeta o un documento?: ")
    h = chatbot.insertar_historial_peticion(
        Peticion)

    if Peticion == "carpeta":

        Carpeta = input("Panda: Dime el nombre o ubicación de la carpeta: ")
        h = chatbot.insertar_historial_carpeta(
            Carpeta)

        if ((Carpeta == "google") or (Carpeta == "buscador") or (Carpeta == "GOOGLE") or (Carpeta == "Google") or (Carpeta == "BUSCADOR") or (Carpeta == "Buscador")):
            wb.open_new(
                r'C:\Program Files (x86)\Google')

        elif ((Carpeta == "archivos") or (Carpeta == "files") or (Carpeta == "common") or (Carpeta == "comunes") or (Carpeta == "ARCHIVOS") or (Carpeta == "FILES") or (Carpeta == "COMMON") or (Carpeta == "COMUNES")):
            wb.open_new(
                r'C:\Program Files (x86)\Common Files')

        elif ((Carpeta == "perfil") or (Carpeta == "linkedin") or (Carpeta == "PERFIL") or (Carpeta == "Perfil") or (Carpeta == "LINKEDIN") or (Carpeta == "Linkedin") or (Carpeta == "https://www.linkedin.com/feed/")):
            wb.open_new(
                r'https://www.linkedin.com/feed/')

        elif ((Carpeta == "mercado") or (Carpeta == "libre") or (Carpeta == "Mercado") or (Carpeta == "Libre") or (Carpeta == "mercado libre") or (Carpeta == "Mercado Libre") or (Carpeta == "MERCADO LIBRE")):
            wb.open_new(r'https://www.mercadolibre.com.ve/')

        elif ((Carpeta == "bestbuy") or (Carpeta == "BestBuy") or (Carpeta == "Best") or (Carpeta == "best") or (Carpeta == "Buy") or (Carpeta == "buy") or (Carpeta == "BESTBUY")):
            wb.open_new(r'https://www.bestbuy.com/')

        elif ((Carpeta == "starplus") or (Carpeta == "Starplus") or (Carpeta == "STARPLUS") or (Carpeta == "StarPlus") or (Carpeta == "Star") or (Carpeta == "star") or (Carpeta == "Plus") or (Carpeta == "plus")):
            wb.open_new(r'https://www.starplus.com/es-419/login')

        elif ((Carpeta == "banesco") or (Carpeta == "BANESCO") or (Carpeta == "Banesco") or (Carpeta == "https://www.banesco.com/")):
            wb.open_new(r'https://www.banesco.com/')

        elif ((Carpeta == "venezuela") or (Carpeta == "Venezuela") or (Carpeta == "VENEZUELA") or (Carpeta == "banco de venezuela") or (Carpeta == "Banco de Venezuela") or (Carpeta == "https://www.bancodevenezuela.com/")):
            wb.open_new(r'https://www.bancodevenezuela.com/')

        else:
            print("Panda: Disculpe, no he entendido lo que busca")

    elif Peticion == "documento":
        # La variable "Documento" nos permite buscar el documento que solicitamos
        Documento = input('Panda: Dime el nombre del documento: ')
        h = chatbot.insertar_historial_documento(
            Documento)
        # La variable "directorio" contiene la ruta desde donde se va a comenzar la búsqueda
        directorio = os.getcwd()
        total = 0

        # La función "os.walk(directorio)" permite recorrer las carpetas y archivos desde la carpeta que le pasemos
        # La variable "root" nos devuelve la carpeta que se ha leido
        for root, dir, ficheros in os.walk(directorio):
            for fichero in ficheros:
                if fichero == Documento:
                    wb.open_new(directorio+'/'+fichero)

    else:
        print("Panda: Disculpa, no he entendido lo que buscas")


if __name__ == '__main__':
    main()
