# import tkinter as tk

# root = tk.Tk()
# root.geometry("600x400")

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=2)

# rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
# rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="EW")

# rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
# rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10, sticky="EW")

# root.mainloop()



# from tkinter import Tk, Label, Button, ttk, messagebox
# master = Tk()
# master.geometry('500x200')
# def func():
#     messagebox.showinfo( "Hello Educba", "Click on the tabs to view the content")
# b1 = Button( master, text='Click me for next step', background = 'Red', fg = '#000000', command = func)
# b1.pack()
# tc = ttk.Notebook(master)
# t1 = ttk.Frame(tc)
# t2 = ttk.Frame(tc)
# tc.add(t1, text ='Notebook tab1')
# tc.add(t2, text ='Notebook tab2')
# tc.pack(expand = 1, fill ="both")
# ttk.Label(t1,
# text ="Hello Educba Technology Institute").grid(column = 3,
# row = 3)
# ttk.Label(t2,
# text ="Notebook widget demonstration").grid(column = 3,
# row = 3)
# master.mainloop()

# def sub(value, result=0):
#     if len(value) < 1:
#         temp = str(result)
#         if len(temp) == 1:
#             return result
#         else:
#             return sub(str(result))
#     else:
#         result += int(value[0])
#         return sub(value[1:] , result)

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# container = ttk.Frame(root)
# canvas = tk.Canvas(container)
# scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# canvas.configure(yscrollcommand=scrollbar.set)

# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()

# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk


# class VertNotebook(ttk.Frame):
#     def __init__(self, *args, **kw):
#         ttk.Frame.__init__(self, *args, **kw)
#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(2, weight=1)
#         # scrollable tabs
#         self._listbox = tk.Listbox(self, width=1, background='lightgrey', 
#                                    highlightthickness=0, relief='raised')
#         scroll = ttk.Scrollbar(self, orient='vertical', command=self._listbox.yview)
#         self._listbox.configure(yscrollcommand=scroll.set)

#         # list of widgets associated with the tabs
#         self._tabs = []
#         self._current_tab = None  # currently displayed tab

#         scroll.grid(row=0, column=0, sticky='ns')
#         self._listbox.grid(row=0, column=1, sticky='ns')
#         # binding to display the selected tab
#         self._listbox.bind('<<ListboxSelect>>', self.show_tab)

#     def add(self, widget, label): # add tab
#         self._listbox.insert('end', label)  # add label listbox
#         # resize listbox to be large enough to show all tab labels
#         self._listbox.configure(width=max(self._listbox.cget('width'), len(label)))
#         if self._current_tab is not None:
#             self._current_tab.grid_remove()
#         self._tabs.append(widget)
#         widget.grid(in_=self, column=2, row=0, sticky='ewns')
#         self._current_tab = widget
#         self._listbox.selection_clear(0, 'end')
#         self._listbox.selection_set('end')
#         self._listbox.see('end')

#     def show_tab(self, event):
#         print(event, self._listbox.curselection(), )
#         try:
#             widget = self._tabs[self._listbox.curselection()[0]]
#             print(widget)
#         except IndexError:
#             return
#         if self._current_tab is not None:
#             self._current_tab.grid_remove()
#         self._current_tab = widget
#         widget.grid(in_=self, column=2, row=0, sticky='ewns')


# root = tk.Tk()
# nb = VertNotebook(root)
# for i in range(50):
#     nb.add(ttk.Label(nb, text='Label %i' % i), 'Tab %i' % i)
# nb.pack(expand=True, fill='both')
# root.mainloop()


import tkinter as tk 


Num_Vertical = ('ehllfslf\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn\nn') 
Num_Horizontal = ("A B C D E F G H I J K L M N O P Q R S T U V \  W X Y Z") 

window = tk.Tk() 
window.geometry("250x200") 

SVBar = tk.Scrollbar(window) 
SVBar.pack (side = tk.RIGHT, 
			fill = "y") 

SHBar = tk.Scrollbar(window, 
					orient = tk.HORIZONTAL) 
SHBar.pack (side = tk.BOTTOM, 
			fill = "x") 

TBox = tk.Text(window, 
			height = 500, 
			width = 500, 
			yscrollcommand = SVBar.set, 
			xscrollcommand = SHBar.set, 
			wrap = "none") 

TBox = tk.Text(window, 
			height = 500, 
			width = 500, 
			yscrollcommand = SVBar.set, 
			xscrollcommand = SHBar.set, 
			wrap = "none") 

TBox.pack(expand = 0, fill = tk.BOTH) 

TBox.insert(tk.END, Num_Horizontal) 
TBox.insert(tk.END, Num_Vertical) 

SHBar.config(command = TBox.xview) 
SVBar.config(command = TBox.yview) 

window.mainloop() 
