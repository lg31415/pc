from tkinter import *

root = Tk()


textLabel = Label(root,
                  text = "您所下载的影片包含有未成年限制",
                  justify = LEFT,
                  padx = 10,
                  )
textLabel.pack(side=LEFT)

photo = PhotoImage(file='18.gif')
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

mainloop()