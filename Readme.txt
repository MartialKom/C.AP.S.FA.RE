
--------------------------- veuillez lire attentivement cette procedure de deploiement et d'utilisation de cette application------------------------------------------------------

outils requis pour l'execution de Call APp Student FAce REcognise (CAPSFARE):
- systeme d'exploitation LINUX;
- langage de programmation python; 
- Base de donnees utilisee postgreSQL (--). parametre de connexion :
																user = "shisui",
    															password = "Amenotejik@r@2",
    															host = "localhost",
    															port = "5432",
    															database = "campus

bibliotheque requisents:
- numpy ++
- matplotlib ++
- Cmake ++
- pillow ++
- opencv2 ++
- psycopg2 ++
- dlib --
- Tkinter ++
- Imutils ++

executable : GUI.py 
commande a saisir dans le terminal (se deplacer d'abord dans le dossier du projet) :python GUI.py -i images

parametre de connexion :
- login : admin ou test
- mot de passe : password pour admin et pass pour test.

          ------------------------------utilisation--------------------------

          ###  BOUTON "Ajouter un etudiant" ####

          une fois sur la page d'accueil de l'application, la premiere chose a faire est d'enregistrer un etudiant en entrant les informations requis dans le formulaire.
          NB : le nom de la photo doit etre le matricule de l'etudiant concerne.

          apres avoir enregistrer l'etudiant, vous devez deplacer la photo de l'etudiant dans le dossier images qui se trouve dans le dossier du projet; 

          ###  BOUTON "Lancer la camera"   ###

          une fois que cela est fait, vous n'avez qu'a cliquer sur lancer la camera et specifier le nom du fichier dans le quel sera enregistrer le nom des etudiants (avec l'extension ".txt") et specifier le numero de la camera source(avant de demarrer l'application, veuillez vous assurez que les cameras sont deja connecter a l'ordinateur au cas contraire vous devez fermer le programme et le re-ouvrir). par exemple si vous avez une camera brancher, le numero de la camera source sera 0 si vous avez une deuxieme camera, le numero sera 1 ainsi de suite. apres avoir donc saisir le numero de la camera source, vous n'avez qu'a cliquer sur le bouton submit et la camera specifie s'activera. pour fermer la camera veulliez appuyer la touche "q" du clavier.

          ###  BOUTON Prendre une Video  ###

          lorsque vous cliquer sur prendre une video, vous devez entrer le nom sous lequel vous souhaitez enregistrer la video(avec l'extension ".avi" ou ".mp4") et la suite est identique au precedent.

          ###  BOUTON "Imprimer les fiches"  ###

          pour imprimer une fiche de presence, vous devez choisir le fichier a imprimer et cliquer sur le bouton imprimer

          ###  BOUTON "visualiser les presences"   ###

          ce bouton ouvre une fenetre dans la quelle vous pouvez visualiser les listes de presence et analyser une video.