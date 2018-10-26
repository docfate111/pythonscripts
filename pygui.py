import tkinter
root=Tinker.tk()
root.Title("title")
def browse():
    print("you are browsing")
label=tkinter.Label(root, text="label")
browseButton=tkinter.button(root, text="button", command=browse)
browseButton.Pack()
label.Pack()
root.mainloop()
#pyinstaller --onefile --windowed "file" (in CMD to make py into exe)