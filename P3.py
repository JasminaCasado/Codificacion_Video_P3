import os

video = input('Nombre del video')
audio = input('Nombre del audio')
subs = input('Nombre de los subtitulos')
output = input('Nombre del contenedor')

command = 'ffmpeg ' + '-i ' + video + ' -i ' + audio + ' -i '+ subs + ' -c copy' + ' -map 0:v:0'+ ' -map 1:a:0'+ ' -c:s mov_text '+ output
#print(command)
#os.system('ffmpeg', '-i', video, '-i', audio, '-i', subs, ' -c copy', ' -map 0:v:0', ' -map 1:a:0', ' -c:s mov_text', output)
os.system(command)

