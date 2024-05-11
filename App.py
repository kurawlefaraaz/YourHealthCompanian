from tkinter import *
class GUI:
    def Add_widget_GUI():
        
class func():
    @staticmethod
    def on_move(event):
        component=event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        xpos=(locx+event.x)
        ypos=(locy+event.y)
        component.place(x=xpos,y=ypos)
    def add_widget(self,widget_name):
        widget_name


 
root = Tk()

root.geometry("500x500")
root.title("WhiteBoard")
msg = Label(root, text = "Click & Move")
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<B1-Motion>',func.on_move)
a=Button(text='press',command=func.add_widget).pack()
print()
msg.place(x=10,y=20)
mainloop()