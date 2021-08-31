from tkinter import*
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Currency Conversion')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

#create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

#Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)
 
#Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="convert")

#Disable 2nd tab
my_notebook.tab(1, state='disabled')

####################
# CURRENCY STUFF
####################
def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WWARNING!, You didn't fill out all the Fields")
    else:
        #Disable entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        #Enable tab
    my_notebook.tab(1, state='normal')
    #Change tab field 
    amount_label.config(text=f'Amount of {home_entry.get()} To convert to{conversion_entry.get()}')
    converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
    convert_button.config(text=f'Convert From {home_entry.get()}')
 
def Unlock():
    #Enable entry boxes
        home_entry.config(state="normal")
        conversion_entry.config(state="normal")
        rate_entry.config(state="normal")
        #Disable tab
        my_notebook.tab(1, state='disabled')
home = LabelFrame(currency_frame, text="Your Name")
home.pack(pady=20)

home = LabelFrame(currency_frame, text="Your Home Currency")  
home.pack(pady=20)

#Home currency entry box
home_entry = Entry(home, font="Helvetica, 24")
home_entry.pack(pady=10, padx=10)

#Conversion Currency Frame
conversion = LabelFrame(currency_frame,text="Conversion Currency")
conversion.pack(pady=20)

#convert to lable
conversion_label = Label(conversion, text="Currency Convert To...")
conversion_label.pack(pady=10)

#Convert to Entry 
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

#rate lable
rate_label = Label(conversion, text="Current Conversion Rate...")
rate_label.pack(pady=10)

#rate Entry 
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10) 

#Button Frame
Button_frame = Frame(currency_frame)
Button_frame.pack(pady=20)

#create buttons
lock_button = Button(Button_frame, text="lock", command="lock")
lock_button .grid(row=0, column=0, padx=10)

Unlock_button = Button(Button_frame, text="Unlock", command="Unlock")
Unlock_button .grid(row=0, column=1, padx=10)

####################
# CONVERSION STUFF
####################
def convert():
     #Clear converted Entry Box 
     converted_entry.delete(0, END)

     #Convert
     conversion = float(rate_entry.get()) * float(amount_entry.get())

    #Convert to decimals
     conversion = round(conversion,2)

    #Add commas
     conversion = '{:,}'.format(conversion) 
    #Update entry box
     converted_entry.insert(0, conversion)
    
def clear():
    amount_entry.delete(0,END)
    converted_entry.delete(0,END)

amount_label = LabelFrame(conversion_frame, text="Amount To Convert")
amount_label.pack(pady=20)

#Entry Box For Amount
amount_entry = Entry(amount_label, font=("Helvetica"))
amount_entry.pack(pady=10,padx=10)

#Convert Button
convert_button = Button(amount_label, text="Convert")
convert_button.pack(pady=20)

#Equals Framne 
converted_label = LabelFrame(currency_frame, text="Converted Currency")
converted_label.pack(pady=20)

#Converted Entry 
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

#Clear Button
clear_button = Button(conversion_frame, text="clear", command="clear")
clear_button.pack(pady=20)

#Fake Label for Spacing
spacer = Label(conversion_frame, text="", width=68) 
spacer.pack() 

