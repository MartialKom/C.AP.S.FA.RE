
--------------------------- veuillez lire attentivement cette procedure de deploiement et d'utilisation de cette application------------------------------------------------------

outils requis pour l'execution de Call APp Student FAce REcognise (CAPSFARE):
- systeme d'exploitation LINUX;
- langage de programmation python; 


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
commande a saisir dans le terminal (se deplacer d'abord dans le dossier du projet) :python GUI.py -i image

parametre de connexion :
- login : admin ou test
- mot de passe : password pour admin et pass pour test.

          ------------------------------utilisation--------------------------

          ###  BOUTON "Lancer la camera"   ###

          une fois que cela est fait, vous n'avez qu'a cliquer sur lancer la camera et specifier le nom du fichier dans le quel sera enregistrer le nom des etudiants (avec l'extension ".txt") et specifier le numero de la camera source(avant de demarrer l'application, veuillez vous assurez que les cameras sont deja connectés a l'ordinateur au cas contraire vous devez fermer le programme et le re-ouvrir). par exemple si vous avez une camera brancher, le numero de la camera source sera 0 si vous avez une deuxieme camera, le numero sera 1 ainsi de suite. apres avoir donc saisi le numero de la camera source, vous n'avez qu'a cliquer sur le bouton submit et la camera specifie s'activera (cela peut prendre quelques temps). pour fermer la camera veulliez appuyer la touche "q" du clavier.

          ###  BOUTON Prendre une Video  ###

          lorsque vous cliquer sur prendre une video, vous devez entrer le nom sous lequel vous souhaitez enregistrer la video(avec l'extension ".avi" ou ".mp4") et la suite est identique au precedent.

        
