from tkinter import *
import scpp2

main = Tk()
#copy_type_radiobuttons = Radiobutton(main, )
hostname_label = Label(main, text = 'IP/Hostname: ')
hostname_label.grid(sticky = 'w')
hostname_entry = Entry(main)
hostname_entry.grid(sticky = 'w')
keyfile_label = Label(main, text = 'Key file')
keyfile_label.grid(sticky = 'w')
keyfile_entry = Entry(main)
keyfile_entry.grid(sticky = 'w')
file_entry = Label(main, text = 'File/Directory')
file_entry.grid(sticky = 'w')
main.mainloop()