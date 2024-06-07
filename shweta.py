from tkinter import *
from PIL import ImageTk,Image 
from tkinter import messagebox
def handel_login():
    email=email_input.get()
    password=password_input.get()

    if email == "shwetasinghsweety04" and password == "hum@17":
        messagebox.showinfo("yaaayy","login successful")
    else:
        messagebox.showerror("error","login failed")    
root=Tk()
root.title("login form")
root.geometry("500x500")
root.configure(background="#83B4FF")
img=Image.open("image.png")
resized_img=img.resize((100,100))
img=ImageTk.PhotoImage(resized_img)




img_label=Label(root,image=img)
img_label.pack(pady=(10,10))
text_label=Label(root,text="us",fg="white",bg="#83B4FF")
text_label.pack()
text_label.config(font=("verdana",24))

email_label= Label(root,text="enter email",fg="white",bg="#83B4FF")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))
email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label= Label(root,text="enter password",fg="white",bg="#83B4FF")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",12))
password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))


login_btn =Button(root,text="upload file",bg="white",fg="black",command=handel_login)
login_btn.pack(pady=(10,20))

root.mainloop()



