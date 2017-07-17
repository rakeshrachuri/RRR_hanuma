import matplotlib
import tkinter as tk
import pandas
from pandas import DataFrame
#go.Candlestick


LARGE_FONT= ("Verdana", 12)

class ScreenManager(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        container = tk.Frame(self)
        container.grid(row=0,column=0,sticky='nsew')
        container.config(bg='blue')
        #container.pack();
        #container.pack(side='top', fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        #Initialize panels around main container
        #topFrame=Top(container,self)
        bottomFrame = Bottom(container, self)
        leftFrame = Left(container, self)
        # rightFrame = Right(container, self)
        # centerFrame = Center(container, self)
        #self.frames[Top]=topFrame
        self.frames[Bottom]=bottomFrame
        self.frames[Left] = leftFrame
        # self.frames[Right] = rightFrame
        # self.frames[Center] = centerFrame
        self.show_frames()
        print(container.grid_size())
        #bottomFrame=Bottom(container,self)
        #leftFrame=Left(container,self)
        #rightFrame=Right(container,self)
        #centerFrame=Center(container,self)
    def show_frames(self):
        for frameName in self.frames:
            print(frameName)
            self.frames[frameName].tkraise()

class Top(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.config(bg='red')
        self.grid(row=0,columnspan=10,sticky='we')
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        topLabel=tk.Label(self,text='Top Label',font=LARGE_FONT)
        topLabel.pack(padx=10,pady=10)

class Bottom(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=9,columnspan=10,sticky='we')
        self.config(bg='yellow')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        bottomLabel=tk.Label(self,text='Bottom Label',font=LARGE_FONT)
        bottomLabel.pack(pady=10,padx=10)

class Left(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=1,rowspan=8,column=0,columnspan=2,sticky='ns')
        self.config(bg='white')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        leftLabel=tk.Label(self,text='Left Label',font=LARGE_FONT)
        leftLabel.pack(pady=10,padx=10)

class Right(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=1,rowspan=8,column=0,columnspan=2)
        self.config(bg='black')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        rightLabel=tk.Label(self,text='Right Label',font=LARGE_FONT)
        rightLabel.pack (pady=10,padx=10)

class Center(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=1,column=2,rowspan=8,columnspan=6)
        self.config(bg='purple')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        centerLabel=tk.Label(self,text='Center Label',font=LARGE_FONT)
        centerLabel.pack(pady=10,padx=10)

sm=ScreenManager()
sm.mainloop()