from gui import *
'''This program reads data from a text file and encrypts(readable -> unreadable) or 
decrypts(unreadable -> readable) it depending on the users need.'''
def main():
    #Creates the window
    window = Tk()
    window.title('Caesar Cipher')
    window.geometry('400x200')
    window.resizable(False,False)

    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()