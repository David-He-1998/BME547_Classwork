#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:58:28 2022

@author: david
"""
import tkinter as tk
from tkinter import ttk


def main_window():
    def ok_cmd():
        other.configure(state=tk.NORMAL)
        print("ID:{}, name:{}, blood type:{},Rh{}\n Donation center:{}".
              format(ID_entry.get(), name_entry.get(), blood_type.get(),
                     Rh_entry.get(), center.get()))
        print("Click ok")

    def cancel_cmd():
        root.destroy()

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

    root.mainloop()


if __name__ == "__main__":
    main_window()
