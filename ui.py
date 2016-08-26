#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx
import chordwise
from chordwise import *
from random import randint


A_0_OFFSET = (1,1)
A_SHARP_0_OFFSET = (21,2)
B_0_OFFSET = (25,1)
C_1_OFFSET = (49,1)
C_SHARP_RELATIVE_OFFSET = (15,1)
D_RELATIVE_OFFSET = (24,0)
D_SHARP_RELATIVE_OFFSET = (43,1)
E_RELATIVE_OFFSET = (48,0)
F_RELATIVE_OFFSET = (72,0)
F_SHARP_RELATIVE_OFFSET = (85,1)
G_RELATIVE_OFFSET = (96,0)
G_SHARP_RELATIVE_OFFSET = (113,1)
A_RELATIVE_OFFSET = (120,0)
A_SHARP_RELATIVE_OFFSET = (140,1)
B_RELATIVE_OFFSET = (144,0)
C_RELATIVE_OFFSET = (196,0)
OCTAVE_OFFSET = 168

OFFSETS = [(0,0), (15,1), (24,0), (43,1), (48,0), (72,0),
           (85,1), (96,0), (113,1), (120,0), (140,1), (144,0)]
OCTAVE_OFFSET = 168



class MyPanel(wx.Panel):
    
    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw) 

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        
        #print 'event reached panel class'
        e.Skip()


class PlayButton(wx.Button):
    
    def __init__(self, *args, **kw):
        super(PlayButton, self).__init__(*args, **kw) 

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        #print self.NoteListBox.GetSelection()
        #chordwise.play_note((randint(0,11),4), GRAND_PIANO, 1) 
        e.Skip()
        #print 'event reached button class'
        
class NoteListBox(wx.ListBox):
    def __init__(self, *args, **kw):
        super(NoteListBox, self).__init__(*args, **kw)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=26)
        self.SetSelection(0)
    def OnSelect(self, e):
       e.Skip()

class OctaveListBox(wx.ListBox):
    def __init__(self, *args, **kw):
        super(OctaveListBox, self).__init__(*args, **kw)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=27)
        self.SetSelection(4)
    def OnSelect(self, e):
        e.Skip()

class ChordFormListBox(wx.ListBox):
    def __init__(self, *args, **kw):
        super(ChordFormListBox, self).__init__(*args, **kw)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=28)
        self.SetSelection(0)
    def OnSelect(self, e):
        e.Skip()

class ChordScaleListBox(wx.ListBox):
    def __init__(self, *args, **kw):
        super(ChordScaleListBox, self).__init__(*args, **kw)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=29)
        self.SetSelection(0)
    def OnSelect(self, e):
        e.Skip()

#def populateScale(self):

def playButtonExec(self):
    note = self.NoteListBox.GetSelection()
    octave = int(self.OctaveListBox.GetStringSelection())
    form = []
    scale = []

    # TODO make this logic come from dictionaries that have list of options mapped to choices in listbox
    if (self.ChordScaleListBox.GetStringSelection() == 'Note'):
        toSelect = chordwise.play_from_mem((note, octave), GRAND_PIANO, self.spinctrl.GetValue())
        self.piano.highlightKey(toSelect)
    else:
        if (self.ChordScaleListBox.GetStringSelection() == 'Minor'):
            scale = MINOR_SCALE
        else:
            scale = MAJOR_SCALE

        if (self.ChordFormListBox.GetStringSelection() == 'Triad'):
            form = TRIAD
        else:
            form = SEVENTH

        toSelect = play_chord((note, octave), scale, form, GRAND_PIANO, self.spinctrl.GetValue())
        self.piano.highlightKeys(toSelect)


#def constructScaleExec(self):

def initScaleText(self, mpnl):
    self.pos_1 = wx.StaticText(mpnl, -1, "1", (50,0), style=wx.ALIGN_CENTRE)
    #self.pos_2 = wx.StaticText(mpnl, -1, "2")
    #self.pos_3 =
    #self.pos_4
    #self.pos_5
    #self.pos_6
    #self.pos_7

def createBitmap(mpnl, path, x_pos, y_pos):
    return wx.StaticBitmap(mpnl, -1, wx.Bitmap(path, wx.BITMAP_TYPE_ANY), pos=(x_pos, y_pos))


class InteractivePiano:

     def __init__(self, mpnl, x_pos, y_pos):
         self.piano = wx.StaticBitmap(mpnl, -1, wx.Bitmap(os.path.join("images","88_key.png"), wx.BITMAP_TYPE_ANY), pos=(x_pos, y_pos))
         self.panel = mpnl
         self.x_pos = x_pos
         self.y_pos = y_pos
         self.selectedKeys = []

