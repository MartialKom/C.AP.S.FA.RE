# coding=utf-8

from tkinter import *
import tkinter as tk
import sys
import os
from pathlib import Path
from fonction import recognise_face, cv2, savefile
from simple_facerec import SimpleFacerec
from tkinter import filedialog as fd
from tkinter.messagebox import showerror
from formulaire import *
from tkinter import ttk
from camera import *
import subprocess

# def chooseDirectory(path):
    
#     face_to_encode_path = Path(path)
#     files = [file_ for file_ in face_to_encode_path.rglob('*.jpeg')]

#     for file_ in face_to_encode_path.rglob('*.png'):
#         files.append(file_)
#     if len(files)==0:
#          #raise ValueError('No faces detect in the directory: {}'.format(face_to_encode_path))
#          showerror(title="Erreur", message="Aucune image trouvee dans le dossier: {}".format(face_to_encode_path))
#     else:
#         global known_face_names 
#         known_face_names= [os.path.splitext(ntpath.basename(file_))[0] for file_ in files]


#         global known_face_encodings 
#         known_face_encodings = []
#         for file_ in files:
#             image = PIL.Image.open(file_)
#             image = np.array(image)
#             face_encoded = encode_face(image)[0][0]
#             known_face_encodings.append(face_encoded)
        
# def choisir_dossier():
#     dir = fd.askdirectory(initialdir="/home/shisui/")
#     chooseDirectory(dir)
#     chemindoss.configure(text=dir)
def value(t):
    x=t.get('1.0','end-1c')
    try:
        x
        return x
    except ValueError:
        showerror(title="Erreur Fatale", message="entrer la source")  
 
def saveVideo():
    global files1
    
    try:
        files = [('Video Files2', '*.avi'),
                ('Video Files1', '*.mp4'),
                ('Video Files1', '*.MP4'),
                ('Video Files2', '*.AVI'),
                ('Video Files3', '*.MKV'),
                ('Video Files3', '*.mkv')]
        files = fd.asksaveasfile(initialdir="/home/" ,filetypes= files, defaultextension=files, initialfile="presence.avi")
        files
        files1 = os.fspath(files.name)
        chemin.configure(text=files1)
    except AttributeError:
        pass
    
    except PermissionError:
        showerror(title="Permissions", message="Vous n'avez pas le droit de sauvegarde a cet emplacement")
    
def takeVideo():
    video_capture = cv2.VideoCapture(s)
    record = cv2.VideoWriter_fourcc(*'XVID')
    try:
        files1
        out = cv2.VideoWriter(files1, record, 6.0, (640,480))
        while True:
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            recognise_face(frame, small_frame, known_face_encodings, known_face_names)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(frame)
            cv2.imshow('Call APP Students face Recognise (video)', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):break

        video_capture.release()
        out.release()
        cv2.destroyAllWindows()
        
    #capture l'exeception si le nom de la video n'est pas defini
    except NameError:
        showerror(title="Erreur Fatale", message="veulliez specifie le nom de la video")
    
def open_text_file():
        
    global f
        
    # file type
    filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
    # show the open file dialog
    f = fd.askopenfile(initialdir="/home/" ,filetypes=filetypes)
    # read the text file and show its content on the Text
    try:
        f
        open_Toplevel2()
     #capture l'exception lever au cas ou aucun fichier n'est choisit
    except AttributeError:
        pass   

def SubmitVideo():
    global s
    try:
        value(t1)
        s = int(value(t1))
        top3.destroy()
        takeVideo()
    #capture l'exception lever au cas ou la source de la camera n'est pas definie
    except ValueError:
        showerror(title="Erreur Fatale", message="entrer le numero de la camera source")  
    

