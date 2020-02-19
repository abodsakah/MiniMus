from pygame import mixer #imports pygame librery

mixer.init() # starts the mixer

volume = 7

print('Input filename (exemple: "song.mp3")')
song = input('>>>') # file name from user input
mixer.music.load(song) # loads the file into pygame mixer
mixer.music.set_volume(volume/10) # sets the apps volume to the volume devided by 10
mixer.music.play() # plays the sound file


while True:
    print('press "p" to pause, "r" to resume.')
    print('press "e" to exit')
    print ('press "+" to incress volume, "-" to decress')

    # prints out a volume visuel
    if volume == 0:
        print('----------')
    elif volume == 1:
        print('|---------')
    elif volume == 2:
        print('||--------')
    elif volume == 3:
        print('|||-------')
    elif volume == 4:
        print('||||------')
    elif volume == 5:
        print('|||||-----')
    elif volume == 6:
        print('||||||----')
    elif volume == 7:
        print('|||||||---')
    elif volume == 8:
        print('||||||||--')
    elif volume == 9:
        print('|||||||||-')
    elif volume == 10:
        print('||||||||||')




    query = input('>>>') #gets user input
    print("\n\n")

    if query=="p": # pause if query input is p
        mixer.music.pause()
    elif query=="r": # unpause if query input is r
        mixer.music.unpause()
    elif query=="e": #stop music and exit if query input is e
        mixer.music.stop()
        break
    elif query=="+" and volume < 10:
        volume += 1
        mixer.music.set_volume(volume/10) # sets the apps volume to the volume devided by 10
    elif query == "-" and volume > 0:
        volume -=1
        mixer.music.set_volume(volume/10) # sets the apps volume to the volume devided by 10
    else: # if an unkown command is writen this would print
        print("Unkown command \n\n")

