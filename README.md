
# Bienvenue dans le jeu de Nim version Syldon

![Illustration](https://members.loria.fr/MDuflot/files/med/doc/Nim/nim.jpg)
Bien le bonjour/bonsoir.

Le jeu de Nim que j'ai essayé de coder (le plus simplement possible) n'est pas bien compliqué. Il est écrit en Python et sans inclusion de bibliothèques graphiques. Pour dire que tout le programme s'affichera dans votre terminal.

## Principe
Le principe est simple :

Au départ, il y a un nombre aléatoire de "bâtonnets" compris entre 20 et 30. Le jeu consiste à enlever 1, 2, ou 3 bâtonnets à chaque tour. Le vainqueur est celui qui peut jouer en dernier. Donc en gros, tu gagnes si c'est toi qui retire le(s) dernier(s) bâtonnet(s). Tu peux affronter soit l'ordinateur soit un ami. Oui, il vous faudra être précis si vous voulez gagner 😌.

## Comment Jouer ?
1. Créez un dossier sur votre PC pour le jeu, nommez-le à votre guise.
2. Téléchargez manuellement chacun des 9 fichiers que vous voyez et placez-les dans le dossier créé précédemment.
   *Ou*
   Depuis votre terminal, naviguez jusqu'au dossier créé avec la commande `cd`. Ensuite, tapez la commande suivante :

   ```bash
   git clone https://github.com/Finosyval/Mini_Syldon_Python_Game.git
   ```

3. Pour démarrer le programme, exécutez le fichier `main.py`.

## Quelques remarques
- Tous les `#appel de fonction` situés à la fin des fichiers servaient de tests du code atomique concerné.
- Ne vous inquiétez pas pour le dossier "Pycache" qui apparaît et se remplit à mesure que le programme est exécuté.