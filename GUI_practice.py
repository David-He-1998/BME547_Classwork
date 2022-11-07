#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:58:28 2022

@author: david
"""
import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk()
    root.title("Blood Donor Database")
    root.geometry("600x400")
    root.rowconfigure(1, minsize=50)
    ttk.Label(root, text="Blood Donor Databse").grid(column=0, row=0)
    ttk.Label(root, text="Name").grid(column=0, row=1)
    ttk.Entry(root, width=50).grid(column=1, row=1, columnspan=2)
    root.mainloop()


if __name__ == "__main__":
    main_window()
