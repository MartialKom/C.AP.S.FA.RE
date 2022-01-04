from tkinter import *
from tkinter import filedialog as fd 
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageTk
from fonction_BD import Etudiant, insertBLOB

#+++++++++++++++++++++++++++liste formulaire+++++++++++++++++++++++
def listeInscrit(fenetre, liste):
		newFen=Toplevel(fenetre)
		newFen.resizable(False, False)
		newFen.geometry("700x300")
		newFen.title("liste des etudiants")

		#definition de l'organisation de la fenetre

		cont1 = Frame(newFen , bg='#3C3C3C' )
		cont1.place (x=0, y=0, width=700,height=400)

		listeCan=Canvas(cont1, bg="#D2D2D2")
		listeCan.grid(row=0, column=0)
  
		fonttLabel='arial 11 bold'

	#organisation de la liste d'enregistrement des etudiant

		resultat = Label(listeCan, text="liste des étudiants", font= fonttLabel, fg='black',bg='#D2D2D2')
		resultat.grid(row=0, column=0, columnspan=3)
  
		matricule = Label(listeCan, text="Matricule",width=15, font=fonttLabel, fg="black", bg='#D2D2D2')
		matricule.grid(row=1, column=1,padx=5, pady=5)

		nom = Label(listeCan, text="nom",width=15, font=fonttLabel, fg="black", bg='#D2D2D2')
		nom.grid(row=1, column=2,padx=5, pady=5)

		prenom = Label(listeCan, text="prenom",width=15, font=fonttLabel, fg="black", bg='#D2D2D2')
		prenom.grid(row=1, column=3,padx=5, pady=5)

		option = Label(listeCan, text="Option",width=15, font=fonttLabel, fg="black", bg='#D2D2D2')
		option.grid(row=1, column=4,padx=5, pady=5)

		photo = Label(listeCan, text="photo",width=12, font=fonttLabel, fg="black", bg='#D2D2D2')
		photo.grid(row=1, column=5,padx=5, pady=5)

		status = Label(listeCan, text="aucun étudiant pour le moment", font='arial 9 bold', fg="black", bg='#D2D2D2')
		status.grid(row=2, column=0,columnspan=3)

	

		if liste:
			r=2
			for e in liste:
				photoLab= Label(listeCan, height=60)
				photoLab.grid(row= r, column=5, pady=2)

				#organisation de la photo dans la fenetre
				img=Image.open(e.photo)
				img=img.resize((85,60),Image.ANTIALIAS)
				photoLab.img=ImageTk.PhotoImage(img)
				photoLab.configure(image=photoLab.img)
   
				ma=Label(listeCan, text=e.matricule, font= fonttLabel,fg='black', bg='#D2D2D2')
				ma.grid(row= r, column=1)
   
				no=Label(listeCan, text=e.nom, font= fonttLabel,fg='black', bg='#D2D2D2')
				no.grid(row= r, column=2)

				pre=Label(listeCan, text=e.prenom, font= fonttLabel,fg='black', bg='#D2D2D2')
				pre.grid(row= r, column=3)
			
				op=Label(listeCan, text=e.option, font= fonttLabel,fg='black', bg='#D2D2D2')
				op.grid(row= r, column=4)
			

				listeCan.create_line(9,55,355,55,width=1,fill='black')

				r+=1

				status.configure(text="{} Etudiants". format(len(liste)))
				status.grid(row=r, column=0, columnspan=3, pady= 2)


