from tkinter import *

window=Tk()

var=IntVar()

class GUI:
    '''
    Class for setting the information of the GUI window
    '''

    def __init__(self, window):
        """
        - This function is for creating the frames of the window, entries, buttons and setting their dimensions.
        """

        self.window = window

        self.price_frame = Frame(self.window)
        self.entry_price = Entry(self.price_frame, width=16, font=10)
        self.label_price = Label(self.price_frame, text='Car price:', font=10)
        self.price_frame.pack(anchor='w', pady=6)
        self.entry_price.pack(padx=14, side='right')
        self.label_price.pack(padx=14, side='right')

        self.tax_frame = Frame(self.window)
        self.entry_tax = Entry(self.tax_frame, width=16, font=10)
        self.label_tax = Label(self.tax_frame, text='State Tax:', font=10)
        self.tax_frame.pack(anchor='w', pady=6)
        self.entry_tax.pack(padx=15, side='right')
        self.label_tax.pack(padx=12, side='right')

        self.insurance_frame=Frame(self.window)
        self.label_insurance=Label(self.insurance_frame, text='Add expected insurance value?', font=10)
        self.insurance_frame.pack(anchor='w', pady=6)
        self.label_insurance.pack(padx=12, side='right')

        self.out_frame = Frame(self.window)
        self.out_frame.pack(side="bottom")
        self.label1 = Label(self.out_frame, text='', font=10)
        self.label1.pack(padx=12, side='right')

        self.out2_frame = Frame(self.window)
        self.out2_frame.pack(side="top")
        self.label2 = Label(self.out2_frame, text='', font=10)
        self.label2.pack(padx=12, side='right')

        Radiobutton1 = Radiobutton(window, text="Yes", variable=var, value=1)

        Radiobutton2 = Radiobutton(window, text="No", variable=var, value=0)

        Radiobutton1.pack()
        Radiobutton2.pack()
        var.set(1)

        self.buttonFrame = Frame(self.window)

        self.buttonQuote = Button(self.window, text='Tax amount!', font=16, width=12, command=self.clicked)
        self.buttonReset = Button(self.window, text='Reset', font=16, width=12, command=self.reset)

        self.buttonFrame.pack(anchor='w', pady=6)
        self.buttonQuote.pack(padx=0, pady=6)
        self.buttonReset.pack(padx=0, pady=6)


    def clicked(self):

        #Getting the user inputs

        price=int(self.entry_price.get())
        tax_rate=int(self.entry_tax.get())
        print(price)
        print(tax_rate)

        total = price + (price * (tax_rate/100))
        print(total)

        insurance = 0
        print(var.get())
        if var.get()==1:

            if price > 5000:
                insurance = 100
            if price > 10000:
                insurance = 140
            if price > 15000:
                insurance = 180
            if price > 20000:
                insurance = 230
            if price > 30000:
                insurance = 300

        print(insurance)



        self.label1.config(text=f'the total amount is {total}' , font=("Arial", 12, "bold"))
        self.label2.config(text=f"insurance expected is: {insurance} ")

        try:
            #Meant to invoke the exception handler to catch data types error.
            price=(int(self.entry_price.get()))
            tax=(int(self.entry_tax.get()))+0

            # Default insurance price
            price=0.00


        except(ValueError, TypeError):
            print('Oops there is something wrong!')
            errorMsg=f"Something went wrong!\nAge: 18-100\nCar year:1995-2022\nDo not leave any entries empty!\nCar makes eligible:Kia, Toyota, Chevrolet, Nissan, Ford, Honda, Hyundai\nCar models eligible: Carnival, Rio, Soul, Camry, Corolla, Avalon, Malibu,Corvette, Sillverado, Altima, Maxima, Sentra, Focus, Edge, Mustang, Accord, odyssey, Civic Sonata, Accent, Elantra"

            messagebox.showerror('Error', errorMsg)


    def reset(self):
        '''
       This function is called when the user presses the 'Reset' button and it is meant to reset the entries.
        '''
        self.entry_price.delete(0, END)
        self.entry_tax.delete(0, END)
        self.label1.config(text="")
        self.label2.config(text="")

