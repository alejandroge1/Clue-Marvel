import random
from tkinter import *
import tkinter as tk

raiz=Tk()
raiz.title("CLUE- MARVEL")
raiz.resizable(0,0) #ancho,alto
raiz.iconbitmap("CLUE_logo.ico")

frame=Frame()
frame.pack()
frame.config(bg="white")
frame.config(width="1000",height="500")

canvas = tk.Canvas(frame, width=1000, height=500)
canvas.pack()
img= tk.PhotoImage(file="MENU.png")
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

final= random.randint(1,5)
        
print ("Final elegido:", final)

  

def f_elegir():
    
    for widgets in frame.winfo_children():
      widgets.destroy()
      
    canvas = tk.Canvas(frame, width=1000, height=500)
    canvas.pack()
    img= tk.PhotoImage(file="ELECCION.png")
    canvas.background = img
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

    
    b_salir=tk.Button(frame,text="Salir del juego", command= f_salir)
    b_salir.place(x=830, y=450)
    b_salir.config(fg="white", bg="red",)
    b_salir.config(font=('helvetica', 15,"bold" ))
      
    s_personaje= IntVar()
    s_lugar= IntVar()
    s_arma= IntVar()
    
    rb_persoanaje= tk.Radiobutton(raiz,text= "LOKI", value= 1, variable = s_personaje).place (x=150, y=250) 
    rb_persoanaje= tk.Radiobutton(raiz,text= "RED SKULL", value= 2, variable = s_personaje).place (x=150, y=300) 
    rb_persoanaje= tk.Radiobutton(raiz,text= "DUENDE VERDE", value= 3, variable = s_personaje).place (x=150, y=350) 
    rb_persoanaje= tk.Radiobutton(raiz,text= "VENOM", value= 4, variable = s_personaje).place (x=150, y=400) 
    rb_persoanaje= tk.Radiobutton(raiz,text= "MAGNETO", value= 5, variable = s_personaje).place (x=150, y=450) 
    
    
    rb_lugar= tk.Radiobutton(frame,text= "SHIELD", value= 1, variable = s_lugar).place (x=400, y=250) 
    rb_lugar= tk.Radiobutton(frame,text= "ASGARD", value= 2, variable = s_lugar).place (x=400, y=300) 
    rb_lugar= tk.Radiobutton(frame,text= "WAKANDA", value= 3, variable = s_lugar).place (x=400, y=350) 
    rb_lugar= tk.Radiobutton(frame,text= "TORRE STARK", value= 4, variable = s_lugar).place (x=400, y=400) 
    rb_lugar= tk.Radiobutton(frame,text= "MANSION-X", value= 5, variable = s_lugar).place (x=400, y=450) 
    
    
    
    rb_arma= tk.Radiobutton(frame,text= "MJOLNIR", value= 1, variable =s_arma).place (x=650, y=250) 
    rb_arma= tk.Radiobutton(frame,text= "ESCUDO DE CAPITAN AMERICA", value= 2, variable = s_arma).place (x=650, y=300) 
    rb_arma= tk.Radiobutton(frame,text= "ARCO DE HAWKEYE", value= 3, variable =s_arma).place (x=650, y=350) 
    rb_arma= tk.Radiobutton(frame,text= "REACTOR ARC", value= 4, variable = s_arma).place (x=650, y=400) 
    rb_arma= tk.Radiobutton(frame,text= "BLASTER DE ROCKET", value= 5, variable =s_arma).place (x=650, y=450) 
    
    
    def f_verificar():
        
        b_ver.destroy()
        p=  s_personaje.get()
        l=  s_lugar.get()
        ar= s_arma.get()
        
        if personaje==p and ubicacion==l and arma==ar:
            print("Correcto")
            label_c= tk.Label(frame, text= "¡CORRECTO! Adivinaste al culpable.", fg= "green",
                              bg= "white", font=('helvetica', 15,"bold" )).place (x=150, y=150) 
           
            
        else:
            print("incorrecto")
            label_c= tk.Label(frame, text= "¡INCORRECTO! No adivinaste al culpable.", fg= "red",
                              bg= "white", font=('helvetica', 15,"bold" )).place (x=150, y=150) 
            
            label_c= tk.Label(frame, text=("El culpable fue", tpersonaje, ". Robó la gema del infinito en",tubicacion, "con el",tarma,".") ,
                              fg= "black",
                              bg= "white", font=('helvetica', 9)).place (x=100, y=180) 
            
            
    
    
    b_ver=tk.Button(frame,text="Verificar respuestas", command= f_verificar)
    b_ver.place(x=813, y=410)
    b_ver.config(fg="white", bg="blue",)
    b_ver.config(font=('helvetica', 12,"bold" ))

    
    return (s_personaje.get(), s_lugar.get(), s_arma.get())
        
def f_salir():
    
    raiz.destroy()
    

if final == 1:
   
    def f_wakanda ():
        
        ventana = tk.Toplevel()
        ventana.title("Wakanda")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Wakanda1.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_mansionx ():
        
        ventana = tk.Toplevel()
        ventana.title("Mansion-X")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Mansion X.1.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_shield():
        
        ventana = tk.Toplevel()
        ventana.title("Shield")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="SHIELD.1.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_stark():
        
        ventana = tk.Toplevel()
        ventana.title("Torre Stark")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Torre Stark.1.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_asgard():
        
        ventana = tk.Toplevel()
        ventana.title("Asgard")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="ASGARD.1.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()


    personaje= 1
    arma= 1
    ubicacion= 1
    
    tpersonaje= "LOKI"
    tarma= "MJOLNIR"
    tubicacion= "SHIELD"
    