def lancer_camera():
    video_capture = cv2.VideoCapture(s)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        recognise_face(frame, small_frame, known_face_encodings, known_face_names)
        cv2.imshow('Call APP Students face Recognise', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    release = video_capture.release()
    try:
        release
        cv2.destroyAllWindows()
    except ValueError:
        showerror(title="Fatal Error", message="entrer le numero de la camera source")
        
def SubmitCamera():
    global s
    try:
        value(t1)
        s = int(value(t1))
        top4.destroy()
        lancer_camera()
       
        
    #capture l'exception lever au cas ou la source de la camera n'est pas definie
    except ValueError:
        showerror(title="Erreur fatal", message="entrer le numero de la camera source")

def select_file():
    global file_to_print

    file_to_print = fd.askopenfilename(
      initialdir="/home/", title="Select file", 
      filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    fichier.configure(text=file_to_print)

def print_file():
    if file_to_print:
        os.system("lpr -P {}".format(file_to_print))
        try:
            subprocess.run(['lpr'], check= True)
        except subprocess.CalledProcessError:
            showerror(title="Erreur", message="Aucune imprimante branchee")
        
    
# Creation de la fenetre principale
root = Tk()
root.resizable(False, False)
root.geometry("610x400")
root.title("Call App Student Face Recognise")
root.minsize(400,400)
#root.iconbitmap("RFC1.ico")

# --------------------------------------Analyser Video
def parcourir():
    
    ch = fd.askopenfile(initialdir="/home/shisui/", title="Aucune video selectionnee",
        filetypes = (("Video Files", "*.avi"),("Video Files","*.mp4"),("Video Files","*.mkv"),("Video Files","*.MP4")
                     ,("Video Files","*.AVI"),("Video Files","*.MKV")))
    try:
        ch
        video_source =ch.name
        App(Toplevel(), "Call App Student Face Recognise", video_source)
    except AttributeError:
        pass

def command1(event):
    if entry1.get() == 'admin' and entry2.get() == 'password' or entry1.get() == 'test' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()
  
def command2():
        top.destroy()
        root.destroy()
        sys.exit()

#creation de l'interface de connexion+++++++++++++++

top = Toplevel()
top.geometry('300x200')
top.title('Connexion')
top.configure(background = 'white')

    #creation d'une zone travaille dans top
frmlog = Frame(top , bg='#3C3C3C' )
frmlog . place (x=0, y=0, width=300,height=200)

    #tete de l'application
lblco=Label(frmlog, text="connecter vous", bg='#3C3C3C',fg='#FFFFFF', font = ('purisa',20))
lblco.place(x=41, y=15, width=220,height=25)
    #login
lbl1= Label(frmlog, text = 'Login', bg='#3C3C3C',fg='#FFFFFF', font = ('purisa',15))
lbl1.place(x=2, y=67, width=95,height=23)

entry1=Entry(frmlog, bd=2, font = ('purisa',15))
entry1.place(x=110, y=67, width=135,height=25)
    #password
lbl2 = Label(frmlog, text = 'Password', bg='#3C3C3C',fg='#FFFFFF', font = ('purisa',15))
lbl2.place(x=2, y=100, width=100,height=23)

entry2=Entry(frmlog, bd=2, show="*", font = ('purisa',15))
entry2.place(x=110, y=100, width=135,height=25)
    #bouton quit
buttonquit2= Button(frmlog, text='cancel',font = ('purisa',15), bg='#AA0000', command=lambda:command2())
buttonquit2.place(x=118, y=165, width=80,height=26)
entry2.bind('<Return>', command1)


img =PhotoImage(file = "plan22.gif")  
label =Label(root, image = img)
width=610
height=400
label.grid()

def open_Toplevel2():
    
    top2 = Toplevel()
    top2.title("Editeur de texte")
    top2.geometry("550x250")
    
    # Editeur
    text = Text(top2, height=12)
    text.grid(column=0, row=0, sticky='nsew')
    text.insert('1.0', f.readlines())
    
    top2.mainloop()

def open_Toplevel3():
    
    global chemin, chemindoss, t1, top3
    
    top3= Toplevel()
    top3.resizable(False, False)
    top3.title("Video")
    top3.geometry("360x260")
    
    fen= Frame(top3 , bg='#3C3C3C' )
    fen.place (x=0, y=0, width=360,height=260)
    
    # Save video
    labela8 = Label(fen, text = "Enregistrer une video",bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    labela8.pack(side=RIGHT, pady=65, fill=X)
    labela8.place(x=65, y=5, width=212,height=20)

        
    nom = Label(fen, text = 'Nom',bg='#3C3C3C',fg='#AF9564',font=("purisa", 112 ))
    nom.place(x=2, y=35, width=60,height=23)
 
    chemin = Label(fen, text = 'Aucune video enregistrer',bg='#3C3C3C',fg='#FFFFFF')
    chemin.place(x=55, y=35, width=280,height=23)

    btn = Button(fen, text='Enregistrer',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ), command=lambda : saveVideo())
    btn.place(x=250, y=65, width=100,height=25)
    
    # Save file
    label12 = Label(fen, text = "veulliez selectionner le fichier",bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    label12.pack(side=RIGHT, pady=65, fill=X)
    label12.place(x=35, y=95, width=270,height=20)

        
    nom = Label(fen, text = 'Nom',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    nom.place(x=2, y=115, width=60,height=23)
 
    cheminfile = Label(fen, text = 'aucun fichier enregister',bg='#3C3C3C',fg='#FFFFFF')
    cheminfile.place(x=60, y=115, width=280,height=23)

    btn = Button(fen, text='Enregistrer',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ), command=lambda : savefile(cheminfile))
    btn.place(x=250, y=140, width=100,height=25)
    
    
 
    #choose directory
    # labela50 = Label(fen, text = "selectionner un dossier contenant les images",font=("times new romen", 10 ))
    # labela50.pack(side=RIGHT, pady=65, fill=X)
    # labela50.place(x=10, y=95, width=350,height=17)

    # doss = Label(fen, text = 'Dossier', bg='#E1E1E1', font = ('helvetica',10))
    # doss.place(x=2, y=115, width=60,height=23)

    # chemindoss = Label(fen, text = 'Aucun dossier selectionner', bg='#E1E1E1', font = ('helvetica',8))
    # chemindoss.place(x=70, y=115, width=280,height=23)

    # butn = ttk.Button(fen, text='Select', command=lambda : choisir_dossier())
    # butn.place(x=250, y=140, width=100,height=25)
 
    #choose source
    sl = Label(fen,text="Numero de la camera source",bg='#3C3C3C',fg='#AF9564',font=("purisa", 11 ))
    sl.pack(side=RIGHT, pady=65, fill=X)
    sl.place(x=65, y=170, width=250,height=17)
 
    cam = Label(fen, text = 'Camera',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    cam.place(x=2, y=190, width=70,height=23)
 
    t1=Text(fen, height=23, width=40,font=("purisa", 12 ))
    t1.place(x=80, y=190, width=40,height=23)
 
    btns = Button(fen, text='Submit',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ), command=lambda : SubmitVideo())
    btns.place(x=260, y=210, width=80,height=25)

    top3.mainloop()

def open_Toplevel4():
    
    global cheminfile, chemindoss, t1, top4
    
    top4= Toplevel()
    top4.resizable(False, False)
    top4.title("Demarrer la camera")
    top4.geometry("360x150")
    fen= Frame(top4 , bg='#3C3C3C' )
    fen.place (x=0, y=0, width=360,height=150)
    
    # Save file
    label12 = Label(fen, text = "veulliez selectionner un fichier",bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    label12.pack(side=RIGHT, pady=65, fill=X)
    label12.place(x=57, y=5, width=270,height=20)

        
    nom = Label(fen, text = 'Nom',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    nom.place(x=2, y=35, width=60,height=23)
 
    cheminfile = Label(fen, text = 'aucun fichier enregister',bg='#3C3C3C',fg='#FFFFFF', font = ('purisa',12))
    cheminfile.place(x=70, y=35, width=280,height=23)

    btn = Button(fen, text='Enregistrer',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ), command=lambda : savefile(cheminfile))
    btn.place(x=250, y=65, width=100,height=25)
 
    #choose directory
    # labela50 = Label(fen, text = "selectionner un dossier contenant les images",font=("times new romen", 10 ))
    # labela50.pack(side=RIGHT, pady=65, fill=X)
    # labela50.place(x=10, y=95, width=350,height=17)

    # doss = Label(fen, text = 'Dossier', bg='#E1E1E1', font = ('helvetica',10))
    # doss.place(x=2, y=115, width=60,height=23)

    # chemindoss = Label(fen, text = 'Aucun dossier selectionner', bg='#E1E1E1', font = ('helvetica',8))
    # chemindoss.place(x=70, y=115, width=280,height=23)

    # butn = ttk.Button(fen, text='Select', command=lambda : choisir_dossier())
    # butn.place(x=250, y=140, width=100,height=25)
 
    #choose source
    sl = Label(fen,text="Numero de la camera source",bg='#3C3C3C',fg='#AF9564',font=("purisa", 11 ))
    sl.pack(side=RIGHT, pady=65, fill=X)
    sl.place(x=47, y=95, width=235,height=17)
 
    cam = Label(fen, text = 'Camera', bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ))
    cam.place(x=2, y=115, width=70,height=23)
 
    t1=Text(fen, height=23, width='40', font = ('purisa',12))
    t1.place(x=80, y=115, width=40,height=23)
 
    btns = Button(fen, text='Submit',bg='#3C3C3C',fg='#AF9564',font=("purisa", 12 ), command=lambda :principale() )
    btns.place(x=250, y=115, width=80,height=25)

    top4.mainloop()

def open_Toplevel6():

    top6= Toplevel()
    top6.resizable(False, False)
    top6.title("Imprimer les fiches de presence")
    top6.geometry("320x120")
    
    fen= Frame(top6 , bg='#3C3C3C' )
    fen.place (x=0, y=0, width=320,height=120)
    
    labeli6= Label(fen, text = "Choisir le fichier a imprimer",font=("purisa", 10 ),bg='#3C3C3C',fg='#FFFFFF')
    labeli6.pack(side=RIGHT, pady=65, fill=X)
    labeli6.place(x=40, y=5, width=212,height=25)
    
    global fichier
    
    fichier = Label(fen, text="Aucun fichier selectionner ", bd=2, font = ('purisa',10),bg='#3C3C3C',fg='#FFFFFF')
    fichier.place(x=8, y=50, width=238,height=23)

    buttonParcourir= Button (fen,text="Parcourir", command= select_file, fg="#FF7800", bg='white',font = ('purisa',10))
    buttonParcourir.place(x=240, y=50, width=75,height=25)
 
    Bt_c4= Button(fen, text ="Imprimer", command=print_file, font=(" purisa", 10))
    Bt_c4.place(x=80, y=75, width=75,height=25)
    
    top6.mainloop()
    
def principale():
    global s
    sfr= SimpleFacerec()
    sfr.load_encoding_images("image/")
    value(t1)
    s = int(value(t1))
#Démarrer la caméra (webcam)
    cap= cv2.VideoCapture(s)

    while True:
        ret, frame= cap.read()
    
    #Deetction fasciale
        face_locations, face_names =sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            top, left, bottom, right= face_loc[0], face_loc[1],face_loc[2], face_loc[3]
            if name == "Inconnue":
                cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,200 ),2)
                cv2.rectangle(frame, (left,top),(right,bottom),(0,0,200),4)
            else:
                cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0 ),2)
                cv2.rectangle(frame, (left,top),(right,bottom),(0,255,0),4)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def open_Toplevel7():

    top7= Toplevel()
    top7.resizable(False, False)
    top7.title("Visualiser les presences")
    top7.geometry("405x160")        
    
    fen= Frame(top7 , bg='#3C3C3C' )
    fen.place (x=0, y=0, width=405,height=160)

    labelg7= Label(fen, text = "Choisir la liste a visualiser",bg='#3C3C3C',fg='#AF9564' ,font = ('purisa',10))
    labelg7.pack(side=RIGHT, pady=65, fill=X)
    labelg7.place(x=95, y=5, width=195,height=25)


    #les sour bouton de la fen....
    Bt_m4= Button(fen, text ="liste de presences", bg='#3C3C3C',fg='#AF9564',command = open_text_file, font = ('purisa',10))
    Bt_m4.pack(side=RIGHT, pady=65, fill=X)
    Bt_m4.place(x=95, y=40, width=180,height=25)
    
    # Save file
    label12 = Label(fen, text = "veulliez selectionner un fichier",bg='#3C3C3C',fg='#AF9564',font = ('purisa',10))
    label12.pack(side=RIGHT, pady=65, fill=X)
    label12.place(x=65, y=80, width=300,height=17)

        
    nom = Label(fen, text = 'Nom', bg='#3C3C3C',fg='#AF9564', font = ('purisa',10))
    nom.place(x=2, y=100, width=60,height=23)
 
    cheminfile = Label(fen, text = 'aucune liste cree',bg='#3C3C3C',fg='#FFFFFF', font = ('purisa',10))
    cheminfile.place(x=56, y=100, width=280,height=23)

    btn = Button(fen, text='Enregistrer',bg='#3C3C3C',fg='#AF9564', command=lambda : savefile(cheminfile),font = ('purisa',10))
    btn.place(x=300, y=100, width=100,height=25)

    #analyser une video
    Bt_ma4= Button(fen, text ="Analyser une video",bg='#3C3C3C',fg='#AF9564', command=parcourir, font = ('purisa',10))
    Bt_ma4.pack(side=RIGHT, pady=65, fill=X)
    Bt_ma4.place(x=95, y=130, width=180,height=25)

    
    top7.mainloop()

