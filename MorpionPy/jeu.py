# Jeu du morpion
# Le joueur commence a jouer en premier, l'ordinateur joue ensuite

# Import des bibliotheques necessaires au programme
import numpy
from game import *

def play():
 #Choix du joueur :
 i1=int(input("Entrer le numéro de la ligne (0, 1 ou 2) : ")) # choix de la ligne i1 par le joueur
 j1=int(input("Entrer le numéro de la colonne (0, 1 ou 2) : ")) # choix de la colonne j1 par le joueur
 if N[i1,j1]==0 or T[i1,j1]==0: # test pour déterminer si la cellule (i1,j1) de la matrice N contient la valeur 0 ou si la cellule (i1,j1) de la matrice T contient la valeur 0
  print("Choix du joueur impossible : rejouer") # retour à l'écran d'un choix de jeu impossible
  return;

 M[i1,j1]="X" # écriture de la lettre X à l'intersection de la ligne i1 et de la colonne j1 représentant le choix du joueur
 N[i1,j1]=0 # écriture de la valeur 0 au même emplacement dans la matrice initiale

 # Choix de l'ordinateur :
 for i2 in [0,1,2]:
  for j2 in [0,1,2]:
   if M[i2,j2]=="a":
    S=numpy.copy(T) #copie de la matrice T dans une nouvelle matrice S : contrainte imposée par le langage sinon une erreur est générée
    S[i2,j2]=0 #�criture de la valeur 0 dans la cellule (i2,j2) de la matrice S
    if sum(S[0,:])==0 or sum(S[1,:])==0 or sum(S[2,:])==0  or sum(S[:,0])==0 or sum(S[:,1])==0 or sum(S[:,2])==0 or S[0,0]+S[1,1]+S[2,2]==0 or S[0,2]+S[1,1]+S[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la première diagonale et la deuxième diagonale de la matrice S est égale à 0
     M[i2,j2]="O" #si tel est le cas l'ordinateur doit placer la lettre O dans la cellule (i2,j2) pour gagner la partie
     T[i2,j2]=0
     return; #variable auxiliaire t réinitialisée à 1 : les boucles Pour ne contiennent plus d'instructions

 for i2 in [0,1,2]: #la variable i2 parcourt les valeurs 0, 1 et 2 autrement dit toutes les lignes de la matrice
  for j2 in [0,1,2]: #la variable j2 parcourt les valeurs 0, 1 et 2 autrement dit toutes les colonnes de la matrice
   if M[i2,j2]=="a": #test pour déterminer si la cellule (i2,j2) contient la lettre a
    P=numpy.copy(N) #copie de la matrice N dans une nouvelle matrice P : contrainte imposée par le langage sinon une erreur est générée
    P[i2,j2]=0 #�criture de la valeur 0 dans la cellule (i2,j2) de la matrice P
    if sum(P[0,:])==0 or sum(P[1,:])==0 or sum(P[2,:])==0  or sum(P[:,0])==0 or sum(P[:,1])==0 or sum(P[:,2])==0 or P[0,0]+P[1,1]+P[2,2]==0 or P[0,2]+P[1,1]+P[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la première diagonale et la deuxième diagonale de la matrice P est égale à 0
     M[i2,j2]="O" #si tel est le cas l'ordinateur doit placer la lettre O dans la cellule (i2,j2) pour essayer d'empêcher le joueur de gagner
     T[i2,j2]=0
     return; #variable auxiliaire t réinitialisée à 1 : les boucles Pour ne contiennent plus d'instructions

 if M[1,1]=="a": #si le joueur n'est pas en mesure de gagner et le joueur n'a pas joué au centre, le choix de l'ordinateur n'est pas contraint, l'ordinateur joue au centre
  M[1,1]="O" #écriture de la lettre O dans la cellule (1,1)
  T[1,1]=0
  return; #variable auxiliaire t réinitialisée à 1 : l'étape suivante est omise

 for i2 in [0,1,2]:
  for j2 in [0,1,2]:
   if M[i2,j2]=="a":
    M[i2,j2]="O"
    T[i2,j2]=0
    return;

# tableau ou matrice de caratères représentant le jeu en taille 3 initialisée avec des caractères lettre a
M=numpy.array([["a","a","a"],["a","a","a"],["a","a","a"]])

# matrice auxiliaire initiale ne comportant que des valeurs 1 en taille 3 correspondant aux choix du joueur
N=numpy.array([[1,1,1],[1,1,1],[1,1,1]])

# matrice auxiliaire initiale ne comportant que des valeurs 1 en taille 3 correspondant aux choix de l'ordinateur
T=numpy.array([[1,1,1],[1,1,1],[1,1,1]])

# Début de la partie du joueur face à l'ordinateur :

while len(M[M=="a"])>0: #test au fur et à mesure pour savoir si la partie peut encore avancer

 play()

 print("") # retour à la ligne pour ahérer l'affichage
 print(M) #retour à l'écran de l'état d'avancement du jeu suite au choix de l'ordinateur
 print("") # retour à la ligne pour ahérer l'affichage

 if sum(N[0,:])==0 or sum(N[1,:])==0 or sum(N[2,:])==0  or sum(N[:,0])==0 or sum(N[:,1])==0 or sum(N[:,2])==0 or N[0,0]+N[1,1]+N[2,2]==0 or N[0,2]+N[1,1]+N[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la premiére diagonale et la deuxième diagonale de la matrice N est égale à 0
  print("Vous avez gagné")
  break;
 if sum(T[0,:])==0 or sum(T[1,:])==0 or sum(T[2,:])==0  or sum(T[:,0])==0 or sum(T[:,1])==0 or sum(T[:,2])==0 or T[0,0]+T[1,1]+T[2,2]==0 or T[0,2]+T[1,1]+T[2,0]==0: #test pour déterminer si la somme sur chacune des lignes 0, 1 et 2, chacune des colonnes 0, 1 et 2, la premiére diagonale et la deuxième diagonale de la matrice T est égale à 0
  print("Vous avez perdu")
  break;
 if len(M[M=="a"])==0:
  print("Pas de perdant ni de gagnant")
  break;

#pour lancer le programme en mode console : exec(open("jeu.py").read())

#émulateur python en ligne : https://www.onlinegdb.com/online_python_interpreter
