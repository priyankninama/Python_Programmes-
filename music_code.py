import os 
import random


music_dir = 'E:\\Music'
songs = os.listdir(music_dir)
filename = random.choice(songs)
path = os.path.join(music_dir, filename)
print(filename)
os.startfile(path)
    