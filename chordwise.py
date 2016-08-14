import pygame.mixer
import time
import contextlib
import os
import sys


# This prevents ugly deprecated carbon component manager
# message from being printed upon every run of the program
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
  #pygame.mixer.pre_init(22050, -16, 2, 2048)
  pygame.mixer.pre_init(44100, -16, 2, 100)
  pygame.mixer.init()


# Constants

GRAND_PIANO = 'GRAND_PIANO'
NOTES = ['A','A_SHARP','B','C','C_SHARP', 'D','D_SHARP','E','F','F_SHARP','G','G_SHARP']
CHORD_SCALES = ['Major', 'Minor']
CHORD_FORMS = ['Triad', 'Seventh']
#TODO create dictionary to map these to the constants so that the conversion doesn't have to happen in the UI file


A_FLAT = 11
A = 0
A_SHARP = 1
B_FLAT = 2
B = 2
C = 3
C_SHARP = 4
D_FLAT = 4
D = 5
D_SHARP = 6
E_FLAT = 6
E = 7
F = 8
F_SHARP = 9
G_FLAT = 9
G = 10
G_SHARP = 11

WAV = '.WAV'
SHARP = 'SHARP'
# Need to start at 1 so we don't jump around (left of keyboard)
OCTAVES = ['1','2','3','4','5','6','7','8']
HALF = 1
WHOLE = 2
MAJOR_SCALE = [WHOLE, WHOLE, HALF, WHOLE, WHOLE, WHOLE, HALF]
MINOR_SCALE = [WHOLE, HALF, WHOLE, WHOLE, HALF, WHOLE, WHOLE]
MAJOR = 'MAJOR'
MINOR = 'MINOR'
TRIAD = [0, 2, 4]
TRIAD_1ST_INV = [2, 4, 7]
TRIAD_2ND_INV = [4, 7, 9] # DOUBLE CHECK THIS
SEVENTH = [0, 2, 4, 6]
SEVENTH_1ST_INV = [2, 4, 6, 7]


piano_notes = []
for note in NOTES:
  note_list = []
  for octave in OCTAVES:
    sound = pygame.mixer.Sound('grand_piano' + '/' + note + '/notes/' + note + '_' + octave + WAV)
    #print("appending sound path = %s" % 'grand_piano' + '/' + note + '/notes/' + note + '_' + octave + WAV)
    note_list.append(sound)
  piano_notes.append(note_list)


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

# TODO add optional scale parameter to prevent need to construct
# TODO also add optional positional parameter to use for chord progressions
def construct_chord(root_note, form, chord_form):
  scale = construct_scale(root_note, form)
  chord = []
  for pos in chord_form:
    chord.append(scale[pos])
  return chord
  

# Construct a scale given a note, it's octave, and the scale form (a list of intervals)
def construct_scale(root_note, form, num=8):
  scale = []
  cur_note = root_note
  scale.append(cur_note)
  # keeps track of how big of a scale desired
  # TODO ?  might be able to ditch this for logic that increments octaves.
  count = 1
  for interval in form:
    if count == num:
      break
    cur_note = find_interval(cur_note, interval)
    scale.append(cur_note)
    count += 1
  return scale

def find_chord(notes):
  num = notes.length()
  # starting from root note
  # construct scale of root note

# Return true if note is accidental
def isAccidental(name):
  if sharp in name:
    return True 

# Return true if note is natural
def isNatural(name):
  if sharp in name:
    return False
  

def play(path, duration):
  print ('play path is %s' % path)
  sound = pygame.mixer.Sound(path)
  mili = int(duration * 1000)
  sound.play(maxtime=mili)

def play_note(note, instrument, duration, solo=True):
  play(instrument + '/' + NOTES[note[0]] + '/notes/' + NOTES[note[0]] + '_' + str(note[1]) + WAV, duration)
#  if solo:
#    time.sleep(duration)

def play_from_mem(note, instrument, duration, solo=True):
  mili = int(duration * 1000)
  piano_notes[note[0]][note[1]-1].play(maxtime=mili)
#  if solo:
#    time.sleep(duration)

def play_chord(root_note, scale_type, chord_type, instrument, duration):
  #calculate chord
  chord = construct_chord(root_note, scale_type, chord_type)
  for note in chord:
    #print note
    #play_note(note, instrument, duration, solo=False)
    play_from_mem(note, instrument, duration, solo=False)
  #time.sleep(duration)


'''
play_chord((A,3),MINOR_SCALE,SEVENTH,GRAND_PIANO,1)
play_chord((A,3),MINOR_SCALE,SEVENTH,GRAND_PIANO,.5)
play_chord((A,3),MINOR_SCALE,SEVENTH,GRAND_PIANO,1)
play_chord((D,3),MAJOR_SCALE,TRIAD,GRAND_PIANO,2)
'''

#sc = construct_scale((B,4),MINOR_SCALE, 15)
#while True:
#  for n in sc:
  #print n
#    play_note(n, GRAND_PIANO, .3)
    #play_from_mem(n, GRAND_PIANO, .5)
#play_chord((A,4),MINOR_SCALE,SEVENTH,GRAND_PIANO,4)

  

#TODO start up page. add text drop downs for chords, scales, notes,