if final == 2:
    
    def f_wakanda ():
        
        ventana = tk.Toplevel()
        ventana.title("Wakanda")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Wakanda.2.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_mansionx ():
        
        ventana = tk.Toplevel()
        ventana.title("Mansion-X")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Mansion X.2.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_shield():
        
        ventana = tk.Toplevel()
        ventana.title("Shield")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="SHIELD.2.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_stark():
        
        ventana = tk.Toplevel()
        ventana.title("Torre Stark")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Torre Stark.2.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_asgard():
        
        ventana = tk.Toplevel()
        ventana.title("Asgard")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="ASGARD.2.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
    
    personaje= 2
    arma= 2
    ubicacion= 2  
    
    
    tpersonaje= "RED SKULL"
    tarma= "ESCUDO DE CAPITAN AMERICA"
    tubicacion= "ASGARD" 

if final == 3:
    
    def f_wakanda ():
        
        ventana = tk.Toplevel()
        ventana.title("Wakanda")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Wakanda.3.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_mansionx ():
        
        ventana = tk.Toplevel()
        ventana.title("Mansion-X")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Mansion X.3.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_shield():
        
        ventana = tk.Toplevel()
        ventana.title("Shield")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="SHIELD.3.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_stark():
        
        ventana = tk.Toplevel()
        ventana.title("Torre Stark")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Torre Stark.3.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_asgard():
        
        ventana = tk.Toplevel()
        ventana.title("Asgard")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="ASGARD.3.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
    
    personaje= 3
    arma= 3
    ubicacion= 3 
    
    tpersonaje= "DUENDE VERDE"
    tarma= "ARCO DE HAWKEYE"
    tubicacion= "WAKANDA" 
    
if final == 4:
    
    def f_wakanda ():
        
        ventana = tk.Toplevel()
        ventana.title("Wakanda")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Wakanda.4.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_mansionx ():
        
        ventana = tk.Toplevel()
        ventana.title("Mansion-X")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Mansion X.4.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_shield():
        
        ventana = tk.Toplevel()
        ventana.title("Shield")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="SHIELD.4.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_stark():
        
        ventana = tk.Toplevel()
        ventana.title("Torre Stark")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Torre Stark.4.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_asgard():
        
        ventana = tk.Toplevel()
        ventana.title("Asgard")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="ASGARD.4.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
    
    personaje= 4
    arma= 4
    ubicacion= 4 
    
    tpersonaje= "VENOM"
    tarma= "REACTOR ARC"
    tubicacion= "TORRE STARK" 
    
if final == 5:
    
    def f_wakanda ():
        
        ventana = tk.Toplevel()
        ventana.title("Wakanda")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Wakanda.5.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_mansionx ():
        
        ventana = tk.Toplevel()
        ventana.title("Mansion-X")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Mansion X.5.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_shield():
        
        ventana = tk.Toplevel()
        ventana.title("Shield")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="SHIELD.5.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_stark():
        
        ventana = tk.Toplevel()
        ventana.title("Torre Stark")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="Torre Stark.5.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
        
    def f_asgard():
        
        ventana = tk.Toplevel()
        ventana.title("Asgard")
        ventana.resizable(0,0) #ancho,alto
        ventana.iconbitmap("CLUE_logo.ico")
        ventana.geometry("1000x500")
        
        img= tk.PhotoImage(file="ASGARD.5.png")
        lbl= tk.Label(ventana, image= img).place(x=0,y=0)
        lbl.pack()
    
    personaje= 5
    arma= 5
    ubicacion= 5 
    
    tpersonaje= "MAGNETO"
    tarma= "BLASTER DE ROCKET"
    tubicacion= "MANSION-X" 
    

print("El culpable fue",personaje, ". Robó la gema del infinito en",ubicacion, "con el",arma,".")

b_wakanda=Button(frame,text="Ir a Wakanda",command= f_wakanda)
b_wakanda.place(x=150, y=180)
b_wakanda.config(fg="white", bg="black")
b_wakanda.config(font=('helvetica', 12,"bold" ))

b_xmen= Button(frame,text="Ir a Mansion-X", command= f_mansionx)
b_xmen.place(x=440, y=145)
b_xmen.config(fg="white", bg="black")
b_xmen.config(font=('helvetica', 12,"bold" ))

b_asgard= Button(frame,text="Ir a Asgard", command= f_asgard)
b_asgard.place(x=760, y=150)
b_asgard.config(fg="white", bg="black")
b_asgard.config(font=('helvetica', 12,"bold" ))

b_tstark= Button(frame,text="Ir a Torre Stark",command= f_stark)
b_tstark.place(x=300, y=330)
b_tstark.config(fg="white", bg="black")
b_tstark.config(font=('helvetica', 12,"bold" ))

b_shield= Button(frame,text="Ir a Shield",command= f_shield)
b_shield.place(x=620, y=305)
b_shield.config(fg="white", bg="black")
b_shield.config(font=('helvetica', 12,"bold" ))

b_terminar= Button(frame,text="CONTINUAR",command=  f_elegir)
b_terminar.place(x=850, y=450)
b_terminar.config(fg="white", bg="red",)
b_terminar.config(font=('helvetica', 15,"bold" ))

    
raiz.mainloop()
