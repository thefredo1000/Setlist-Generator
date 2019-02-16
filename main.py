#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:25:07 2019

@author: rodrigocasale
"""
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter


def randomize(array, i, lenght):
    i = i - 1
    a = 0
    b = a + 1
    
    artist = []
    song = []
    newArray = [artist, song]
    
    isFull = False
    while(isFull == False):
        if(array[0][a] == array[0][b] or array[2][a] == array[2][b]):
            print(array[0][a]+ array[0][b])
            newSong = array[1][10 - a]
            array[1][lenght - a] = array[1][a]
            array[1][a] = newSong
            newArtist = array[0][10 - a]
            array[0][lenght - a] = array[0][a]
            array[0][a] = newArtist
            
        if(a <=8):
            a = a + 1
            b = b + 1
            i = i - 1
        elif(a>8):
            isFull =True
    array[0] = array[0][1:]
    array[1] = array[1][1:]
    newArray[0] = array[0]
    newArray[1] = array[1]
    return newArray

def main(): 
    from reportlab.pdfgen import canvas
    artist = []
    song = []
    album = []
    genre = []
    completeArray = [artist, song, album, genre]
    finalArray = [artist, song]
    
    wb = load_workbook('songs.xlsx', read_only=True)
    sh = wb["sheet1"]
    
    canvas = canvas.Canvas("form.pdf", pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica-Bold', 40)
    canvas.drawString(100,690, 'Setlist')
    
    canvas.setFont('Helvetica', 20)
    
    cellArtist = 'A2'
    i = 1
    while(sh[cellArtist].value != None):
        
        i += 1
        cellArtist = 'A' + str(i)
        cellSong = 'B' + str(i)
        cellAlbum = 'C' + str(i)
        cellGenre = 'D' + str(i)
            
        """for x in range(2,12):
            cellArtist2 = 'A' + str(x)
            if(cellArtist != cellArtist2):
                if(sh[cellArtist].value == sh[cellArtist2].value):
                    print(sh[cellArtist].value + " from "+ cellArtist +" is the same as " + sh[cellArtist2].value+ " from "+ cellArtist2)
        """         
        
        if(sh[cellArtist].value != None):
            print("")
        
        artist.append(str(sh[cellArtist].value))
        song.append(str(sh[cellSong].value))
        album.append(str(sh[cellAlbum].value))
        genre.append(str(sh[cellGenre].value))
        
    finalArray = randomize(completeArray, i, len(completeArray[0]) - 1)
    for i in range(0, len(finalArray[0])):
        if(i >= 9):
            bullet = str(i + 1) + ') '
        else:
            bullet = str(i + 1) + ') ' + '  '
        canvas.drawString(100,665-(20*i),  bullet + finalArray[0][i] + " - " + finalArray[1][i] )
    
    canvas.save()

main()