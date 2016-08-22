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
    pygame.mixer.set_num_channels(128)

# Constants

GRAND_PIANO = 'GRAND_PIANO'
NOTES = ['C','C_SHARP', 'D','D_SHARP','E','F','F_SHARP','G','G_SHARP','A','A_SHARP','B']
CHORD_SCALES = ['Major', 'Minor','Note']
CHORD_FORMS = ['Triad', 'Seventh']
#TODO create dictionary to map these to the constants so that the conversion doesn't have to happen in the UI file


A_FLAT = 8
A = 9
A_SHARP = 10
B_FLAT = 10
B = 11
C = 0
C_SHARP = 1
D_FLAT = 1
D = 2
D_SHARP = 3
E_FLAT = 3
E = 4
F = 5
F_SHARP = 6
G_FLAT = 6
G = 7
G_SHARP = 8

WAV = '.WAV'
SHARP = 'SHARP'
# Need to start at 1 so we don't jump around (left of keyboard)
# TODO Fixing starting at 1 now, making it C based instead of A based should fix
OCTAVES = ['0','1','2','3','4','5','6','7','8']
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

'''
# old sound library
piano_notes = []
for note in NOTES:
    note_list = []
    for octave in OCTAVES:
        path = os.path.join('grand_piano', note, 'notes', note + "_" + octave + WAV)
        if (os.path.exists(path)):
            sound = pygame.mixer.Sound(path)
            note_list.append(sound)
    piano_notes.append(note_list)
'''
# new sound library
piano_notes = []
piano_sounds = []
for octave in OCTAVES:
    note_list = []
    sound_list = []
    for note in NOTES:
        path = os.path.join('grand_piano', octave + '_' + note + WAV)
        if os.path.exists(path):
            print path
            note_list.append(note)
            sound = pygame.mixer.Sound(path)
            sound_list.append(sound)
    piano_notes.append(note_list)
    piano_sounds.append(sound_list)

# Sharp a note
def sharp(note):
    return (note + 1) % 12

# Flat a note
def flat(note):
    note = note - 1
    return note if note > 0 else 11

# Find note that is interval steps higher
def find_interval(note, interval):
    # note = ((note[0] + interval) % 12)
    # octave = note[1] if (note[0] + interval) < 12 else note[1] + 1
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
    path = os.path.join(instrument,NOTES[note[0]], "notes", NOTES[note[0]], "_", str(note[1]), WAV)
    print path
    play(instrument + '/' + NOTES[note[0]] + '/notes/' + NOTES[note[0]] + '_' + str(note[1]) + WAV, duration)
#  if solo:
#    time.sleep(duration)

def play_from_mem(note, instrument, duration):
    mili = int(duration * 1000)
    # if note exists in octave's notes
    if (NOTES[note[0]] in piano_notes[note[1]]):
        #find correct index, octaves 0 and 8 are misleading
        note_idx = piano_notes[note[1]].index(NOTES[note[0]])
        piano_sounds[note[1]][note_idx].play(maxtime=mili)
    else:
        print ('octave %s for note %s is out of range' % (str(note[1]), NOTES[note[0]]))


def play_chord(root_note, scale_type, chord_type, instrument, duration):
    #calculate chord
    chord = construct_chord(root_note, scale_type, chord_type)
    for note in chord:
        print note
        #play_note(note, instrument, duration)
        play_from_mem(note, instrument, duration)
        #time.sleep(duration)


#TODO start up page. add text drop downs for chords, scales, notes,