#USE CALLBACK FUNCTION TO SPAWN A THREAD WHICH EXITS AND DELETES CREATED NOTES
     def highlightKey(self, note):
         #if not noteValid(note):
         #    print ("Note %s invalid, cannot highlight" % str(note))

         n = note[0]
         octave = note[1]
         note_str = NOTES[n]

         if octave == 0:
            # start at a
            if isAccidental(note_str):
                bitmap = createBitmap(os.path.join("images","88_key_accidental.png"), self.x_pos + A_SHARP_0_OFFSET[0], self.y_pos +  A_SHARP_0_OFFSET[1])
                self.selectedKeys.append(bitmap)
            # TODO HANDLE ELSE CASE FOR A and B 0

         elif octave < 8:
            # start at c1
            #x_offset = self.x_pos + C_1_OFFSET[0] + OFFSETS[n][0] + (octave - 1) * OCTAVE_OFFSET
            x_offset = self.x_pos + C_1_OFFSET[0] + OFFSETS[n][0] + (octave - 1) * OCTAVE_OFFSET - octave/2
            y_offset = self.y_pos + C_1_OFFSET[1] + OFFSETS[n][1]
            if isAccidental(note_str):
                path = os.path.join("images","88_key_accidental.png")
            else:
                print note_str
                path = os.path.join("images","88_key_" + note_str + ".png")
            print path
            bitmap = createBitmap(self.panel, path, x_offset, y_offset)
            self.selectedKeys.append(bitmap)
         #else:
             # octave 8 just c

     def highlightKeys(self, notes):
         for note in notes:
             self.highlightKey(note)

     def clearKeys(self):
         for key in self.selectedKeys:
             key.Destroy()
         self.selectedKeys[:] = []



class HomePage(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(HomePage, self).__init__(*args, **kw) 
        
        self.InitUI()
        
        
    def InitUI(self):

        mpnl = MyPanel(self)

        PlayButton(mpnl, label='Play', pos=(15, 15))
        self.ScaleCreatorButton = wx.Button(mpnl, label='Construct Scale', pos=(15,200))
        self.NoteListBox = NoteListBox(mpnl, 26, (200,0), (100, 245), NOTES, wx.LB_SINGLE)
        self.OctaveListBox = OctaveListBox(mpnl, 27, (300,0), (100, 185), OCTAVES, wx.LB_SINGLE)
        self.ChordScaleListBox = ChordFormListBox(mpnl, 28, (400,0), (100, 130), CHORD_SCALES, wx.LB_SINGLE)
        self.ChordFormListBox = ChordFormListBox(mpnl, 29, (500,0), (100, 130), CHORD_FORMS, wx.LB_SINGLE)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        #TODO initialize all text boxes required for scales
        initScaleText(self,mpnl)


        self.spinctrl = wx.SpinCtrl(mpnl, 30, '3', (120, 20), (60, -1), wx.SP_ARROW_KEYS, 1, 10, 3)
        #self.piano = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key.png", wx.BITMAP_TYPE_ANY), pos=(15,300))
        self.piano = InteractivePiano(mpnl, 15,300)
        #self.piano.highlightKey((4,2))
        #self.piano.highlightKey((0,4))
        #self.piano.highlightKey((7,4))
        #self.piano.highlightKeys([(4,1),(4,2), (4,3), (4,4), (4,5),(4,6), (4,7)])
        '''
        self.a_1_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_a_1.png", wx.BITMAP_TYPE_ANY), pos=(16,301))
        self.a_sharp_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(36,302))
        self.b_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_b.png", wx.BITMAP_TYPE_ANY), pos=(40,301))
        self.c_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_c.png", wx.BITMAP_TYPE_ANY), pos=(64,301))
        self.c_sharp_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(79,302))
        self.d_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_d.png", wx.BITMAP_TYPE_ANY), pos=(88,301))
        self.d_sharp_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(107,302))
        self.e_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_b.png", wx.BITMAP_TYPE_ANY), pos=(112,301))
        self.f_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_c.png", wx.BITMAP_TYPE_ANY), pos=(136,301))
        self.f_sharp_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(149,302))
        self.g_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_g.png", wx.BITMAP_TYPE_ANY), pos=(160,301))
        self.g_sharp_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(177,302))
        self.a_2_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_a.png", wx.BITMAP_TYPE_ANY), pos=(184,301))
        self.a_sharp_2 = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_accidental.png", wx.BITMAP_TYPE_ANY), pos=(204,302))
        self.b2_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_b.png", wx.BITMAP_TYPE_ANY), pos=(208,301))
        '''

     #   self.a_1_key = wx.StaticBitmap(mpnl, -1, wx.Bitmap("88_key_c.png", wx.BITMAP_TYPE_ANY), pos=(15+49+168,301))

        self.SetTitle('Chordwise')
        self.Centre()
        self.Show(True)  
#TODO HAVE OPTION TO PLAY A SCALE WITH KEYS AND DISPLAY

    def OnButtonClicked(self, e):
        button = e.GetEventObject()
        label = button.GetLabel()

        if (label == "Play"):
            self.piano.clearKeys()
            playButtonExec(self)
        elif (label == "Construct Scale"):
            constructScaleExec(self)
        # GetSelection returns 0 based integer position



def main():
    
    ex = wx.App()
    HomePage(None,size=(1273,485))
    ex.MainLoop()    


if __name__ == '__main__':
    main()  
