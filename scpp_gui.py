from tkinter import *
import scpp
import threading

def local_scp(source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive):
    scpp.scp(source_ssh_file = source_ssh_file_entry.get().strip().replace('\\','/'), source_username = source_username_entry.get().strip().replace('\\','/'), source_host = source_hostname_entry.get().strip().replace('\\','/'), target_ssh_file = target_ssh_file_entry.get().strip().replace('\\','/'), copy_filepath = copy_filepath_entry.get().strip().replace('\\','/'), target_username = target_username_entry.get().strip().replace('\\','/'), target_host = target_hostname_entry.get().strip().replace('\\','/'), target_directory_path = target_folderpath_entry.get().strip().replace('\\','/'), recursive = recursive.get())


main = Tk()
recursive = BooleanVar(main)
#copy_type_radiobuttons = Radiobutton(main, )
source_hostname_label = Label(main, text = 'Source IP/Hostname: ')
source_hostname_label.grid(row = 1, column = 0, padx = 4, pady = 4, sticky = 'w')
source_hostname_entry = Entry(main, width = 50)
source_hostname_entry.grid(row = 2, column = 0, padx = 4, pady = 4, sticky = 'w')

target_hostname_label = Label(main, text = 'Target IP/Hostname: ')
target_hostname_label.grid(row = 1, column = 1, padx = 4, pady = 4, sticky = 'w')
target_hostname_entry = Entry(main, width = 50)
target_hostname_entry.grid(row = 2, column = 1, padx = 4, pady = 4, sticky = 'w')

source_username_label = Label(main, text = 'Source Username: ')
source_username_label.grid(row = 3, column = 0, padx = 4, pady = 4, sticky = 'w')
source_username_entry = Entry(main, width = 50)
source_username_entry.grid(row = 4, column = 0, padx = 4, pady = 4, sticky = 'w')

target_username_label = Label(main, text = 'Target Username: ')
target_username_label.grid(row = 3, column = 1, padx = 4, pady = 4, sticky = 'w')
target_username_entry = Entry(main, width = 50)
target_username_entry.grid(row = 4, column = 1, padx = 4, pady = 4, sticky = 'w')

source_ssh_file_label = Label(main, text = 'Source SSH Key-File Path: ')
source_ssh_file_label.grid(row = 5, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_file_entry = Entry(main, width = 50)
source_ssh_file_entry.grid(row = 6, column =0, padx = 4, pady = 4, sticky = 'w')

target_ssh_file_label = Label(main, text = 'Target SSH Key-File Path: ')
target_ssh_file_label.grid(row = 5, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_file_entry = Entry(main, width = 50)
target_ssh_file_entry.grid(row = 6, column = 1, padx = 4, pady = 4, sticky = 'w')

copy_filepath_label = Label(main, text = 'Absolute Path of File to be Copied: ')
copy_filepath_label.grid(row = 7, column =0, padx = 4, pady = 4, sticky = 'w')
copy_filepath_entry = Entry(main, width = 50)
copy_filepath_entry.grid(row = 8, column = 0 , padx = 4, pady = 4, sticky = 'w')

target_folderpath_label = Label(main, text = 'Absolute Path of the Destination Folder:')
target_folderpath_label.grid(row = 7, column = 1, padx = 4, pady = 4, sticky = 'w')
target_folderpath_entry = Entry(main, width = 50)
target_folderpath_entry.grid(row = 8, column = 1, padx = 4, pady = 4, sticky = 'w')
###add print statements to check the cause of the empty string
copy_button = Button(main, text = 'Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive)).start())
copy_button.grid(row = 9, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')
copy_button = Button(main, text = 'Trust and Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive, establish_trust = True: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, establish_trust)).start())
copy_button.grid(row = 10, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')
recursive_checkbutton = Checkbutton(main, text = 'Recursive', variable = recursive, onvalue = True, offvalue = False)
recursive_checkbutton.grid(row = 11, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'w')
main.mainloop()
