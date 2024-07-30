#bir klasörü açsın ve içindekileri göstersin.
from pygame import mixer
from os import chdir
from pathlib import Path

while True:
    try:
        path = input('Enter a path: ')
        chdir(path)
        break
    except Exception as f:
        print(f)

mypath = Path()
counter=0
print('\tSongs in your directory:')
for a in mypath.glob('*.mp3'):
    print(a)
    counter+=1
print(f'\n\t{counter} songs found.')
mixer.init()
mixer.music.load('song.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()
print("Press 'p' to pause 'r' to resume.")
print("Press 'q' to exit.")
while True:
    query =input('>>>')
    if query =='p':
        mixer.music.pause()
    elif query=='r':
        mixer.music.unpause()
    elif query=='q':
        mixer.music.stop()
        break