#Jeu de type morpion : cas d'une grille carrée à neuf cases

#Le joueur commence à jouer en premier, l'ordinateur joue ensuite

#coding: utf-8

import numpy #import de la librairie numpy
M=numpy.array([["a","a","a"],["a","a","a"],["a","a","a"]]) #tableau ou matrice de caratères représentant le jeu en taille 3 initialisée avec des caractères lettre a
N=numpy.array([[1,1,1],[1,1,1],[1,1,1]]) #matrice auxiliaire initiale ne comportant que des valeurs 1 en taille 3 correspondant aux choix du joueur
T=numpy.array([[1,1,1],[1,1,1],[1,1,1]]) #matrice auxiliaire initiale ne comportant que des valeurs 1 en taille 3 correspondant aux choix de l'ordinateur
#D�but de la partie du joueur face à l'ordinateur :
y=0 #variable auxiliaire y initialisée à 0
while len(M[M=="a"])>0 and y==0: #test au fur et à mesure pour savoir si la partie peut encore avancer
 #Choix du joueur :
 t=0 #variable auxiliaire t initialisée à 0
 i1=int(input("Entrer le num�ro de la ligne (0, 1 ou 2) : ")) #choix de la ligne i1 par le joueur
 j1=int(input("Entrer le num�ro de la colonne (0, 1 ou 2) : ")) #choix de la colonne j1 par le joueur
 if N[i1,j1]==0 or T[i1,j1]==0: #test pour déterminer si la cellule (i1,j1) de la matrice N contient la valeur 0 ou si la cellule (i1,j1) de la matrice T contient la valeur 0
  print("Choix du joueur impossible : rejouer") #retour à l'écran d'un choix de jeu impossible
  t=1
 if t==0:
  M[i1,j1]="X" #écriture de la lettre X à l'intersection de la ligne i1 et de la colonne j1 représentant le choix du joueur
  N[i1,j1]=0 #�criture de la valeur 0 au même emplacement dans la matrice initiale
 print(M) #retour à l'écran de l'état d'avancement du jeu suite au choix du joueur
 #Choix de l'ordinateur :
 if t==0:
  for i2 in [0,1,2]:
   for j2 in [0,1,2]:
    if t==0 and M[i2,j2]=="a":
     S=numpy.copy(T) #copie de la matrice T dans une nouvelle matrice S : contrainte imposée par le langage sinon une erreur est générée
     S[i2,j2]=0 #�criture de la valeur 0 dans la cellule (i2,j2) de la matrice S
     if sum(S[0,:])==0 or sum(S[1,:])==0 or sum(S[2,:])==0  or sum(S[:,0])==0 or sum(S[:,1])==0 or sum(S[:,2])==0 or S[0,0]+S[1,1]+S[2,2]==0 or S[0,2]+S[1,1]+S[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la première diagonale et la deuxième diagonale de la matrice S est égale à 0
      M[i2,j2]="O" #si tel est le cas l'ordinateur doit placer la lettre O dans la cellule (i2,j2) pour gagner la partie
      T[i2,j2]=0
      t=1 #variable auxiliaire t réinitialisée à 1 : les boucles Pour ne contiennent plus d'instructions
 if t==0:
  for i2 in [0,1,2]: #la variable i2 parcourt les valeurs 0, 1 et 2 autrement dit toutes les lignes de la matrice
   for j2 in [0,1,2]: #la variable j2 parcourt les valeurs 0, 1 et 2 autrement dit toutes les colonnes de la matrice
    if t==0 and M[i2,j2]=="a": #test pour déterminer si la cellule (i2,j2) contient la lettre a
     P=numpy.copy(N) #copie de la matrice N dans une nouvelle matrice P : contrainte imposée par le langage sinon une erreur est générée
     P[i2,j2]=0 #�criture de la valeur 0 dans la cellule (i2,j2) de la matrice P
     if sum(P[0,:])==0 or sum(P[1,:])==0 or sum(P[2,:])==0  or sum(P[:,0])==0 or sum(P[:,1])==0 or sum(P[:,2])==0 or P[0,0]+P[1,1]+P[2,2]==0 or P[0,2]+P[1,1]+P[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la première diagonale et la deuxième diagonale de la matrice P est égale à 0
      M[i2,j2]="O" #si tel est le cas l'ordinateur doit placer la lettre O dans la cellule (i2,j2) pour essayer d'empêcher le joueur de gagner
      T[i2,j2]=0
      t=1 #variable auxiliaire t réinitialisée à 1 : les boucles Pour ne contiennent plus d'instructions
 if t==0 and M[1,1]=="a": #si le joueur n'est pas en mesure de gagner et le joueur n'a pas joué au centre, le choix de l'ordinateur n'est pas contraint, l'ordinateur joue au centre
     M[1,1]="O" #écriture de la lettre O dans la cellule (1,1)
     T[1,1]=0
     t=1 #variable auxiliaire t réinitialisée à 1 : l'étape suivante est omise
 if t==0:
  for i2 in [0,1,2]:
   for j2 in [0,1,2]:
    if t==0 and M[i2,j2]=="a":
     M[i2,j2]="O"
     T[i2,j2]=0
     t=1
 print("Jeu de l'ordinateur :")
 print(M) #retour à l'écran de l'état d'avancement du jeu suite au choix de l'ordinateur
 if sum(N[0,:])==0 or sum(N[1,:])==0 or sum(N[2,:])==0  or sum(N[:,0])==0 or sum(N[:,1])==0 or sum(N[:,2])==0 or N[0,0]+N[1,1]+N[2,2]==0 or N[0,2]+N[1,1]+N[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la premiére diagonale et la deuxième diagonale de la matrice N est égale à 0
  print("Vous avez gagné")
  y=1
 if sum(T[0,:])==0 or sum(T[1,:])==0 or sum(T[2,:])==0  or sum(T[:,0])==0 or sum(T[:,1])==0 or sum(T[:,2])==0 or T[0,0]+T[1,1]+T[2,2]==0 or T[0,2]+T[1,1]+T[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la premiére diagonale et la deuxième diagonale de la matrice T est égale à 0
  print("Vous avez perdu")
  y=1
 if len(M[M=="a"])==0:
  print("Pas de perdant ni de gagnant")
  y=1

#pour lancer le programme en mode console : exec(open("jeu.py").read())

#émulateur python en ligne : https://www.onlinegdb.com/online_python_interpreter