#Creation  frame arriere plan vert pour le haut
frm = Frame(root , bg='#E1E1E1', bd=2 )
img0 =PhotoImage(file = "plan22.gif")
canvas=Canvas(frm, width=600, height=300, bg='#5A5A5A')
canvas.create_image(width/2, height/2, image=img0)
canvas.pack()
# Emplacement du frame
frm . place (x=10, y=0, width=590,height=75)

#Creation frame arriere plan vert pour le bas
frm1 = Frame(root , bg='#002B00' )
img1 =PhotoImage(file = "plan5.gif")
canvas=Canvas(frm1, width=600, height=300, bg='#5A5A5A')
canvas.create_image(width/2, height/2, image=img1)
canvas.pack()
# Emplacement du frame
frm1 . place (x=10, y=90, width=200,height=300)

#Creation  frame arriere plan vert
frm2 = Frame(root , bg='#5A5A5A' )
img2 =PhotoImage(file = "plan1.gif")
canvas=Canvas(frm2, width=600, height=300, bg='#5A5A5A')
canvas.create_image(width/3, height/3, image=img2)
canvas.pack()
# Emplacement du frame
frm2 . place (x=220, y=90, width=380,height=300)
#fin de la cration des differente section de lapplication

#sous-titre interne au logiciel
soustitre= Label(frm, text="C.AP.S.FA.RE", font = ('purisa',18), bg='#5A5A5A', fg='#000000')
soustitre.pack(expand=YES)
soustitre.place(x=125, y=2, width=364,height=25)