def form():
	fen = Toplevel()
	fen.resizable(False, False)
	fen.geometry("420x350")
	fen.title("formulaire")

	#creation des section dans la fenetre
	cont2= Frame(fen , bg='#3C3C3C' )
	cont2.place (x=0, y=0, width=420,height=350)
	contenu=Canvas(cont2, bg="#D2D2D2")
	contenu.place(x=10, y=10, width=400,height=200)

	def parcourir():
		global imageName
		imn= fd.askopenfilename(initialdir="/home/", title="selectionner une image",
			filetypes = (("jpeg files1", "*.jpeg"),
						("jpeg files1", "*.JPEG"),
                		("jpeg files2", "*.png"),
						("jpeg files2", "*.PNG"),
						("jpeg files3", "*.JPG"),
                  		("jpeg files3","*.jpg")))

		if imn:
			imageName=imn
		if imageName:
			texte=imageName.split()
			photoEntre.configure(text= texte)

	def appartient(liste, val):
		for i in range (len(liste)):
			if liste[i].__eq__(val): 
				return 1
		return 0
	global listePersonne, imageName

	def valider():
     
		photo=imageName
		if prenomEntre.get() and nomEntre.get() and matriculeEntre.get() and optionEntre.get() and photo:
      
			insertBLOB(matriculeEntre.get(), nomEntre.get(), prenomEntre.get(), photo, optionEntre.get())
			etudiant=Etudiant(matriculeEntre.get(), nomEntre.get(), prenomEntre.get(), optionEntre.get(), photo)
			if appartient(listePersonne, etudiant):
				showerror(title="erreur", message="cette étudiant existe deja!")
		
			else:
				listePersonne.append(etudiant)
				showinfo(title="validation réussie", message="{} a bien été enregistré". format(matriculeEntre.get()))	
		
		else:
			showinfo(title="Formulaire invalide", message="veulliez renseigné tout les champs")

	def Reinitialiser():
		global listePersonne, imageName
		prenomEntre.delete(0,END)
		nomEntre.delete(0,END)
		matriculeEntre.delete(0,END)
		optionEntre.delete(0,END)
		imageName=''
		photoEntre.configure(text="selectionner une image")
	imageName, listePersonne='',[]


# forme couleur et style d'ecriture de bouton et label

	fontLabel='arial 13 bold'
	fontEntre='arial 11 bold'

	#identification des different etudiants============
 
	matricule = Label (contenu, text="Matricule:", font= fontLabel, fg='black',bg='#D2D2D2' )
	matricule.grid(row=1, column=0, sticky=E, padx=5, pady=5)

	nom = Label(contenu, text="nom:", font= fontLabel, fg='black', bg='#D2D2D2')
	nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)

	prenom = Label (contenu, text="prenom:", font= fontLabel, fg='black',bg='#D2D2D2' )
	prenom.grid(row=3, column=0, sticky=E, padx=5, pady=5)

	option = Label (contenu, text="Option:", font= fontLabel, fg='black',bg='#D2D2D2' )
	option.grid(row=4, column=0, sticky=E, padx=5, pady=5)

	photo = Label(contenu, text="votre photo:", font= fontLabel, fg='black', bg='#D2D2D2')
	photo.grid(row=5, column=0, sticky=E, padx=5, pady=5)

	validation = Label(contenu, text="Entrer vos information ici", font= fontLabel, fg='black', bg="#D2D2D2")
	validation.grid( row=0, column=0, columnspan=2)

	#creation des zone decriture
 
	matriculeEntre = Entry(contenu,font= fontLabel )
	matriculeEntre.grid(row=1, column=1, padx=5, pady=5)

	nomEntre = Entry(contenu, font= fontLabel)
	nomEntre.grid(row=2, column=1, padx=5, pady=5)

	prenomEntre = Entry (contenu, font= fontEntre)
	prenomEntre.grid(row=3, column=1, padx=5, pady=5)

	optionEntre = Entry(contenu,font= fontLabel )
	optionEntre.grid(row=4, column=1, padx=5, pady=5)

	photoEntre = Label(contenu, text="selectionner une image", font='arial 8 bold', fg='black')
	photoEntre.grid(row=5, column=1, padx=5, pady=5,sticky=W)
 
	buttonParcourir= Button (contenu,text="Parcourir", command= parcourir, fg="#FF7800", bg='white')
	buttonParcourir.grid(row=5, column=1, padx=7, pady=5,sticky=E)

	#boutton de gestion de l'enregistrement

	b1= Button (fen, text="Valider",command= valider,width=10, fg='white', bg='#5A5A5A')
	b1.place(x=160, y=230, width=90,height=25)

	b2= Button (fen, text="Reinitialiser", command= Reinitialiser,width=10, fg='white', bg='#5A5A5A')
	b2.place(x=160, y=260, width=90,height=25)
	global b3
	b3= Button (fen, text="voir la liste", command= lambda: listeInscrit(fen,listePersonne),width=10, fg='white', bg='#5A5A5A')
	b3.place(x=160, y=290, width=90,height=25)

	fen.mainloop()