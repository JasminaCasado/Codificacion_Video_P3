# **P3 SCAV VIDEO**
En este repositorio se encuentras los ejercicios adjuntos de la tercera práctica de codificacion de video de la asignatura para la Universidad Pompeu Fabra. 

## 1. Nuevo BBB video
Para cortar 1 minuto del video original usamos el comando 

`ffmpeg -i bbb_video.mp4 -c copy -t 60 bbb_1minute.mp4` 

Tambien necesitamos el archivo sin audio, unicamente con el video 
`ffmpeg -i bbb_1minute.mp4 -c copy -an bbb_1minute_onlyVideo.mp4`

Después es necesario convertir a mono el audio del video y conseguir el menor biterate. Para ello 

`ffmpeg -i bbb_1minute.mp4 -ac 1 bbb_1minute_mono.ac3`

Comprobamos que efectivamente nuestro audio esta en mono 
`ffprobe bbb_1minute_mono.ac3`

Aplicamos la compresion 
`ffmpeg -i bbb_1minute_mono.ac3 -map 0:a:0 -b:a 16k lower_bbb.ac3`

Creamos un documento .srt con los subtitulos del primer minuto del video. 

Usamos la siguiente comanda para la ejecucion del container 

`ffmpeg -i bbb_1minute_onlyVideo.mp4 -i bbb_subtitles.srt -i bbb_1minute_mono.ac3 -i lower_bbb.ac3 -c:v copy -c:a aac -c:s mov_text -map 0:v:0 -map 2:a:0 -map 3:a:0 -map 1:s:0 bbb_container.mp4`

En este container podemos encontrar dos pistas de audio, una con el audio original en mono y otra con este mismo audio con un bitrate inferior. También se puede seleccionar desde VLC la pista de subtitulos. 

## 2. Automatizate Container 

Generamos un script _P3.py_ que por pantalla pide al usuario el nombre de los archivos para poder crear el container. En el ejercicio 5 creamos una función con este código. 

## 3. Container Info 

Creamos un script _P3_ en el que al introducir un container determina si pertenece a un Standard o no. 

Finalmente integramos las dos funciones generadas en una clase en el script _class_Lab3.py_


## Referencias 
* https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles
