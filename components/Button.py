import tkinter as tk


class Button(tk.Button):
  def __init__(self, parent, *args, **kwargs):
    tk.Button.__init__(self, parent, *args, **kwargs)
    self.parent = parent
