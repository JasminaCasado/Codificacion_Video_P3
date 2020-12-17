import os

video = input('Nombre del video')
audio = input('Nombre del audio')
subs = input('Nombre de los subtitulos')
output = input('Nombre del contenedor')

command = 'ffmpeg -i {} -i {} -i {} -c:v copy -c:a -c:s mov_text -map 0:v:0 -map 1:a:0 -map 2:s:0 {}'.format(video, audio, subs, output)
#print(command)
#os.system('ffmpeg', '-i', video, '-i', audio, '-i', subs, ' -c copy', ' -map 0:v:0', ' -map 1:a:0', ' -c:s mov_text', output)
os.system(command)

