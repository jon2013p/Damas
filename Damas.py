from tkinter import*
tk=Tk()
canvas=Canvas(tk, width=645, height=645)
canvas.pack()
canvas.create_rectangle(5,5,80,640)
canvas.create_rectangle(160,5,80,640)
canvas.create_rectangle(240,5,80,640)
canvas.create_rectangle(320,5,80,640)
canvas.create_rectangle(400,5,80,640)
canvas.create_rectangle(480,5,80,640)
canvas.create_rectangle(560,5,80,640)
canvas.create_rectangle(640,5,80,640)


canvas.create_rectangle(5,5,640,80)
canvas.create_rectangle(5,160,640,80)
canvas.create_rectangle(5,240,640,80)
canvas.create_rectangle(5,320,640,80)
canvas.create_rectangle(5,400,640,80)
canvas.create_rectangle(5,480,640,80)
canvas.create_rectangle(5,560,640,80)
canvas.create_rectangle(5,640,640,80)


piezza=PhotoImage(file="piezza.gif")
piezza1=PhotoImage(file="piezza.gif")
piezza2=PhotoImage(file="piezza.gif")
piezza3=PhotoImage(file="piezza.gif")
piezza4=PhotoImage(file="piezza.gif")
piezza5=PhotoImage(file="piezza.gif")
piezza6=PhotoImage(file="piezza.gif")
piezza7=PhotoImage(file="piezza.gif")
piezza8=PhotoImage(file="piezza.gif")
piezza9=PhotoImage(file="piezza.gif")
piezza10=PhotoImage(file="piezza.gif")
piezza11=PhotoImage(file="piezza.gif")

canvas.create_image(10,6, anchor=NW, image=piezza)
canvas.create_image(10,166, anchor=NW, image=piezza1)
canvas.create_image(10,332, anchor=NW, image=piezza2)
canvas.create_image(10,492, anchor=NW, image=piezza3)
canvas.create_image(90,86, anchor=NW, image=piezza4)
canvas.create_image(90,246, anchor=NW, image=piezza5)
canvas.create_image(90,406, anchor=NW, image=piezza6)
canvas.create_image(90,566, anchor=NW, image=piezza7)
canvas.create_image(170,6, anchor=NW, image=piezza8)
canvas.create_image(170,166, anchor=NW, image=piezza9)
canvas.create_image(170,332, anchor=NW, image=piezza10)
canvas.create_image(170,492, anchor=NW, image=piezza11)

x,y=25,15;
def move(event):
    global x,y
    if (x==585 and y==15):   
        if event.keysym=="Up":
            canvas.move(17,0,0)
            y=y
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
        else:
            canvas.move(17,0,0)
            x=x
    elif(x==585 and (y==95 or y==175 or y==255 or y==335 or y==415 or y==495)):
           
        if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
        else:
            canvas.move(17,0,0)
            x=x

    elif(x==585 and y==575):
        if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
        elif event.keysym=="Down":
            canvas.move(17,0,0)
            y=y
        elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
        else:
            canvas.move(17,0,0)
            x=x

    elif (y==15 and x==25):
        if event.keysym=="Up":
            canvas.move(17,0,0)
            y=y
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,0,0)
            x=x
        else:
            canvas.move(17,80,0)
            x=x+80

    elif(y==15 and (x==105 or x==185 or x==265 or x==345 or x==425 or x==505
                    or x==585)):
        
        if event.keysym=="Up":
            canvas.move(17,0,0)
            y=y
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
        else:
            canvas.move(17,80,0)
            x=x+80

    elif(x==25 and (y==95 or y==175 or y==255 or y==335 or y==415 or y==495)):
        if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,0,0)
            x=x
        else:
            canvas.move(17,80,0)
            x=x+80

    elif(x==25 and y==575):
        if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
        elif event.keysym=="Down":
            canvas.move(17,0,0)
            y=y
        elif event.keysym=="Left":
            canvas.move(17,0,0)
            x=x
        else:
            canvas.move(17,80,0)
            x=x+80

    elif(y==575 and (x==105 or x==185 or x==265 or x==345 or x==425 or x==505
                    or x==585)):
         if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
         elif event.keysym=="Down":
            canvas.move(17,0,0)
            y=y
         elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
         else:
            canvas.move(17,80,0)
            x=x+80
         

         
        
    else:
        if event.keysym=="Up":
            canvas.move(17,0,-80)
            y=y-80
        elif event.keysym=="Down":
            canvas.move(17,0,80)
            y=y+80
        elif event.keysym=="Left":
            canvas.move(17,-80,0)
            x=x-80
        else:
            canvas.move(17,80,0)
            x=x+80
        
    
        
canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

tk.mainloop()
