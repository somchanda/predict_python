from tkinter import Tk, Label, Entry, StringVar, ttk, Scrollbar
from db import Predict


def center_window(w=300, h=200):
    # get screen width and height
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))


def sum_string(value, result=0):
    if len(value) < 1:
        temp = str(result)
        if len(temp) == 1:
            return result
        else:
            return sum_string(str(result))
    else:
        result += int(value[0])
        return sum_string(value[1:], result)


def cal(e):
    name = name_text.get()
    name = str(name).lower().replace('a', '1').replace('j', '1').replace(
        's', '1').replace('b', '2').replace('k', '2').replace(
            't', '2').replace('c', '3').replace('l', '3').replace(
                'u', '3').replace('d', '4').replace('m', '4').replace(
                    'v', '4').replace('e', '5').replace('n', '5').replace(
                        'w', '5').replace('f', '6').replace('o', '6').replace(
                            'x', '6').replace('g', '7').replace('p', '7').replace('y', '7').replace('h', '8').replace('q', '8').replace('z', '8').replace('i', '9').replace('r', '9').replace(' ', '')
    code = sum_string(name)
    print(code)
    pd = Predict()
    rows = pd.getPredictByCode(code)
    for row in rows:
        if row[2] == 1:
            attitude.config(text=row[3])
        elif row[2] == 2:
            personality.config(text=row[3])
        elif row[2] == 3:
            love.config(text=row[3])
        elif row[2] == 4:
            work.config(text=row[3])
        elif row[2] == 5:
            money.config(text=row[3])


app = Tk()
app.configure(background='#000d1a')
app.title("Predict application")
center_window(1080, 920)
# ការទស្សន៍ទាយតាមឈ្មោះជាអក្សឡាតាំង
# ឈ្មោះជាអក្សឡាតាំង

head = Label(app, text="ការទស្សន៍ទាយតាមឈ្មោះជាអក្សឡាតាំង", foreground="white",
             background="#003367", font=("Khmer OS Bokor", 30))
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=2)
app.rowconfigure(2, weight=1)
head.grid(column=0, row=0, columnspan=2, ipadx=20, ipady=20, sticky="NSEW")

name_label = Label(app, text="ឈ្មោះជាអក្សឡាតាំង", foreground="white",
                   background="#000d1a", font=("Khmer OS Bokor", 20))
name_label.grid(column=0, row=1, ipadx=40, ipady=20, sticky="E")

name_text = StringVar()
name_entry = Entry(app, textvariable=name_text, font=(
    "Times New Roman", 20), bg="#00274d", fg="white", bd=4)
name_entry.grid(column=1, row=1, sticky="W")
name_entry.bind("<FocusOut>", cal)
name_entry.bind("<Return>", cal)

# Create tab control
tab_control = ttk.Notebook(app)
s = ttk.Style()
s.configure('TNotebook.Tab', font=('Khmer OS Bokor', '12'))

# Create tab conten frame
tab_attitude = ttk.Frame(tab_control)
tab_personality = ttk.Frame(tab_control)
tab_love = ttk.Frame(tab_control)
tab_work = ttk.Frame(tab_control)
tab_money = ttk.Frame(tab_control)

tab_attitude.columnconfigure(0, weight=1)
tab_attitude.rowconfigure(0, weight=1)
SVBar = Scrollbar(tab_attitude, orient='vertical') 
SVBar.grid(column=1, row=0, sticky='NS')

# Display tab item
tab_control.add(tab_attitude, text='បុគ្គលិកលក្ខណៈ')
tab_control.add(tab_personality, text='បុគ្គលភាព')
tab_control.add(tab_love, text='ស្នេហា')
tab_control.add(tab_work, text='ការងារ')
tab_control.add(tab_money, text='ប្រាក់កាស')
tab_control.grid(column=0, row=2, columnspan=2, sticky="NSEW")


attitude = ttk.Label(tab_attitude, text="", font=(
    "Khmer OS Bokor", 12), wraplength=800)
attitude.grid(column=0, row=0, sticky='NW')


personality = ttk.Label(tab_personality, text="", font=(
    "Khmer OS Bokor", 12), wraplength=800)
personality.grid(column=3, row=3)

love = ttk.Label(tab_love, text="", font=(
    "Khmer OS Bokor", 12), wraplength=800)
love.grid(column=3, row=3)

work = ttk.Label(tab_work, text="", font=(
    "Khmer OS Bokor", 12), wraplength=800)
work.grid(column=3, row=3)

money = ttk.Label(tab_money, text="", font=(
    "Khmer OS Bokor", 12), wraplength=800)
money.grid(column=3, row=3)

app.mainloop()
