#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:25:07 2019

@author: rodrigocasale
"""
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

wb = load_workbook('songs.xlsx', read_only=True)
sh = wb["sheet1"]

canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 20)

cellArtist = 'A2'
i = 1
while(sh[cellArtist].value != None):
    i += 1
    cellArtist = 'A' + str(i)
    cellSong = 'B' + str(i)
        
    """for x in range(2,12):
        cellArtist2 = 'A' + str(x)
        if(cellArtist != cellArtist2):
            if(sh[cellArtist].value == sh[cellArtist2].value):
                print(sh[cellArtist].value + " from "+ cellArtist +" is the same as " + sh[cellArtist2].value+ " from "+ cellArtist2)
    """         
    if(sh[cellArtist].value != None):
        canvas.drawString(100,750-(20*i), str(sh[cellArtist].value) + " - " + str(sh[cellSong].value) )
    
    

canvas.save()