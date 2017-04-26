#
# created by Injung Lily Kim
# last modified date: 3/9/2017
# contact: t-likim@microsoft.com
#
# pyglet is open source to play music
# ref: https://bitbucket.org/pyglet/pyglet/wiki/Home
#
import pyglet

winxp = 'winxp.wav'
win10 = 'win10.wav'
tada = 'tada.wav'

def exiter(dt):
    pyglet.app.exit()

# this part may be chosen by user's intent (which music/sound they want to play)
sound = pyglet.media.load(win10)

# play the sound
sound.play()

# hole until the sound is over, then finish the application
pyglet.clock.schedule_once(exiter, sound.duration)
pyglet.app.run()