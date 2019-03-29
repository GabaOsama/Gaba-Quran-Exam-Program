import random
import datetime
from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END,filedialog
from tkinter.messagebox import showinfo
from tkinter import *
import tkinter as tk
import webbrowser



class Exam2(Tk):
    
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Hifdh Spot Test App')
        self.geometry('700x665')
        
        self.make_widgets()
        self.lst=[]
        self.count=float(0)
        self.lst2=[]
        self.memocount=float(0.0)
        self.tajcount=float(0.0)
        self.stutcount=float(0.0)
        self.show=[]
       
        
        
        
        
    def QuranTest(self):
          

          if self.variable.get()=='':
              
           showinfo(title='Error!',message='You must enter all of the juz that the student is being tested on!')
           return 
          if self.variable.get()=='Select a juz to add' or self.variable.get()=='Remove all':
              showinfo(title='Error!',message='No juz selected')
              
    
              return
          elif 'Quarter' in str(self.variable.get()):
            
            pages=['1st','2nd','3rd','4th','5th']
            random.shuffle(pages)
            random.shuffle(pages)
            random.shuffle(pages)
            
            beg=['Beginning','Middle']
            var2=random.choice(beg)
            

            page=random.choice(pages)
            
            self.lst.append( '{}. {} Page.'.format(self.variable.get(),page,end='/n'))
            self.show.append((self.variable.get()))
            self.showlabel.config(text='{}'.format(self.show))
            self.variable.set(self.mylst[0])
            

                
                
                
        
      
            

          else:
            quarter=['1st','2nd','3rd','4th']
            pages=['1st','2nd','3rd','4th','5th']
            random.shuffle(quarter)
            random.shuffle(quarter)
            random.shuffle(quarter)
            random.shuffle(pages)
            random.shuffle(pages)
            random.shuffle(pages)
            random.shuffle(pages)
            random.shuffle(pages)
            beg=['Beginning','Middle']
            var2=random.choice(beg)
            var=random.choice(quarter)
            page=random.choice(pages)

            self.lst.append( '{} Juz. {} Quarter. {} Page.'.format(self.variable.get(),var,page,end='/n'))
            self.show.append(self.variable.get())
            self.showlabel.config(text='{}'.format(self.show))
            self.variable.set(self.mylst[0])
            
    
           
            
           
     
         
    def getData(self):

        

        if self.lst==[]:
            showinfo(title='No Questions!',message='No more questions to ask at this time!')
            return
        
        else:
            
                
            random.shuffle(self.lst)    
            self.var=random.choice(self.lst)
            self.test.config(text='{}'.format(self.var))
            
        
            
          
            #1st Juz
            if self.var==str('1st Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('1st Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('1st Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('1st Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('1st Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('1st Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('1st Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('1st Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('1st Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('1st Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('1st Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('1st Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('1st Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('1st Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('1st Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('1st Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('1st Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('1st Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('1st Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('1st Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #2nd Juz
            elif self.var==str('2nd Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:142')
            elif  self.var==str('2nd Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:146')
            elif  self.var==str('2nd Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:154')
            elif self.var==str('2nd Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:164')
            elif self.var==str('2nd Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:170')

            elif self.var==str('2nd Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:177')
            elif  self.var==str('2nd Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:182')
            elif  self.var==str('2nd Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:187')
            elif self.var==str('2nd Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:191')
            elif self.var==str('2nd Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:197')

            elif self.var==str('2nd Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:203')
            elif  self.var==str('2nd Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:211')
            elif  self.var==str('2nd Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:216')
            elif self.var==str('2nd Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:220')
            elif self.var==str('2nd Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:225')

            elif self.var==str('2nd Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:231')
            elif  self.var==str('2nd Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:234')
            elif  self.var==str('2nd Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:238')
            elif self.var==str('2nd Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:246')
            elif self.var==str('2nd Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:249')

        #3rd Juz
            elif self.var==str('3rd Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:253')
            elif  self.var==str('3rd Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:257')
            elif  self.var==str('3rd Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:260')
            elif self.var==str('3rd Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:265')
            elif self.var==str('3rd Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:270')

            elif self.var==str('3rd Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:275')
            elif  self.var==str('3rd Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:282')
            elif  self.var==str('3rd Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:283')
            elif self.var==str('3rd Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:1')
            elif self.var==str('3rd Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:10')

            elif self.var==str('3rd Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#3:16')
            elif  self.var==str('3rd Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#3:23')
            elif  self.var==str('3rd Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#3:30')
            elif self.var==str('3rd Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:38')
            elif self.var==str('3rd Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:46')

            elif self.var==str('3rd Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#3:53')
            elif  self.var==str('3rd Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#3:62')
            elif  self.var==str('3rd Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#3:71')
            elif self.var==str('3rd Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:78')
            elif self.var==str('3rd Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:84')

        #4th Juz
            elif self.var==str('4th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#3:93')
            elif  self.var==str('4th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#3:101')
            elif  self.var==str('4th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#3:109')
            elif self.var==str('4th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:116')
            elif self.var==str('4th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:122')

            elif self.var==str('4th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#3:133')
            elif  self.var==str('4th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#3:141')
            elif  self.var==str('4th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#3:149')
            elif self.var==str('4th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:154')
            elif self.var==str('4th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:158')

            elif self.var==str('4th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#3:166')
            elif  self.var==str('4th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#3:174')
            elif  self.var==str('4th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#3:181')
            elif self.var==str('4th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#3:187')
            elif self.var==str('4th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#3:195')

            elif self.var==str('4th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#4:1')
            elif  self.var==str('4th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#4:7')
            elif  self.var==str('4th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#4:12')
            elif self.var==str('4th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#4:15')
            elif self.var==str('4th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#4:20')

        #5th Juz
            elif self.var==str('5th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#4:24')
            elif  self.var==str('5th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#4:27')
            elif  self.var==str('5th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#4:34')
            elif self.var==str('5th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#4:38')
            elif self.var==str('5th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#4:45')

            elif self.var==str('5th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#4:52')
            elif  self.var==str('5th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#4:60')
            elif  self.var==str('5th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#4:66')
            elif self.var==str('5th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#4:75')
            elif self.var==str('5th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#4:80')

            elif self.var==str('5th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#4:87')
            elif  self.var==str('5th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#4:92')
            elif  self.var==str('5th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#4:95')
            elif self.var==str('5th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#4:102')
            elif self.var==str('5th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#4:106')

            elif self.var==str('5th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#4:114')
            elif  self.var==str('5th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#4:122')
            elif  self.var==str('5th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#4:128')
            elif self.var==str('5th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#4:135')
            elif self.var==str('5th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#4:141')

        #6th Juz
            elif self.var==str('6th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('6th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('6th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('6th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('6th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('6th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('6th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('6th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('6th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('6th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('6th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('6th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('6th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('6th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('6th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('6th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('6th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('6th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('6th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('6th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #7th Juz
            elif self.var==str('7th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('7th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('7th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('7th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('7th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('7th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('7th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('7th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('7th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('7th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('7th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('7th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('7th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('7th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('7th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('7th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('7th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('7th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('7th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('7th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #8th Juz
            elif self.var==str('8th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('8th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('8th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('8th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('8th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('8th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('8th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('8th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('8th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('8th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('8th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('8th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('8th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('8th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('8th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('8th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('8th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('8th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('8th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('8th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #9th Juz
            elif self.var==str('9th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('9th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('9th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('9th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('9th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('9th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('9th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('9th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('9th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('9th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('9th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('9th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('9th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('9th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('9th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('9th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('9th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('9th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('9th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('9th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

         #10th Juz
            elif self.var==str('10th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('10th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('10th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('10th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('10th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('10th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('10th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('10th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('10th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('10th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('10th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('10th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('10th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('10th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('10th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('10th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('10th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('10th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('10th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('10th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #11th Juz
            elif self.var==str('11th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('11th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('11th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('11th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('11th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('11th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('11th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('11th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('11th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('11th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('11th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('11th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('11th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('11th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('11th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('11th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('11th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('11th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('11th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('11th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #12th Juz
            elif self.var==str('12th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('12th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('12th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('12th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('12th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('12th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('12th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('12th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('12th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('12th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('12th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('12th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('12th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('12th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('12th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('12th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('12th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('12th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('12th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('12th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #13th Juz
            elif self.var==str('13th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('13th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('13th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('13th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('13th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('13th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('13th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('13th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('13th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('13th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('13th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('13th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('13th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('13th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('13th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('13th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('13th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('13th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('13th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('13th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #14th Juz
            elif self.var==str('14th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('14th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('14th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('14th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('14th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('14th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('14th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('14th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('14th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('14th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('14th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('1st Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('14th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('14th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('14th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('14th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('14th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('14th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('14th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('14th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #15th Juz
            elif self.var==str('15th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('15th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('15th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('15th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('15th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('15th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('15th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('15th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('15th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('15th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('15th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('15th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('15th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('15th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('15th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('15th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('15th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('15th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('15th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('15th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #16th Juz
            elif self.var==str('16th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('16th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('16th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('16th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('16th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('16th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('16th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('16th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('16th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('16th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('16th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('16th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('16th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('16th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('16th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('16th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('16th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('16th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('16th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('16th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #17th Juz
            elif self.var==str('17th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('17th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('17th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('17th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('17th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('17th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('17th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('17th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('17th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('17th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('17th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('17th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('17th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('17th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('17th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('17th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('17th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('17th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('17th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('17th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #18th Juz
            elif self.var==str('18th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('18th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('18th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('18th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('18th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('18th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('18th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('18th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('18th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('18th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('18th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('18th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('18th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('18th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('18th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('18th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('18th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('18th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('18th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('19th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #19th Juz
            elif self.var==str('19th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('19th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('19th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('19th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('19th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('19th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('19th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('19th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('19th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('19th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('19th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('19th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('19th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('19th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('19th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('19th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('19th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('19th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('19th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('19th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #20th Juz
            elif self.var==str('20th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('20th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('20th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('20th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('20th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('20th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('20th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('20th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('20th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('20th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('20th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('20th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('20th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('20th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('20th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('20th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('20th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('20th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('20th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('20th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #21st Juz
            if self.var==str('21st Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('21st Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('21st Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('21st Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('21st Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('21st Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('21st Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('21st Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('21st Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('21st Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('21st Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('21st Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('21st Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('21st Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('21st Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('21st Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('21st Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('21st Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('21st Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('21st Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #22nd Juz
            if self.var==str('22nd Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('22nd Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('22nd Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('22nd Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('22nd Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('22nd Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('22nd Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('22nd Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('22nd Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('22nd Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('22nd Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('22nd Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('22nd Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('22nd Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('22nd Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('22nd Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('22nd Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('22nd Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('22nd Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('22nd Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

         #23rd Juz
            if self.var==str('23rd Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('23rd Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('23rd Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('23rd Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('23rd Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('23rd Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('23rd Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('23rd Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('23rd Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('23rd Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('23rd Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('23rd Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('23rd Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('23rd Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('23rd Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('23rd Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('23rd Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('23rd Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('23rd Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('23rd Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')
        #24th Juz
            elif self.var==str('24th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('24th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('24th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('24th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('24th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('24th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('24th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('24th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('24th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('24th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('24th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('24th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('24th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('24th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('24th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('24th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('24th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('24th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('24th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('24th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #25th Juz
            elif self.var==str('25th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('25th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('25th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('25th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('25th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('25th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('25th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('25th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('25th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('25th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('25th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('25th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('25th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('25th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('25th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('25th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('25th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('25th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('25th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('25th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #26th Juz
            elif self.var==str('26th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:1')
            elif  self.var==str('26th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:6')
            elif  self.var==str('26th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:17')
            elif self.var==str('26th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:25')
            elif self.var==str('26th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:30')

            elif self.var==str('26th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:38')
            elif  self.var==str('26th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:49')
            elif  self.var==str('26th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:58')
            elif self.var==str('26th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:62')
            elif self.var==str('26th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:70')

            elif self.var==str('26th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:77')
            elif  self.var==str('26th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:84')
            elif  self.var==str('26th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:89')
            elif self.var==str('26th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:94')
            elif self.var==str('26th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:102')

            elif self.var==str('26th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#2:106')
            elif  self.var==str('26th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#2:113')
            elif  self.var==str('26th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#2:120')
            elif self.var==str('26th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#2:127')
            elif self.var==str('26th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#2:135')

        #27th Juz
            elif self.var==str('27th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#51:31')
            elif  self.var==str('27th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#51:52')
            elif  self.var==str('27th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#52:15')
            elif self.var==str('27th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#52:32')
            elif self.var==str('27th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#53:1')

            elif self.var==str('27th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#53:27')
            elif  self.var==str('27th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#53:45')
            elif  self.var==str('27th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#54:7')
            elif self.var==str('27th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#54:28')
            elif self.var==str('27th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#54:50')

            elif self.var==str('27th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#55:17')
            elif  self.var==str('27th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#55:41')
            elif  self.var==str('27th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#55:68')
            elif self.var==str('27th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#56:17')
            elif self.var==str('27th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#56:51')

            elif self.var==str('27th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#56:77')
            elif  self.var==str('27th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#57:4')
            elif  self.var==str('27th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#57:12')
            elif self.var==str('27th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#57:19')
            elif self.var==str('27th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#57:25')

        #28th Juz
            elif self.var==str('28th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#58:1')
            elif  self.var==str('28th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#58:7')
            elif  self.var==str('28th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#58:12')
            elif self.var==str('28th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#58:22')
            elif self.var==str('28th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#59:4')

            elif self.var==str('28th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#59:10')
            elif  self.var==str('28th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#59:17')
            elif  self.var==str('28th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#60:1')
            elif self.var==str('28th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#60:6')
            elif self.var==str('28th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#60:12')

            elif self.var==str('28th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#61:6')
            elif  self.var==str('28th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#62:1')
            elif  self.var==str('28th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#62:9')
            elif self.var==str('28th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#63:5')
            elif self.var==str('28th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#64:1')

            elif self.var==str('28th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#64:10')
            elif  self.var==str('28th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#65:1')
            elif  self.var==str('28th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#65:6')
            elif self.var==str('28th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#66:1')
            elif self.var==str('28th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#66:8')

        #29th Juz
            elif self.var==str('29th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#67:1')
            elif  self.var==str('29th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#67:13')
            elif  self.var==str('29th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#67:27')
            elif self.var==str('29th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#68:16')
            elif self.var==str('29th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#68:43')
                
            elif self.var==str('29th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#69:9')
            elif self.var==str('29th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#69:35')
            elif  self.var==str('29th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#70:11')
            elif  self.var==str('29th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#70:40')
            elif self.var==str('29th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#71:11')
                
            elif self.var==str('29th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#72:1')
            elif self.var==str('29th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#72:14')
            elif  self.var==str('29th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#73:1')
            elif  self.var==str('29th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#73:20')
            elif self.var==str('29th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#74:18')
                
            elif self.var==str('29th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#74:48')
            elif self.var==str('29th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#75:20')
            elif  self.var==str('29th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#76:6')
            elif  self.var==str('29th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#76:26')
            elif self.var==str('29th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#77:20')
           

         #30th Juz
            elif self.var==str('30th Juz. 1st Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#78:1')
            elif  self.var==str('30th Juz. 1st Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#78:31')
            elif  self.var==str('30th Juz. 1st Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#79:16')
            elif self.var==str('30th Juz. 1st Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#80:1')
            elif self.var==str('30th Juz. 1st Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#81:1')

            elif self.var==str('30th Juz. 2nd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#82:1')
            elif  self.var==str('30th Juz. 2nd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#82:7')
            elif  self.var==str('30th Juz. 2nd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#83:35')
            elif self.var==str('30th Juz. 2nd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#85:1')
            elif self.var==str('30th Juz. 2nd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#86:1')

            elif self.var==str('30th Juz. 3rd Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#87:16')
            elif  self.var==str('30th Juz. 3rd Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#89:1')
            elif  self.var==str('30th Juz. 3rd Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#89:24')
            elif self.var==str('30th Juz. 3rd Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#91:1')
            elif self.var==str('30th Juz. 3rd Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#92:15')

            elif self.var==str('30th Juz. 4th Quarter. 1st Page.'):
                webbrowser.open('http://tanzil.net/#95:1')
            elif  self.var==str('30th Juz. 4th Quarter. 2nd Page.'):
                webbrowser.open('http://tanzil.net/#97:1')
            elif  self.var==str('30th Juz. 4th Quarter. 3rd Page.'):
                webbrowser.open('http://tanzil.net/#98:8')
            elif self.var==str('30th Juz. 4th Quarter. 4th Page.'):
                webbrowser.open('http://tanzil.net/#103:1')
            elif self.var==str('30th Juz. 4th Quarter. 5th Page.'):
                webbrowser.open('http://tanzil.net/#106:1')

        

            else:
                return

   
                    
            
                    
            
            
            
            
                    
    def examMath(self):
      
        if len(self.lst)==0:
            
                showinfo(title='Error!',message='Cannot calculate total. No question asked.')
                return
            
        
            
            
        else:
            
                try:
            
            
                    self.lst.remove(self.var)
                    mem=float(self.memocount)*5
                    t=float(self.tajcount)*2
                    s=float(self.stutcount)*0.5
                    total=float(mem)+float(t)+float(s)
                    result=100
                    self.answer= float(result) - float(total)
                    self.count+=float(self.answer)
                
                    self.lst2.append('-->Tested on: {} \nAMOUNT OF MEMORIZATION MISTAKES: {}\nAMOUNT OF TAJWEED MISTAKES: {} \nAMOUNT OF STUTTER MISTAKES: {} \nScore: {}/100\n '.format(str(self.var),self.memocount,self.tajcount,self.stutcount,float(self.answer)))
                    self.memo.config(text=float(0.0))
                    self.tajweed.config(text=float(0.0))
                    self.stutter.config(text=float(0.0))
                    var=''
                    self.test.config(text='{}'.format(var))
                    showinfo(title='Score',message='Score for this question: {}'.format(float(self.answer)))
                    self.memocount=float(0.0)
                    self.tajcount=float(0.0)
                    self.stutcount=float(0.0)
                    
                    self.test.config(text='None')
                   
                    
                except:
                    showinfo(title='Error!',message='Cannot calculate. No question asked.')
                    return
            
                
                
           
            
    def writeFile(self):

        if self.sname.get()=='':
                showinfo(title='Enter Name!',message='Please enter the name of the student.')
                return

        
        try:
            var=len(self.lst2)
            
            scores= float(self.count)//float(var)
        
            if scores < 60:
                var2 = 'F'
            if scores >= 60 and scores< 70:
                var2 = 'D'
            if scores >= 70 and scores< 80:
                var2 = 'C'
            if scores >= 80 and scores< 90:
                var2 = 'B'
            if scores >= 90:
                var2 = 'A'
            
            
            outfile=open('Exam-'+self.sname.get()+'.txt','w')
            outfile.write("{}'s Exam Report.\n \n{}\n \n".format(self.sname.get(),self.now))
            for i in self.lst2:
                outfile.write('-'*80+'\n')
                outfile.write('{}\n'.format(i))
            outfile.write('-'*80+'\n')
            outfile.write('-->Total Score Average: {0:.2f} (This score has been rounded up.)\n-->Letter Grade: {1}'.format(float(scores),var2))
            outfile.close()
            showinfo(title='Report Made!',message="Thank you! A file by the name of 'Exam-{}.txt' has been created and is ready to be printed!".format(self.sname.get())) 
            self.sname.delete(0,END)
            
            self.lst2.clear()
            self.memocount=float(0.0)
            
            
            self.tajcount=float(0.0)
            self.stutcount=float(0.0)
            self.count=float(0.0)
            self.answer=0
            self.test.config(text='None')
            self.show.clear()
            self.lst.clear()
            self.showlabel.config(text='No Juz Added')
            self.variable.set(text='{}'.format(self.mylst[0]))
      

                
        except:
              showinfo(title='Error!',message="Please select a juz to add!")                                                      
              return
    def memoincrease(self):
        
        val=float(self.memocount+1)
        self.memo.config(text='{}'.format(float(val)))
        self.memocount=float(val)
    def memodecrease(self):
        val=float(self.memocount)-1
        if float(val)<0:
            showinfo(title='Error!',message='Cannot go below 0!')
            return
        else:
        

            self.memo.config(text='{}'.format(float(val)))
            self.memocount=float(val)
    def tajincrease(self):
        
        val=self.tajcount+1
        self.tajweed.config(text='{}'.format(val))
        self.tajcount=val
    def tajdecrease(self):
        val=self.tajcount-1
        if val<0:
            showinfo(title='Error!',message='Cannot go below 0!')
            return
        else:
        

            self.tajweed.config(text='{}'.format(val))
            self.tajcount=val
    def remove(self):
        
        if self.variable.get()=='Select a juz to add':
              showinfo(title='Error!',message='You must add a juz first in order for it to be removed!')
              return
        if self.variable.get() in self.show:
            self.show.remove(self.variable.get())
            self.showlabel.config(text='{}'.format(self.show))
            if len(self.show)==0:
                self.showlabel.config(text='No Juz Added')
            for i in self.lst:
                
                if 'Half' in str(self.variable.get()):
                    if str(self.variable.get()) in str(i[0:20]):
                        self.lst.remove(i)
                        self.variable.set(self.mylst[0])
                        
                        break
                elif 'Quarter' in str(self.variable.get()):
                    if str(self.variable.get()) in str(i[0:20]):
                        self.lst.remove(i)
                        self.variable.set(self.mylst[0])
                        
                        break
                elif str(self.variable.get()) in str(i[0:8]):
                    self.lst.remove(i)
                    self.variable.set(self.mylst[0])
                   
                    break
                
        elif self.variable.get()=='Remove all':
            self.show.clear()
            self.lst.clear()
            self.showlabel.config(text='No Juz Added')
            self.variable.set(self.mylst[0])

        else:
            showinfo(title='Juz not in list!',message="You must add the juz first in order for it to be removed!")
            return
                    
                

    def stutterincrease(self):
        
        val=self.stutcount+1
        self.stutter.config(text='{}'.format(val))
        self.stutcount=val
    def stutterdecrease(self):
        val=self.stutcount-1
        if val<0:
            showinfo(title='Error!',message='Cannot go below 0!')
            return
        else:
        

            self.stutter.config(text='{}'.format(val))
            self.stutcount=val
            
                
                
            
                    
                    
                
                
    def make_widgets(self):
           self.mylst=['Select a juz to add','Remove all','1st','1st Juz. 1st Quarter','1st Juz. 2nd Quarter','1st Juz. 3rd Quarter','1st Juz. 4th Quarter','2nd','2nd Juz. 1st Quarter','2nd Juz. 2nd Quarter','2nd Juz. 3rd Quarter','2nd Juz. 4th Quarter','3rd','3rd Juz. 1st Quarter','3rd Juz. 2nd Quarter','3rd Juz. 3rd Quarter','3rd Juz. 4th Quarter','4th','4th Juz. 1st Quarter','4th Juz. 2nd Quarter','4th Juz. 3rd Quarter','4th Juz. 4th Quarter','5th','5th Juz. 1st Quarter','5th Juz. 2nd Quarter','5th Juz. 3rd Quarter','5th Juz. 4th Quarter','6th','6th Juz. 1st Quarter','6th Juz. 2nd Quarter','6th Juz. 3rd Quarter','6th Juz. 4th Quarter','7th Juz. 1st Quarter','7th Juz. 2nd Quarter','7th Juz. 3rd Quarter','7th Juz. 4th Quarter','8th','8th Juz. 1st Quarter','8th Juz. 2nd Quarter','8th Juz. 3rd Quarter','8th Juz. 4th Quarter','9th','9th Juz. 1st Quarter','9th Juz. 2nd Quarter','9th Juz. 3rd Quarter','9th Juz. 4th Quarter','10th','10th Juz. 1st Quarter','10th Juz. 2nd Quarter','10th Juz. 3rd Quarter','10th Juz. 4th Quarter',' 11th','11th Juz. 1st Quarter','11th Juz. 2nd Quarter','11th Juz. 3rd Quarter','11th Juz. 4th Quarter','12th','12th Juz. 1st Quarter','12th Juz. 2nd Quarter','12th Juz. 3rd Quarter','12th Juz. 4th Quarter','13th','13th Juz. 1st Quarter','13th Juz. 2nd Quarter','13th Juz. 3rd Quarter','13th Juz. 4th Quarter','14th','14th Juz. 1st Quarter','14th Juz. 2nd Quarter','14th Juz. 3rd Quarter','14th Juz. 4th Quarter','15th','15th Juz. 1st Quarter','15th Juz. 2nd Quarter','15th Juz. 3rd Quarter','15th Juz. 4th Quarter','16th','16th Juz. 1st Quarter','16th Juz. 2nd Quarter','16th Juz. 3rd Quarter','16th Juz. 4th Quarter','17th','17th Juz. 1st Quarter','17th Juz. 2nd Quarter','17th Juz. 3rd Quarter','17th Juz. 4th Quarter','18th','18th Juz. 1st Quarter','18th Juz. 2nd Quarter','18th Juz. 3rd Quarter','18th Juz. 4th Quarter','19th','19th Juz. 1st Quarter','19th Juz. 2nd Quarter','19th Juz. 3rd Quarter','19th Juz. 4th Quarter','20th','20th Juz. 1st Quarter','20th Juz. 2nd Quarter','20th Juz. 3rd Quarter','20th Juz. 4th Quarter','21st','21st Juz. 1st Quarter','21st Juz. 2nd Quarter','21st Juz. 3rd Quarter','21st Juz. 4th Quarter','22nd','22nd Juz. 1st Quarter','22nd Juz. 2nd Quarter','22nd Juz. 3rd Quarter','22nd Juz. 4th Quarter','23rd','23rd Juz. 1st Quarter','23rd Juz. 2nd Quarter','23rd Juz. 3rd Quarter','23rd Juz. 4th Quarter','24th','24th Juz. 1st Quarter','24th Juz. 2nd Quarter','24th Juz. 3rd Quarter','24th Juz. 4th Quarter','25th','25th Juz. 1st Quarter','25th Juz. 2nd Quarter','25th Juz. 3rd Quarter','25th Juz. 4th Quarter','26th','26th Juz. 1st Quarter','26th Juz. 2nd Quarter','26th Juz. 3rd Quarter','26th Juz. 4th Quarter','27th','27th Juz. 1st Quarter','27th Juz. 2nd Quarter','27th Juz. 3rd Quarter','27th Juz. 4th Quarter','28th','28th Juz. 1st Quarter','28th Juz. 2nd Quarter','28th Juz. 3rd Quarter','28th Juz. 4th Quarter','29th','29th Juz. 1st Quarter','29th Juz. 2nd Quarter','29th Juz. 3rd Quarter','29th Juz. 4th Quarter','30th','30th Juz. 1st Quarter','30th Juz. 2nd Quarter','30th Juz. 3rd Quarter','30th Juz. 4th Quarter']
           self.variable = StringVar(self)
           self.variable.set(self.mylst[0])
           #self.photo= PhotoImage(file='homer.gif')
           #ilabel=Label(self,image=self.photo,height=30)
           #ilabel.image=self.photo
           #ilabel.pack(side=TOP)
           
        
           
        

           self.namr=Label(self,text='Name of Student').pack(side=TOP)
           self.sname=Entry(self)
           self.sname.pack(side=TOP)

           
           
           now=datetime.datetime.now()
           self.now=now.strftime(("Date: %m/%d/%Y"))
           self.date=Label(self,text='{}'.format(self.now))
           self.date.pack(side=TOP)

           

           self.juznum=OptionMenu(self,self.variable,*self.mylst)
           self.juznum.pack(side=TOP)
           Button(self,text='Add Juz',command=lambda:self.QuranTest()).pack(side=TOP)
           self.showlabel=Label(self,text='No Juz Added')
           self.showlabel.pack(side=TOP)
           Button(self,text='Remove Juz',command=lambda:self.remove()).pack(side=TOP)
           Label(self,text='').pack(side=TOP)
           self.lstjuz=Label(self,text='Once all the ajza have been added,\nClick on Question to generate a question')
           self.lstjuz.pack(side=TOP)
           Label(self,text='').pack(side=TOP)
           

           Button(self,text='Question',command=lambda:self.getData()).pack(side=TOP)
           

           Label(self,text='Tested on the following:').pack(side=TOP)
           self.test=Label(self,text='None')
           self.test.pack(side=TOP)


           Label(self,text='Memorization Mistakes:').pack(side=TOP)
           self.memo=Label(self,text=float(0.0))
           self.memo.pack(side=TOP)
           Button(self,text='Add Mistake',command=lambda:self.memoincrease()).pack(side=TOP)
           Button(self,text='Subtract Mistake',command=lambda:self.memodecrease()).pack(side=TOP)

           Label(self,text='Tajweed Mistakes:').pack(side=TOP)
           self.tajweed=Label(self,text=float(0.0))
           self.tajweed.pack(side=TOP)
           Button(self,text='Add Mistake',command=lambda:self.tajincrease()).pack(side=TOP)
           Button(self,text='Subtract Mistake',command=lambda:self.tajdecrease()).pack(side=TOP)

           Label(self,text='Stutter Mistakes:').pack(side=TOP)
           self.stutter=Label(self,text=float(0.0))
           self.stutter.pack(side=TOP)
           Button(self,text='Add Mistake',command=lambda:self.stutterincrease()).pack(side=TOP)
           Button(self,text='Subtract Mistake',command=lambda:self.stutterdecrease()).pack(side=TOP)
           Button(self,text='Calculate Score',command=lambda:self.examMath()).pack(side=LEFT)
           Button(self,text='Finish Exam',command=lambda:self.writeFile()).pack(side=RIGHT)
Exam2().mainloop()
           
    

    
    
        