soustitre1= Label(frm, text="V1.0", font = ('purisa',11), bg='#5A5A5A', fg='#FFFFFF')
soustitre1.pack(expand=YES)
soustitre1.place(x=444, y=7, width=45,height=20)

acceuil_bt= Button(frm, text="Acceuil", font = ('purisa',15),bg='#41B77F' ,command = root)
acceuil_bt.pack(expand=YES, pady=65, fill=X)
acceuil_bt.place(x=10, y=32, width=130,height=33)

#ferme le logiciel
Boutquit = Button(frm1, text = 'Quitter', font = ('purisa',13), bg='#AA0000',command =root.destroy)
Boutquit.pack(side=RIGHT,pady=65, fill=X)
Boutquit.place(x=22, y=255, width=130,height=33)
    # Ajouter une image au boutton gere presence
imgequit =PhotoImage(file = "rouge Quit.png")  
labelquit =Label(Boutquit, image = imgequit)
labelquit.grid()

#******************Mis en commentaire ************************
#differente tache a realiser dans lapplication
#btn_fill2 = Button(frm1, text="Ajouter etudiant", font = ('purisa',9), bg='#D2D2D2',command = lambda:form())
#btn_fill2.pack(expand=YES, pady=65, fill=X)
#btn_fill2.place(x=8, y=10, width=185,height=33)
        # Ajouter une image au boutton etudiant
