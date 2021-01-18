import tkinter as tk


class Entry(tk.Entry):
  def __init__(self, parent, *args, **kwargs):
    tk.Entry.__init__(self, parent, *args, **kwargs)
    self.parent = parent

  def getText(self):
    return self.get()
