import tkinter as tk
from frames.window import MainApplication


def mainLoop():
  root = tk.Tk()
  main = MainApplication(root)
  main.pack(side="top", fill="both", expand=True)
  root.geometry("500x500")
  root.mainloop()


if __name__ == "__main__":
  mainLoop()
