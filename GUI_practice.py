#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:58:28 2022

@author: david
"""
import tkinter as tk
from tkinter import ttk, filedialog
from client import upload_patient_info
from PIL import Image, ImageTk


def upload_data(name, ID, blood, Rh):
    blood_type = blood + Rh
    ID = int(ID)
    msg, status = upload_patient_info(name, ID, blood_type)
    return msg, status


def main_window():
    # def get_update_info():
    #     # command
    #     root.after(2000, get_update_info)  # Update every 2000 ms

    def ok_cmd():
        # if Rh_entry.get() == '':
        #     print("Choose a Rh type")
        #     return
        name = name_entry.get()
        ID = ID_entry.get()
        blood = blood_type.get()
        Rh = Rh_entry.get()
        msg, _ = upload_data(name, ID, blood, Rh)
        print(Rh)
        print("ID:{}, name:{}, blood type:{}\n Donation center:{}".
              format(ID_entry.get(), name_entry.get(), blood_type.get() +
                     Rh_entry.get(), center.get()))
        other.configure(state=tk.NORMAL)
        print("Click ok")
        status.configure(text=msg)

    def cancel_cmd():
        root.destroy()

    def load_img_button():
        # background_img = Image.open("img/angel.jpeg")
        img_filename = filedialog.askopenfilename()
        if img_filename == '':
            return
        background_img = Image.open(img_filename)
        x, y = background_img.size
        newx = 150
        newy = int(y * newx / x)
        background_img = background_img.resize((newx, newy))
        tk_img = ImageTk.PhotoImage(background_img)
        img_label.configure(image=tk_img)
        img_label.image = tk_img

    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("600x400")
    root.rowconfigure(1, minsize=50)
    ttk.Label(root, text="Blood Donor Databse").grid(column=0, row=0,
                                                     columnspan=2, sticky="W")
    ttk.Label(root, text="Name").grid(column=0, row=1)
    name_entry = tk.StringVar()
    ttk.Entry(root, width=40, textvariable=name_entry).\
        grid(column=1, row=1, columnspan=2)  # For text entry

    ttk.Label(root, text="ID").grid(column=0, row=2, sticky=tk.E)
    ID_entry = tk.IntVar()
    ttk.Entry(root, width=10, textvariable=ID_entry).\
        grid(column=1, row=2, sticky="W")
    status = ttk.Label(root, text="status")
    status.grid(column=0, row=7)
    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=2, row=6)

    blood_type = tk.StringVar()
    blood_type.set("O")  # set initial value
    ttk.Label(root, text="Blood type").grid(column=0, row=3, sticky=tk.E)
    ttk.Radiobutton(root, text="A", variable=blood_type, value="A").\
        grid(column=1, row=3, sticky="W")
    ttk.Radiobutton(root, text="B", variable=blood_type, value="B").\
        grid(column=1, row=4, sticky="W")
    ttk.Radiobutton(root, text="AB", variable=blood_type, value="AB").\
        grid(column=1, row=5, sticky="W")
    ttk.Radiobutton(root, text="O", variable=blood_type, value="O").\
        grid(column=1, row=6, sticky="W")

    Rh_entry = tk.StringVar()
    ttk.Checkbutton(root, text="Rh Positive", onvalue="+", offvalue="-",
                    variable=Rh_entry).\
        grid(column=2, row=4, sticky=tk.W)

    ttk.Label(root, text="Nearest Donor Center").grid(column=2, row=2)
    center = tk.StringVar()
    center_combo = ttk.Combobox(root, textvariable=center)
    center_combo.grid(column=3, row=2)
    center_combo["values"] = ["Durham", "Cary", "Raleigh"]
    center_combo.state(["readonly"])
    other = ttk.Button(root, text="Other", state=tk.DISABLED)
    other.grid(column=3, row=4)
    ttk.Button(root, text="cancel", command=cancel_cmd).grid(column=3, row=6)

    background_img = Image.open("img/Marina_Mayuri.jpeg")
    x, y = background_img.size
    newx = 150
    newy = int(y * newx / x)
    background_img = background_img.resize((newx, newy))
    tk_img = ImageTk.PhotoImage(background_img)
    img_label = ttk.Label(root, image=tk_img)
    img_label.configure(image=tk_img)
    img_label.image = tk_img
    img_label.grid(column=1, row=7)
    ttk.Button(root, text="Load Image", command=load_img_button).grid(column=2,
                                                                      row=7)
    root.mainloop()


if __name__ == "__main__":
    main_window()
