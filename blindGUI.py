from PIL import Image, ImageTk
from tkinter import Button
from tkinter import Tk, StringVar, Frame, Label,Entry, messagebox
from tkinter import filedialog
from mysql import upload, delete
def remove_mariadb():
    global name_entry
    flag = delete(name_entry.get())
    if flag==0:
        messagebox.showinfo("showinfo", f"removed {name_entry.get()} ")
    else:
        messagebox.showerror("error", f" cold not add User {name_entry.get()} check connection with raspberry pi")
def upload_mariadb():
    global name_entry
    print(root.filename)
    print(name_entry.get())
    flag = upload( name_entry.get(),root.filename)
    if flag==0:
        messagebox.showinfo("showinfo", f"User {name_entry.get()}  added")
    else:
        messagebox.showerror("error", f" cold not add User {name_entry.get()} check connection with raspberry pi")
def open_and_resize(file):
    #Load an image in the script
    img= Image.open(file)

    #Resize the Image using resize method
    resized_image= img.resize((300,400), Image.LANCZOS)
    
    return resized_image
def open():
    global frame
    global face
    global face_label
    root.filename = filedialog.askopenfilename(initialdir="/home/anirudhan/Pictures/project/", title="Select a image", filetypes=(("jpg image","*.jpg"),("png image","*.png"),("all files","*.*")))
    print(root.filename)
    face = ImageTk.PhotoImage(open_and_resize(root.filename))
    face_label.configure(image=face)
root = Tk()
root.title("Upload Images")
root.geometry("800x600")
name_var=StringVar()
frame = Frame(root, width=600, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)
face_label = Label(frame)
load_file_button = Button(root,text='Open Image',command=open)
load_file_button.grid(row=0,column=0)
face_label.grid(row=1,column=0)
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
add_image_mariadb = Button(root,text='Add + ',command=upload_mariadb,font=('calibre',10, 'bold'))
del_mariadb = Button(root,text='Del - ',command=remove_mariadb,font=('calibre',10, 'bold'))
name_label.grid(row=2,column=0)
name_entry.grid(row=2,column=1)
add_image_mariadb.grid(row=2,column=3)
del_mariadb.grid(row=2,column=4)
root.mainloop()
