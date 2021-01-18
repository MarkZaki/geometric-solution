import tkinter as tk
from components.Entry import Entry
from components.Button import Button
from components.Label import Label


class MainApplication(tk.Frame):
  def __init__(self, parent, *args, **kwargs):
    tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent
    self.elementsFactory()
    self.draw()

  def getInputs(self):
    text = self.x1.getText()
    print(text)

  def elementsFactory(self):
    self.x1 = Entry(self)
    self.x1 = Entry(self)
    self.submitButton = Button(
        self, bg="green", text="Submit", fg="white", command=self.getInputs)

  def draw(self):
    self.x1.pack(side="top", fill="x")
    self.submitButton.pack(side="bottom", fill="x")
