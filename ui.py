#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx
import chordwise
from chordwise import *
from random import randint


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
        self.SetSelection(0)
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

class HomePage(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(HomePage, self).__init__(*args, **kw) 
        
        self.InitUI()
        
        
    def InitUI(self):

        mpnl = MyPanel(self)

        PlayButton(mpnl, label='Play', pos=(15, 15))
        self.ScaleCreatorButton = wx.Button(mpnl, label='Construct Scale', pos=(15,200))
        self.NoteListBox = NoteListBox(mpnl, 26, (200,0), (100, 245), NOTES, wx.LB_SINGLE)
        self.OctaveListBox = OctaveListBox(mpnl, 27, (300,0), (100, 165), OCTAVES, wx.LB_SINGLE)
        self.ChordScaleListBox = ChordFormListBox(mpnl, 28, (400,0), (100, 130), CHORD_SCALES, wx.LB_SINGLE)
        self.ChordFormListBox = ChordFormListBox(mpnl, 29, (500,0), (100, 130), CHORD_FORMS, wx.LB_SINGLE)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        self.spinctrl = wx.SpinCtrl(mpnl, 30, '3', (120, 20), (60, -1), wx.SP_ARROW_KEYS, 1, 10, 3)

        self.SetTitle('Chordwise')
        self.Centre()
        self.Show(True)  
#TODO HAVE OPTION TO PLAY A SCALE WITH KEYS AND DISPLAY

    def OnButtonClicked(self, e):
        button = e.GetEventObject()
        print button.GetLabel()
        # GetSelection returns 0 based integer position
        note = self.NoteListBox.GetSelection()
        octave = int(self.OctaveListBox.GetStringSelection())
        form = []
        scale = []
        #TODO make this logic come from dictionaries that have list of options mapped to choices in listbox
        if (self.ChordScaleListBox.GetStringSelection() == 'Note'):
            chordwise.play_from_mem((note, octave), GRAND_PIANO, self.spinctrl.GetValue())
        else:
            if (self.ChordScaleListBox.GetStringSelection() == 'Minor'):
                scale = MINOR_SCALE
            else:
                scale = MAJOR_SCALE

            if (self.ChordFormListBox.GetStringSelection() == 'Triad'):
                form = TRIAD
            else:
                form = SEVENTH

            play_chord((note,octave),scale,form,GRAND_PIANO,self.spinctrl.GetValue())


def main():
    
    ex = wx.App()
    HomePage(None,size=(600,350))
    ex.MainLoop()    


if __name__ == '__main__':
    main()  
