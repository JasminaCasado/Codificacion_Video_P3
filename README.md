# **P3 SCAV VIDEO**
En este repositorio se encuentras los ejercicios adjuntos de la tercera práctica de codificacion de video de la asignatura para la Universidad Pompeu Fabra. 

## 1. Nuevo BBB video
Para cortar 1 minuto del video original usamos el comando 

`ffmpeg -i bbb_video.mp4 -ss 00:00:00 -t 00:01:00 bbb_1minute.mp4` 

Tambien necesitamos el archivo sin audio, unicamente con el video 
`ffmpeg -i bbb_1minute.mp4 -c copy -an bbb_1minute_onlyVideo.mp4`

Después es necesario convertir a mono el audio del video y conseguir el menor biterate. Para ello 

`ffmpeg -i bbb_1minute.mp4 -ac 1 bbb_1minute_mono.mp4`

Comprobamos que efectivamente nuestro audio esta en mono 
`ffprobe bbb_1minute_mono.mp4`

Aplicamos la compresion 
`ffmpeg -i bbb_1minute_mono.mp4 -map 0:a:0 -b:a 31k lower_bbb.mp3`

Creamos un documento .srt con los subtitulos del primer minuto del video. 
## 2. MP4 container 

Usamos la siguiente comanda para la ejecucion del container 

`ffmpeg -i bbb_1minute_onlyVideo.mp4 -i lower_bbb.mp3 -i bbb_subtitles.srt -c copy -map 0:0 -map 1:0 -c:s mov_text totalSub.mp4`


## Referencias 
* https://stackoverflow.com/questions/8672809/use-ffmpeg-to-add-text-subtitles
