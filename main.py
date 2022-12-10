from gui import *


def main():
    '''
    This function is for calling GUI class created and setting the title and deminisions of the window.
    '''

    widgets = GUI(window)
    window.title('Car Tax')
    window.geometry('400x400')

    window.resizable(False,False)
    window.mainloop()

if __name__ == '__main__':
    main()