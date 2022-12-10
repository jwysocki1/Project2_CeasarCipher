from tkinter import *           #Used to create GUI
from tkinter import filedialog  #Supports the file explorer
import os.path                  #Ensures file will work
from tool import *              #The actual cipher

class GUI:
    file = ''      #Variable for the soon to be opened file
    content = ''   #Variable used to hold the data before and after it's modified

    def __init__(self, window):
        self.window = window

        self.fileframe = Frame(self.window)
        self.filelabel = Label(self.fileframe, text='Choose file:', width=20)
        self.enterbutton = Button(self.fileframe, text='Choose File', command=self.findfile)
        self.filelabel.pack(side='left')
        self.enterbutton.pack(padx=30)               #Creates the file explorer button
        self.fileframe.pack(anchor='w', pady=10)

        self.enterframe = Frame(self.window)
        self.openlabel = Label(self.enterframe, text='')   #Label that displays the path for the opened file
        self.openlabel.pack()
        self.enterframe.pack(anchor='center', pady=5)

        self.modeframe = Frame(self.window)
        self.modelabel = Label(self.modeframe,text='Mode:', width=20)   #Creates the two radio buttons to figure
        self.selection = IntVar()                                       #whether to decrypt or encrypt the data
        self.selection.set(0)
        self.encryptradio = Radiobutton(self.modeframe, text='Encrypt',variable=self.selection, value=1)
        self.decryptradio = Radiobutton(self.modeframe,text='Decrypt',variable=self.selection,value=2)
        self.modelabel.pack(side='left')
        self.encryptradio.pack(side='left')
        self.decryptradio.pack(side='left')
        self.modeframe.pack(anchor='w', pady=10)

        self.shiftframe = Frame(self.window)
        self.shiftlabel = Label(self.shiftframe,text='Key:', width=20)
        self.shiftspinbox = Spinbox(self.shiftframe, from_=0.0,to=100.0)
        self.otherlabel = Label(self.shiftframe, text='Remember the key.',width=15)
        self.shiftlabel.pack(side='left')
        self.shiftspinbox.pack(side='left')        #Takes user input to figure how to modify the data
        self.otherlabel.pack(side='left')          #input must be the same twice in a row for the text to be readable
        self.shiftframe.pack(anchor='w', pady=10)  #spinbox can take any integer value, even outside the specified range

        self.runframe = Frame(self.window)
        self.runbutton = Button(self.runframe,text='Run',command=self.run)   #Button that calls the functions to
        self.runbutton.pack()                                                 #manipulate the data
        self.runframe.pack(anchor='center',pady=5)


    def findfile(self):
        '''
        This function opens the file explorer and saves the path in a class variable (file)
        then reads the data from the file and stores it in the other class variable (content)
        :return: assigns two variables
        '''
        GUI.file = filedialog.askopenfilename(initialdir="documents",title="Select a File",
                                          filetypes=(("Text files","*.txt*"),("all files","*.*")))
        self.openlabel.config(text=f'File opened: {GUI.file}')
        if os.path.isfile(GUI.file):
            with open(GUI.file, 'r') as readfile:
                GUI.content = readfile.readlines()
                GUI.content = [x.strip() for x in GUI.content]
        else:
            self.openlabel.config(text='File does not exist.')

    def run(self):
        '''
        This function validates the input of the spinbox and calls the functions which encrypt or decrypt the text
        found in "content." It then writes the modified text back into the same file it was pulled from.
        :return: writes data back into file
        '''
        try:
            choice = self.selection.get()
            shift = int(self.shiftspinbox.get())
            if choice == 0 or choice == 1:
                product = encrypt(GUI.content, shift)
                self.otherlabel.config(text='File encrypted!')
            elif choice == 2:
                product = decrypt(GUI.content, shift)
                self.otherlabel.config(text='File decrypted!')

            with open(GUI.file, 'w') as writefile:
                for x in product:
                    writefile.write(x)
                    writefile.write('\n')
        except:
            self.otherlabel.config(text='Enter integer value')