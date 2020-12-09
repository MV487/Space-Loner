from tkinter import *
import pathlib
assets_dir = pathlib.Path.cwd()/"assets"

root = Tk()
root.title("menu")
photo = PhotoImage(file=assets_dir / 'pictures' / 'cogwheel.png')
root.iconphoto(False, photo)

sh1 = Button(image='pictures \ player.png')


mainloop()