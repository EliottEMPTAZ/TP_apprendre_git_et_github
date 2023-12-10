# Simulation de Collaboration avec Git et GitHub

## Objectif du TP

Ce TP a pour but de simuler un environnement de travail collaboratif utilisant Git et GitHub. Nous apprendrons à gérer un dépôt Git, à travailler avec des branches, et à résoudre des conflits de fusion. L'accent est mis sur l'utilisation pratique de Git et GitHub en équipe, plutôt que sur la programmation.

Le TP se réalise en binôme.

## Mise en Situation

Vous formez une équipe de deux développeurs travaillant sur un projet Python simple, comprenant deux fichiers.
functions.py contient des fonctions mathématiques de base, tandis que main.py les utilise pour calculer et afficher des graphiques.

## Rendu

À la fin du TP est à rendre un rapport montrant les commandes utilisées pour chaque tâche et le lien du dépôt github.

## Prérequis

- Installation des outils suivants :
  - [Visual Studio Code](https://code.visualstudio.com/download)
  - [Git](https://git-scm.com/book/fr/v2/Démarrage-rapide-Installation-de-Git)

- Création d'un compte GitHub : [s'inscrire ici](https://github.com/join)

- Création et association d'une clé SSH à Git et GitHub : [instructions ici](https://docs.github.com/fr/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#)

## Configuration de Git

Exécutez les commandes suivantes dans un terminal pour configurer Git :

```bash
git config --global user.name "[Nom d'utilisateur GitHub]"
git config --global user.email [Email GitHub]
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global core.editor notepad++
git config --global merge.tool vimdiff
```

## Mise en Place du Projet

Chaque groupe doit créer une copie personnelle du dépôt. Suivez ces étapes :

### Fork du Projet

À réaliser une fois par groupe :

Allez sur [la page GitHub du projet](https://github.com/EliottEMPTAZ/TP_apprendre_git_et_github).

Cliquez sur Fork en haut à droite pour copier le dépôt dans votre espace personnel.

### Clonage du Fork

Après le fork, clonez le dépôt pour travailler localement :

1. Créez un dossier de travail sur votre ordinateur.

2. Ouvrez un terminal.

3. Naviguez jusqu'à votre dossier de travail.

    ```text
    cd [lien du dossier]
    ```

4. Clonez le dépôt

    ```text
    git clone [url du dépôt distant]
    ```

## Travail à Réaliser

**Aide** : Lorsque vous avez un doute sur ce que vous êtes en train de faire ou simplement pour vérifier où vous en êtes utilisé la commande

```text
git status
```

### Tâche 1

Modifiez chacun un fichier différent, puis enregistrez vos modifications localement et sur GitHub. Après cela, mettez à jour votre dossier de travail avec la dernière version en ligne de chaque fichier.

**Personnage 1** : Ajoutez la définition de la fonction `calculate_values`

Exemple :

```Python
def calculate_values(function, x_values):
    """
    Calcule et retourne les valeurs obtenues en appliquant une fonction donnée à chaque élément d'une liste d'entrée.

    Args:
        function : Une fonction qui prend un seul argument et renvoie une valeur. 

        x_values : Une liste de valeurs sur lesquelles la fonction 'function' est appliquée.

    Returns:
        List: Une liste contenant les résultats de l'application de 'function' à chaque élément de 'x_values'.
    """
    return [function(x) for x in x_values]

```

**Personnage 2** : Ajoutez un commentaire dans main.py

Exemple :

```Python
from functions import * #Importe les fonctions crée dans le fichier `function.py``

```

**Procédure**

Ajouter les fichiers modifiés à votre futur commit

```text
git add [nom_fichier]
```

Ajoutez vos modifications dans le dépôt local

```text
git commit -m "[msg_du_commit]"
```

Le `-m` permet d'ajouter un msg à votre commit, il est obligatoire. Le message doit être le plus clair possible exemple : "Ajout de la définition de la fonction calculate_values"

Verifier où vous en êtes

```text
git status
```

Puis, si tout est prêt poussez vos modifications dans le dépôt distant

```text
git push
```

une fois que vous avez tous les deux terminer le but est de retrouver le travail de l'autre en local sur son ordinateur. pour cela faite

```text
git pull
```

À ce stade vous devriez chacun avoir sur votre ordinateur les modifications réalisées par votre binôme.

Pour les prochaines Tâches vous n'aurez plus les commandes écrites, référez-vous au [mémo commandes git](Mémo%20commandes%20Git.md)

### Tâche 2

L'objectif de cette Tâche est de vous familiariser avec les branches dans Git. Vous allez chacun créer une nouvelle branche, y ajouter une fonctionnalité spécifique, puis pousser vos modifications sur cette branche.

1. Créez une branche.

2. Basculez sur la nouvelle branche.

3. **Personnage 1 :** Ajoutez dans le fichier functions.py une fonction square() qui calcule le carré d'un nombre.\
**Personnage 2:** Ajoutez dans le fichier functions.py une fonction cube() qui calcule le cube d'un nombre.

4. Enregistrez dans le dépôt local.

5. Enregistrez dans le dépôt distant.

Après avoir tous les deux réalisé votre branche et vos modifications, vérifiez sur GitHub que les branches sont bien créées avec le nouveau contenu.

### Tâche 3

Après avoir ajouté vos nouvelles fonctionnalités chacun de votre côté, décidez de les tester ensemble sur une nouvelle branche fonctionnalités (déjà existante).

1. Chacun de votre côté, placez-vous sur la branche fonctionnalités.

2. Fusionnez votre branche créée à la Tâche 2 sur la nouvelle branche fonctionnalités. /!\ faite le chaqu'un 

3. Testez les nouvelles fonctions en lançant le script main.py.

### Tâche 4

Maintenant que les tests sur la branche fonctionnalités sont concluants, faites un merge sur la branche principale.

### Tâche 5

Votre premier conflit : Ici, le but va être de modifier une même ligne dans le même fichier pour créer un conflit.

1. Renommez tous les deux la fonction square.\
**Personnage 1 :** Renommez en carreNombre.\
**Personnage 2:** Renommez en carre.

2. Ajoutez vos modifications sur le dépôt distant, chacun de votre côté (n'oubliez pas les étapes intermédiaires non citées).

3. Le deuxième à utiliser la commande git push devrait obtenir un conflit. Résolvez le conflit en gardant la deuxième modification (carre).

### Tâche 6

Apprenez à utiliser git stash pour sauvegarder des modifications temporaires.

1. Placez-vous sur la branche principale.

2. Chacun de votre côté, créez une fonction mathématique (peu importe laquelle).

3. Une fois la fonction finie, rappelez-vous que vous ne vous n'êtes pas placés sur la bonne branche pour créer la fonctionnalité. Utilisez git stash pour mettre vos modifications de côté.

### Tâche 7

Apprenez à utiliser git rebase.

Dans l'étape précédente, vous avez effectué des modifications directement sur la branche principale. Or, vous voulez modifier la branche fonctionnalité. Il faut d'abord que cette branche soit à jour par rapport à la branche principale.

mettre a jour la branche fonctionalité

### Tâche 8

Répliquez vos modifications sur la branche fonctionalité

1. Placez-vous sur la branche fonctionnalités.

2. Répliquez vos modifications sur cette branche.

3. Enregistrez vos modifications dans le dépôt local, puis distant.

## Conclusion

Félicitations ! Vous êtes arrivés au bout de ce TP sur la collaboration avec Git et GitHub.

J'espère que ce TP vous a donné une base solide pour utiliser Git et GitHub dans vos futurs projets de groupe à l'école.
