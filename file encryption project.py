import tkinter as tk
from tkinter import filedialog,messagebox
from cryptography.fernet import Fernet

#function to generate a key
def generate_key():
    key=Fernet.generate_key()
    with open("message.key","wb") as file:
        file.write(key)

#function to encrypt a file
def encrypt_file():
    file_path=filedialog.askopenfilename(title="Select afile to Encrypt")
    if not file_path:
        return
    k=open("message.key","rb").read()
    f=Fernet(k)
    with open(file_path,"rb") as file:
        original_text=file.read()
    
        encrypted=f.encrypt(original_text) # encrypting text inside file

        with open(file_path+".enc","wb") as encrypted_file:
            encrypted_file.write(encrypted)
        messagebox.showinfo("Sucessfully File has been encrypted")
                   
#function to decrypt an encrypted file          
def decrypt_file():
    file_path=filedialog.askopenfilename(title="Select Encrypted file")
    if not file_path:
        return
    k=open("message.key","rb").read()
    f=Fernet(k)
    
    try:
        with open(file_path,"rb") as enc_file:
            encrypted_data=enc_file.read()
            
            decrypted=f.decrypt(encrypted_data) #decrypting text 
            
            decrypted_file_path=file_path.replace(".enc","decrypt.txt")
            with open(decrypted_file_path,"wb") as dec_file:
                dec_file.write(decrypted)
        messagebox.showinfo("Successfully File has been decrypted")
        
    except Exception:
       messagebox.showerror("Error Decryption failed! Wrong key or corrupted file")
    
   
if __name__=="__main__":
    generate_key()
    root=tk.Tk()
    root.title("File encryption/Decryption Tool")
    root.geometry("400x350")
    root.configure(bg="lightyellow")
    
title=tk.Label(root,text="File Encryption/Decryption tool",font=("Times New Roman",18,"bold"),bg="yellow")
title.pack(pady=20)

#creating buttons    
encrypted_button=tk.Button(root,text="Encrypt file",command=encrypt_file,font=("Calibri",12,"bold"),bg="lightblue",width=20)
encrypted_button.pack(pady=10)

decrypted_button=tk.Button(root,text="Decrypt file",command=decrypt_file,font=("Calibri",12,"bold"),bg="lightblue",width=20)
decrypted_button.pack(pady=10)

footer=tk.Label(root,text="Micro IT Internship",font=("Times New Roman",18,"bold"),bg="yellow")
footer.pack(side="bottom",pady=10)

root.mainloop()






