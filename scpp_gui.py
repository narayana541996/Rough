from tkinter import *
from tkinter.messagebox import *
import scpp
import threading
from tkinter.ttk import *
from ttkthemes import *
#########Remove the entry to select file name of the new_key to establish trust.
def local_scp(source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, trust, target_key_file_on_source_entry, create_key_bits = 1024):
    response = scpp.scp_(source_ssh_file = source_ssh_file_entry.get().strip().replace('\\','/'), source_username = source_username_entry.get().strip().replace('\\','/'), source_host = source_hostname_entry.get().strip().replace('\\','/'), target_ssh_file = target_ssh_file_entry.get().strip().replace('\\','/'), copy_filepath = copy_filepath_entry.get().strip().replace('\\','/'), target_username = target_username_entry.get().strip().replace('\\','/'), target_host = target_hostname_entry.get().strip().replace('\\','/'), target_directory_path = target_folderpath_entry.get().strip().replace('\\','/'), recursive = recursive.get(), establish_trust = trust, create_key_bits = create_key_bits, target_key_file_on_source = target_key_file_on_source_entry.get().strip().replace('\\', '/'))
    #if f'Established Trust between {source_username_entry.get().strip().replace("\\","/")}@{source_hostname_entry.get().strip().replace("\\","/")} and {target_username.get().strip().replace("\\","/")}@{target_host.get().strip().replace("\\","/")}' in response and f'Copied {copy_filepath_entry.get().split().replace("\\","/")} from {source_username_entry.get().strip().replace("\\","/")}@{source_hostname_entry.get().strip().replace("\\","/")} to {target_username_entry.get().strip().replace("\\","/")}@{target_hostname_entry.get().strip().replace("\\","/")}' in response:
    message = show_message(message_box = showinfo, message = response)

def show_message(message_box, message):
    return message_box(title = 'Response', message = message)

def set_mode(disabled, normal, *args, **kwargs):
    for item in disabled:
        item['state'] = 'disabled'
    for item in normal:
        item['state'] = 'normal'

def set_target_key_file_on_source(trust, items, *args, **kwargs):
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
target_key_file_on_source = BooleanVar(main)
recursive.set(True)
authentication.set('ssh')
trust.set(False)
target_key_file_on_source.set(True)
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

trust_button = Checkbutton(main, text = 'Establish trust between the servers with a key-pair.', variable = trust, onvalue = True, offvalue = False)

copy_target_key_button = Radiobutton(main, text = 'Copy the key given in the \'Target SSH Key File Path\' to source,\nto establish trust with the target.', variable = target_key_file_on_source, value = False)
password_radiobutton = Radiobutton(main, text = 'Access with Password ', variable = authentication, value = 'password', command = lambda: set_mode(disabled = (source_ssh_file_label, source_ssh_file_entry, source_ssh_password_label, source_ssh_password_entry, target_ssh_file_label, target_ssh_file_entry, target_ssh_password_label, target_ssh_password_entry, copy_target_key_button), normal = (source_password_label, source_password_entry, target_password_label, target_password_entry)))
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
source_ssh_file_label = Label(main, text = 'Source SSH Key File Path: ')
source_ssh_file_label.grid(row = 13, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_file_entry = Entry(main, width = 50)
source_ssh_file_entry.grid(row = 14, column =0, padx = 4, pady = 4, sticky = 'w')
source_ssh_password_label = Label(main, text = 'Source SSH Key File Password(if required): ')
source_ssh_password_label.grid(row = 15, column = 0, padx = 4, pady = 4, sticky = 'w')
source_ssh_password_entry = Entry(main, show = '*', width = 50)
source_ssh_password_entry.grid(row = 16, column = 0, padx = 4, pady = 4, sticky = 'w')

target_ssh_file_label = Label(main, text = 'Target SSH Key-File Path: ')#####Ask user if ssh file for target exists on source
target_ssh_file_label.grid(row = 13, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_file_entry = Entry(main, width = 50)
target_ssh_file_entry.grid(row = 14, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_password_label = Label(main, text = 'Target SSH Key-File Password(if required): ')###Pass ssh-file password with ssh-copy-id
target_ssh_password_label.grid(row = 15, column = 1, padx = 4, pady = 4, sticky = 'w')
target_ssh_password_entry = Entry(main, show = '*', width = 50)
target_ssh_password_entry.grid(row = 16, column = 1, padx = 4, pady = 4, sticky = 'w')

password_radiobutton.invoke()
ssh_radiobutton.invoke()

trust_button.grid(row = 17, column = 0, padx = 4, pady = 4, sticky = 'w')###If ssh key file has password, disable.
target_key_file_on_source_button = Radiobutton(main, text = 'Use target\'s key on the source to establish trust\nbetween the source and the target.', variable = target_key_file_on_source, value = True)
target_key_file_on_source_button.grid(row = 18, column = 0, padx = 4, pady = 4, sticky = 'w')
target_key_file_on_source_label = Label(main, text = 'Enter the path of the key-pair on the source to establish trust: ', state = 'disabled')
target_key_file_on_source_label.grid(row = 19, column = 0, padx = 4, pady = 4, sticky = 'w')
target_key_file_on_source_entry = Entry(main, width = 50, state = 'disabled')
target_key_file_on_source_entry.grid(row = 20, column = 0, padx = 4, pady = 4, sticky = 'w')

copy_target_key_button.grid(row = 18, column = 1, padx = 4, pady = 4, sticky = 'w')
trust_button.configure(command = lambda: set_target_key_file_on_source(checkbutton = trust_button, trust = trust, items = (target_key_file_on_source_button, copy_target_key_button, target_key_file_on_source_label, target_key_file_on_source_entry)))
target_key_file_on_source_button.configure(command = lambda: set_mode(normal = (target_key_file_on_source_label, target_key_file_on_source_entry), disabled = ()), state = 'disabled')
copy_target_key_button.configure(command = lambda: set_mode(disabled = (target_key_file_on_source_label, target_key_file_on_source_entry), normal = ()), state = 'disabled')

recursive_checkbutton = Checkbutton(main, text = 'Recursive', variable = recursive, onvalue = True, offvalue = False)
recursive_checkbutton.grid(row = 21, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'w')
copy_button = Button(main, text = 'Copy', command = lambda source_ssh_file_entry = source_ssh_file_entry, source_username_entry = source_username_entry, source_hostname_entry = source_hostname_entry, target_ssh_file_entry = target_ssh_file_entry, copy_filepath_entry = copy_filepath_entry, target_username_entry = target_username_entry, target_hostname_entry = target_hostname_entry, target_folderpath_entry = target_folderpath_entry, recursive = recursive, source_password = source_ssh_password_entry, target_password = target_ssh_password_entry: threading.Thread(target = local_scp, args = (source_ssh_file_entry, source_username_entry, source_hostname_entry, target_ssh_file_entry, copy_filepath_entry, target_username_entry, target_hostname_entry, target_folderpath_entry, recursive, source_password, target_password)).start())
copy_button.grid(row = 22, column = 0, padx = 4, pady = 4, columnspan = 2, sticky = 'nsew')
main.mainloop()
