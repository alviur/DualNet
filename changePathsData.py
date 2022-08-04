# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 13:29:46 2022

@author: Alex
"""
import csv

mainPath = 'C:\\Users\DELL\\Documents\\GitHub\\DualNet\\data\\'

newPath = '/data/Datasets/miniImagenet/'

# Train
with open(mainPath+"mini_cl_train.csv", "w") as fileW:
    fileW.write('File,Label\n')

    file = open(mainPath+'mini_cl_train_old.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        name = row[0]
        imgName = name[37:]
        folder = name [37:46]
        print(imgName,folder)
        fileW.write(newPath+'train/'+folder+'/'+imgName+','+row[1]+'\n')
        
# Val        

with open(mainPath+"mini_val_train.csv", "w") as fileW:
    fileW.write('File,Label\n')

    file = open(mainPath+'mini_val_train_old.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        name = row[0]
        imgName = name[37:]
        folder = name [37:46]
        print(imgName,folder)
        fileW.write(newPath+'val/'+folder+'/'+imgName+','+row[1]+'\n')
        
with open(mainPath+"mini_val_test.csv", "w") as fileW:
    fileW.write('File,Label\n')

    file = open(mainPath+'mini_val_test_old.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        name = row[0]
        imgName = name[37:]
        folder = name [37:46]
        print(imgName,folder)
        fileW.write(newPath+'val/'+folder+'/'+imgName+','+row[1]+'\n')
        
# Test

with open(mainPath+"mini_cl_test.csv", "w") as fileW:
    fileW.write('File,Label\n')

    file = open(mainPath+'mini_cl_test_old.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        name = row[0]
        imgName = name[37:]
        folder = name [37:46]
        print(imgName,folder)
        fileW.write(newPath+'test/'+folder+'/'+imgName+','+row[1]+'\n')