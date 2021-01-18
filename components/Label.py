import tkinter as tk


class Label(tk.Label):
  def __init__(self, parent, *args, **kwargs):
    tk.Label.__init__(self, parent, *args, **kwargs)
    self.parent = parent
