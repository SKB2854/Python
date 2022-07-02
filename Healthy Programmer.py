'''
Healthy Programmer
9AM - 5PM
Water - water.mp3 - (3.5 litre) - Drank - time log when pani pi liya
Eyes - eyes.mp3 - every 30 min - EyDone - log
Physical activity - physical.mp3 - every 45 mins exercise - ExDone - log
----Rules----
Pygame module to play audio
'''
from time import time
from datetime import datetime
from pygame import mixer

def music_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 15

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            music_loop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            music_loop('water.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            music_loop('water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")