#imgetudiant =PhotoImage(file = "etudiant.png")  
#labelet =Label(btn_fill2, image = imgetudiant)
#labelet.grid()

#btn_fill5 = Button(frm1, text="Importer photo", font = ('purisa',10), bg='#D2D2D2',command = '')
#btn_fill5.pack(expand=YES, pady=65, fill=X)
#btn_fill5.place(x=8, y=50, width=185,height=33)
        # Ajouter une image au boutton source
#imgeadmin =PhotoImage(file = "adimin.png")  
#labeladmin =Label(btn_fill5, image = imgeadmin)
#labeladmin.grid()

btn_fill4 = Button(frm1, text="Lancer la caméra", bg='#D2D2D2', font = ('purisa',9),command =open_Toplevel4 )
btn_fill4.pack(expand=YES, pady=65, fill=X)
btn_fill4.place(x=8, y=90, width=185,height=33)
# Ajouter une image au boutton camera
imgelancer =PhotoImage(file = "lancer camera.png")  
labellancer =Label(btn_fill4, image = imgelancer)
labellancer.grid()

btn_fill3 = Button(frm1, text="Prendre une video", bg='#D2D2D2', font = ('purisa',9),command = open_Toplevel3)
btn_fill3.pack(expand=YES, pady=65, fill=X)
btn_fill3.place(x=8, y=130, width=185,height=33)
# Ajouter une image au boutton departement
imgedepart =PhotoImage(file = "Gere departement.png")  
labeldepar =Label(btn_fill3, image = imgedepart)
labeldepar.grid()

#btn_fill6 = Button(frm1, text="Imprimer", font = ('purisa',9), bg='#D2D2D2', command = open_Toplevel6)
#btn_fill6.pack(expand=YES, pady=65, fill=X)
#btn_fill6.place(x=8, y=170, width=185,height=33)
        # Ajouter une image au boutton imprimer
#imgedoc =PhotoImage(file = "imprimer doc.png")  
#labeldoc =Label(btn_fill6, image = imgedoc)
#labeldoc.grid()

#Bouton1 = Button(frm1, text = "Visualiser presence", bg='#D2D2D2', font = ('purisa',9), command = open_Toplevel7 )
#Bouton1.pack(side=RIGHT, pady=65, fill=X)
#Bouton1.place(x=8, y=210, width=185,height=33)
    # Ajouter une image au boutton gere présence
#imgeajout =PhotoImage(file = "Ajout presence.png")  
#labelajout =Label(Bouton1, image = imgeajout)
#labelajout.grid()

#root. config (menu=menuBar)
root.withdraw()
root.mainloop()










