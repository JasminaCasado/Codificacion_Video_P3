import os
import subprocess


class Lab3_P5:

    def check_brodcast(codec_video, codec_audio):
        if codec_video in ['avs', 'avs+']:

            if codec_audio in ['mp2', 'dra']:
                print('DTMB: Compatible con el codec', codec_audio, 'de audio y codec de video', codec_video)

            else:
                print('No es un standard')

        elif codec_video in ['h264', 'mpeg2']:

            if codec_audio == 'ac-3':  # al imprimire los foramatos ac3 lo guarda como ac-3
                print('DVB, DTMB y ATSC: Compatibles con el codec', codec_audio, 'de audio y codec de video', codec_video)

            elif codec_audio == 'mp3':
                print('DVB y DTMB: Compatibles con el codec', codec_audio, 'de audio y codec de video', codec_video)

            elif codec_audio == 'aac':
                print('DVB, ISDB y DTMB: Compatibles con el codec', codec_audio, 'de audio y codec de video', codec_video)

            else:
                print('No es un standard')

    def create_container(video, audio, subs, output):
        command = 'ffmpeg -i {} -i {} -i {} -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 2:a:0 -map 1:s:0 {}'.format(
            video, subs, audio, output)
        #print(command)
        os.system(command)

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0

while not salir:

    print("1. Opcion 1 : Creat Container")
    print("2. Opcion 2 : Check Broadcasting Standard Compatibility")
    print("3. Salir")

    # print ("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        video = input('Nombre del video')
        audio = input('Nombre del audio')
        subs = input('Nombre de los subtitulos')
        output = input('Nombre del contenedor')

        Lab3_P5.create_container(video, audio, subs, output)

    elif opcion == 2:
        container = input('Nombre del container del que obtener informacion')

        codec_video = subprocess.getoutput('ffprobe -v error -select_streams v:0 -show_entries '
                                           'stream=codec_name '
                                           '-of default=nokey=1:noprint_wrappers=1 {}'.format(container))
        codec_audio = subprocess.getoutput('ffprobe -v error -select_streams a:0 -show_entries '
                                           'stream=codec_name '
                                           '-of default=nokey=1:noprint_wrappers=1 {}'.format(container))
        Lab3_P5.check_brodcast(codec_video, codec_audio)

        print(codec_video, codec_audio)

    elif opcion == 3:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
