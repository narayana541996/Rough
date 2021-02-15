from tkinter import *
import scpp
import threading
from tkinter.ttk import *
from ttkthemes import *
#########Remove the entry to select file name of the new_key to establish trust.
def local_scp(source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, trust, connect_target_key_file_entry, create_key_bits = 1024):
    scpp.scp(source_ssh_file = source_ssh_file_entry.get().strip().replace('\\','/'), source_username = source_username_entry.get().strip().replace('\\','/'), source_host = source_hostname_entry.get().strip().replace('\\','/'), target_ssh_file = target_ssh_file_entry.get().strip().replace('\\','/'), copy_filepath = copy_filepath_entry.get().strip().replace('\\','/'), target_username = target_username_entry.get().strip().replace('\\','/'), target_host = target_hostname_entry.get().strip().replace('\\','/'), target_directory_path = target_folderpath_entry.get().strip().replace('\\','/'), recursive = recursive.get(), establish_trust = trust, create_key_bits = create_key_bits, connect_target_key_file = connect_target_key_file_entry.get().strip().replace('\\', '/'))

def set_mode(disabled, normal, *args, **kwargs):
    for item in disabled:
        item['state'] = 'disabled'
    for item in normal:
        item['state'] = 'normal'

def set_trust_mode(trust, items, *args, **kwargs):
    if trust.get():
        normal = items
        disabled = ()
    else:
        normal = ()
        disabled = items
    set_mode(disabled = disabled, normal = normal)

root = Tk()
main = Frame(root)
main.pack()
style = ThemedStyle(main)
style.set_theme('vista')
#style.configure('TButton', justify = 'center')
recursive = BooleanVar(main)
authentication = StringVar(main)
trust = BooleanVar(main)
trust_key = StringVar(main)
recursive.set(True)
authentication.set('ssh')
trust.set(False)
trust_key.set('new')
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

trust_button = Checkbutton(main, text = 'Establish trust between the servers.', variable = trust, onvalue = True, offvalue = False)

password_radiobutton = Radiobutton(main, text = 'Access with Password ', variable = authentication, value = 'password', command = lambda: set_mode(disabled = (source_ssh_file_label, source_ssh_file_entry, source_ssh_password_label, source_ssh_password_entry, target_ssh_file_label, target_ssh_file_entry, target_ssh_password_label, target_ssh_password_entry, trust_button), normal = (source_password_label, source_password_entry, target_password_label, target_password_entry)))
password_radiobutton.grid(row = 9, column = 0, padx = 4, pady = 4, sticky = 'w')
source_password_label = Label(main, text = 'Source Password: ')
source_password_label.grid(row = 10, column = 0, padx = 4, pady = 4, sticky = 'w')
source_password_entry = Entry(main, width = 50)
source_password_entry.grid(row = 11, column = 0, padx = 4, pady = 4, sticky = 'w')

target_password_label = Label(main, text = 'Target Password: ')
target_password_label.grid(row = 10, column = 1, padx = 4, pady = 4, sticky = 'w')
target_password_entry = Entry(main, width = 50)
target_password_entry.grid(row = 11, column = 1, padx = 4, pady = 4, sticky = 'w')

ssh_radiobutton = Radiobutton(main, text = 'Access with SSH', variable = authentication, value = 'ssh', command = lambda: set_mode(normal = (source_ssh_file_label, source_ssh_file_entry, source_ssh_password_label, source_ssh_password_entry, target_ssh_file_label, target_ssh_file_entry, target_ssh_password_label, target_ssh_password_entry, trust_button), disabled = (source_password_label, source_password_entry, target_password_label, target_password_entry)))
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

trust_button.grid(row = 17, column = 0, padx = 4, pady = 4, sticky = 'w')
trust_old_button = Radiobutton(main, text = 'Use existing key-pair to establish trust\nbetween the source and the target.', variable = trust_key, value = 'old')
trust_old_button.grid(row = 18, column = 0, padx = 4, pady = 4, sticky = 'w')
connect_target_key_file_label = Label(main, text = 'Enter the path of the key-pair on the source to establish trust: ', state = 'disabled')
connect_target_key_file_label.grid(row = 19, column = 0, padx = 4, pady = 4, sticky = 'w')
connect_target_key_file_entry = Entry(main, width = 50, state = 'disabled')
connect_target_key_file_entry.grid(row = 20, column = 0, padx = 4, pady = 4, sticky = 'w')
trust_new_button = Radiobutton(main, text = 'Create new key-pair to establish trust\nbetween the source and the target.', variable = trust_key, value = 'new')
trust_new_button.grid(row = 18, column = 1, padx = 4, pady = 4, sticky = 'w')
trust_button.configure(command = lambda: set_trust_mode(checkbutton = trust_button, trust = trust, items = (trust_old_button, trust_new_button)))
trust_old_button.configure(command = lambda: set_mode(normal = (connect_target_key_file_label, connect_target_key_file_entry), disabled = ()), state = 'disabled')
trust_new_button.configure(command = lambda: set_mode(disabled = (connect_target_key_file_label, connect_target_key_file_entry), normal = ()), state = 'disabled')

copy_button = Button(main, text = 'Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive, source_password = source_ssh_password_entry, target_password = target_ssh_password_entry: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, source_password, target_password)).start())
copy_button.grid(row = 21, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')

recursive_checkbutton = Checkbutton(main, text = 'Recursive', variable = recursive, onvalue = True, offvalue = False)
recursive_checkbutton.grid(row = 22, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'w')
main.mainloop()
