import pygame.mixer
import time
import contextlib
import os
import sys

@contextlib.contextmanager
def ignore_stderr():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)

with ignore_stderr():
  pygame.mixer.init()


# Constants
grand_piano = 'grand_piano'
notes = ['a','a_sharp','b','c','c_sharp', 'd','d_sharp','e','f','f_sharp','g','g_sharp']
wav = '.WAV'
sharp = 'sharp'
octaves = ['0','1','2','3','4','5','6','7','8']

def isAccidental(name):
  if sharp in name:
    return True 

def isNatural(name):
  if sharp in name:
    return False
  

def play(path, dur):
  print ('play path is %s' % path)
  sound = pygame.mixer.Sound(path)
  sound.play()
  time.sleep(dur);


play(grand_piano+'/notes/'+notes[3]+ '_4' + wav, 4)
print notes

#def c_major_scale():
  
