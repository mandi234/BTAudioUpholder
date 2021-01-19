import os
import time
import vlc

start_of_program = time.time()
path = os.getcwd()

media = vlc.MediaPlayer(path+'\\white_noise.mp3')
media.play()

while True:
    print("loop")
    time.sleep(15)
    media.set_time(0)
