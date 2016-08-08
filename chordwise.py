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
a_flat = 11
a = 0
a_sharp = 1
b_flat = 2
b = 2
c = 3
c_sharp = 4
d_flat = 4
d = 5
d_sharp = 6
e_flat = 6
e = 7
f = 8
f_sharp = 9
g_flat = 9
g = 10
g_sharp = 11

wav = '.WAV'
sharp = 'sharp'
octaves = ['0','1','2','3','4','5','6','7','8']
half = 1
whole = 2
major_form = [whole, whole, half, whole, whole, whole, half]
minor_form = [whole, half, whole, whole, half, whole, whole]
major = 'major'
minor = 'minor'
major_triad = [0, 2, 4]

# Sharp a note
def sharp(note):
  return (note + 1) % 12

# Flat a note
def flat(note):
  note = note - 1
  return note if note > 0 else 11

# Find note that is interval steps higher
def find_interval(note, interval):
  return (((note[0] + interval) % 12), note[1] if (note[0] + interval) < 12 else note[1] + 1)

def construct_chord(root_note, form, chord_form):
  scale = construct_scale(root_note, form)
  chord = []
  for n in chord_form:
    chord.append(scale[n])
  return chord
  

# Construct a scale given a note, it's octave, and the scale form (a list of intervals)
def construct_scale(root_note, form, num=8):
  scale = []
  cur_note = root_note
  scale.append(cur_note)
  count = 1
  for interval in form:
    if count == num:
      break
    cur_note = find_interval(cur_note, interval)
    #print("appending %s" % cur_note)
    scale.append(cur_note)
    count += 1
  return scale

# Return true if note is accidental
def isAccidental(name):
  if sharp in name:
    return True 

# Return true if note is natural
def isNatural(name):
  if sharp in name:
    return False
  

def play(path):
  print ('play path is %s' % path)
  sound = pygame.mixer.Sound(path)
  sound.play()

def play_note(note, instrument, duration):
  play(instrument + '/' + notes[note[0]] + '/notes/' + notes[note[0]] + '_' + str(note[1]) + wav)
  time.sleep(duration)

def play_chord(root_note, form, num, instrument, duration):
  #calculate chord
  n = construct_chord(root_note, form, major_triad)
  for key in n:
    print key
    play_note(key, instrument, 0)
  #play_note((c,4), grand_piano, 0)
  #play_note((e,4), grand_piano, 0)
  #play_note((g,4), grand_piano, 0)
  time.sleep(3)


#def play_chord(chord, variation, instrument, duration):
#  play(instrument + '/' + notes[note[0]] + '/chords/' + variation + notes[note[0]] + '_' + str(note[1]) + wav, duration)

#play(grand_piano+'/notes/'+notes[3]+ '_4' + wav, 1)
#print notes
#sc = construct_major(c,4)
#sc = construct_scale((c,4),major_form, 7)
#print sc

#g_chord = construct_scale((g,4),major_form,3)
#d_chord = construct_scale((g,4),major_form,3)
while True:
  play_chord((g,3),major_form,3,grand_piano,3)
  play_chord((g,3),major_form,3,grand_piano,3)
  play_chord((d,4),major_form,3,grand_piano,3)
  play_chord((d,4),major_form,3,grand_piano,3)
  play_chord((c,4),major_form,3,grand_piano,3)

#play_chord(c,d,e,f)
#for n in sc:
#  print n
#  play_note(n, grand_piano, 1)


  
