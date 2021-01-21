from tkinter import *
import scpp
import threading

def local_scp(source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive):
    scpp.scp(source_ssh_file = source_ssh_file_entry.get().strip().replace('\\','/'), source_username = source_username_entry.get().strip().replace('\\','/'), source_host = source_hostname_entry.get().strip().replace('\\','/'), target_ssh_file = target_ssh_file_entry.get().strip().replace('\\','/'), copy_filepath = copy_filepath_entry.get().strip().replace('\\','/'), target_username = target_username_entry.get().strip().replace('\\','/'), target_host = target_hostname_entry.get().strip().replace('\\','/'), target_directory_path = target_folderpath_entry.get().strip().replace('\\','/'), recursive = recursive.get())

def set_auth_mode(disabled, normal):
    for item in disabled:
        item['state'] = 'disabled'
    for item in normal:
        item['state'] = 'normal'

main = Tk()
recursive = BooleanVar(main)
authentication = StringVar(main)
recursive.set(True)
authentication.set('ssh')
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

copy_filepath_label = Label(main, text = 'Absolute Path of File to be Copied: ')
copy_filepath_label.grid(row = 7, column =0, padx = 4, pady = 4, sticky = 'w')
copy_filepath_entry = Entry(main, width = 50)
copy_filepath_entry.grid(row = 8, column = 0 , padx = 4, pady = 4, sticky = 'w')

target_folderpath_label = Label(main, text = 'Absolute Path of the Destination Folder:')
target_folderpath_label.grid(row = 7, column = 1, padx = 4, pady = 4, sticky = 'w')
target_folderpath_entry = Entry(main, width = 50)
target_folderpath_entry.grid(row = 8, column = 1, padx = 4, pady = 4, sticky = 'w')
###add print statements to check the cause of the empty string
#####Include entry for target_ssh_password and source_ssh_password.

password_radiobutton = Radiobutton(main, text = 'Access with Password ', variable = authentication, value = 'password', command = lambda: set_auth_mode(disabled = (source_ssh_file_label, source_ssh_file_entry, source_ssh_password_label, source_ssh_password_entry, target_ssh_file_label, target_ssh_file_entry, target_ssh_password_label, target_ssh_password_entry), normal = (source_password_label, source_password_entry, target_password_label, target_password_entry)))
password_radiobutton.grid(row = 9, column = 0, padx = 4, pady = 4, sticky = 'w')
source_password_label = Label(main, text = 'Source Password: ')
source_password_label.grid(row = 10, column = 0, padx = 4, pady = 4, sticky = 'w')
source_password_entry = Entry(main, width = 50)
source_password_entry.grid(row = 11, column = 0, padx = 4, pady = 4, sticky = 'w')

target_password_label = Label(main, text = 'Target Password: ')
target_password_label.grid(row = 10, column = 1, padx = 4, pady = 4, sticky = 'w')
target_password_entry = Entry(main, width = 50)
target_password_entry.grid(row = 11, column = 1, padx = 4, pady = 4, sticky = 'w')

ssh_radiobutton = Radiobutton(main, text = 'Access with SSH', variable = authentication, value = 'ssh', command = lambda: set_auth_mode(normal = (source_ssh_file_label, source_ssh_file_entry, source_ssh_password_label, source_ssh_password_entry, target_ssh_file_label, target_ssh_file_entry, target_ssh_password_label, target_ssh_password_entry), disabled = (source_password_label, source_password_entry, target_password_label, target_password_entry)))
ssh_radiobutton.grid(row = 12, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_file_label = Label(main, text = 'Source SSH Key-File Path: ')
source_ssh_file_label.grid(row = 13, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_file_entry = Entry(main, width = 50)
source_ssh_file_entry.grid(row = 14, column =0, padx = 4, pady = 4, sticky = 'w')
source_ssh_password_label = Label(main, text = 'Source SSH Key-File Password(if required): ')
source_ssh_password_label.grid(row = 15, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_password_entry = Entry(main, show = '*', width = 50)
source_ssh_password_entry.grid(row = 16, column = 0, padx = 4, pady = 4, sticky = 'w')

target_ssh_file_label = Label(main, text = 'Target SSH Key-File Path: ')
target_ssh_file_label.grid(row = 13, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_file_entry = Entry(main, width = 50)
target_ssh_file_entry.grid(row = 14, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_password_label = Label(main, text = 'Target SSH Key-File Password(if required): ')
target_ssh_password_label.grid(row = 15, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_password_entry = Entry(main, show = '*', width = 50)
target_ssh_password_entry.grid(row = 16, column = 1, padx = 4, pady = 4, sticky = 'w')

password_radiobutton.invoke()
ssh_radiobutton.invoke()

copy_button = Button(main, text = 'Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive)).start())
copy_button.grid(row = 17, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')
copy_button = Button(main, text = 'Trust and Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive, establish_trust = True: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, establish_trust)).start())
copy_button.grid(row = 18, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')
recursive_checkbutton = Checkbutton(main, text = 'Recursive', variable = recursive, onvalue = True, offvalue = False)
recursive_checkbutton.grid(row = 19, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'w')
main.mainloop()
