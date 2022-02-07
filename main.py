from pytube import YouTube

# Link del video a descargar: (Primera version, mas adelante se agregará descarga por ficheros)
link = "https://www.youtube.com/watch?v=6qugPyUrzRE"



if __name__ == "__main__":
    print("Pues iniciamos: ")
    print("....")

    yt = YouTube(link)

    #Generamos las posibles transmisiones del video:
    videos = yt.streams.all()

    #Indexamos la lista, comenzando con el 0 (cero)
    video = list(enumerate(videos))

    for i in video:
        print(i)
        # Imprimimos todo el formato disponible.

    
    #Preguntamos cual es la opcion de video que queremos descargar:
    print("ingrese la Opcion a descargar: ")

    selected_option = int(input("Ingrese la opcion: "))

    dn_video = videos[selected_option]

    try:

        #El archivo de descarga queda en el mismo directorio de la app
        dn_video.download()
        print("Descarga correcta.")
    except:
        print("Error al descargar video.")
    

