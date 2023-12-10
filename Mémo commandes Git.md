# **Mémo des commandes Git**

* [Configuration initiale](#configuration-initiale)
* [Création et gestion des dépôts](#création-et-gestion-des-dépôts)
* [Gestion des modifications](#gestion-des-modifications)
* [Branche et fusion](#branche-et-fusion)
* [Travail avec des dépôts distants](#travail-avec-des-dépôts-distants)
* [Tagging et logs](#tagging-et-logs)
* [Mettre des modifications de cote pour les affecter a une nouvelle branche](#mettre-des-modifications-de-cote-pour-les-affecter-a-une-nouvelle-branche)
* [Modifier la branche après le commit](#modifier-la-branche-après-le-commit)
* [Annuler des commits avec `git revert` et `git reset`](#annuler-des-commits-avec-git-revert-et-git-reset)
* [Suivi des modifications et responsabilités](#suivi-des-modifications-et-responsabilités-avec-git-log-git-reflog-git-checkout-et-git-blame)
* [En cas de conflis lors du `git push`](#en-cas-de-conflis-lors-du-git-push)
* [Differents Workflow](#differents-workflow)

## Configuration initiale

Configurations de base pour un nouvel utilisateur Git.

* `git config --global user.name "[nom]"` : Définit le nom d'utilisateur.
* `git config --global user.email "[adresse email]"` : Définit l'adresse e-mail.

## Création et gestion des dépôts

Commandes pour initialiser et cloner des dépôts.

* `git init` : Initialise un nouveau dépôt Git.
* `git clone [url]` : Clone un dépôt existant.

## Gestion des modifications

Commandes pour vérifier l'état des fichiers et enregistrer les modifications.

* `git status` : Affiche l'état des fichiers (modifiés, non suivis, etc.).
* `git add [fichier]` : Ajoute un fichier à la zone de staging.
* `git commit -m "[message de commit]"` : Enregistre les changements.
* `git commit --amend -m "Votre nouveau message de commit"` : modifier le dernier message de commit
* `git diff` : Montre les différences de contenu non stagées.

## Branche et fusion

Commandes pour gérer les branches et les fusions.

* `git branch` : Liste les branches.
* `git branch [nom de la branche]` : Crée une nouvelle branche.
* `git checkout [nom de la branche]` : Change de branche.
* `git checkout -b [nom de la branche]` : Créer une nouvelle branche et bascule dessus immédiatement.
* `git merge [branche]` : Fusionne la branche spécifiée avec la branche actuelle.
* `git branch -d [branch]`: Supprime la branche si elle a été fusionnée.
* `git branch -D [branch]`: Force la suppression de la branche, même si elle contient des travaux non fusionnés.
* `git rebase [branche de base]` : Réapplique les commits de la branche courante sur la pointe de la branche de base.

## Travail avec des dépôts distants

Commandes pour ajouter des dépôts distants et synchroniser les données.

* `git remote add [nom court] [url]` : Ajoute un dépôt distant.
* `git fetch [nom distant]` : Récupère les modifications du dépôt distant.
* `git pull [nom distant] [branche]` : Télécharge et intègre les modifications du dépôt distant.
* `git push [nom distant] [branche]` : Publie vos modifications sur le dépôt distant.

## Tagging et logs

Commandes pour le tagging et l'affichage de l'historique des commits.

* `git log` : Affiche l'historique des commits.
* `git tag [nom du tag]` : Marque un commit avec un tag.

## Mettre des modifications de cote pour les affecter a une nouvelle branche

Si des modifications sont faites sur la branche principale (`main` ou `master`) sans avoir fait de commit, vous pouvez les mettre de côté temporairement avec `stash` :

* `git stash` : Met de côté les modifications en cours.
* `git stash list` : Liste les mises de côté.
* `git stash apply` : Réapplique les modifications mises de côté sur la branch active mais les garde en mémoire pour les répliquer autre part.
* `git stash pop` : Réapplique les modifications mises de côté sur la branch active et les supprime de la liste.

## Modifier la branche après le commit

Si vous avez modifié et commité sur la branche principale par erreur :

1. Utilisez `git log` pour trouver le hash du commit erroné.
2. Sur la branche principale, exécutez `git reset --hard HEAD^` pour supprimer le dernier commit.
3. Créez une nouvelle branche avec `git branch brancheCommit`.
4. Basculez sur cette nouvelle branche avec `git checkout brancheCommit`.
5. Appliquez le commit avec `git reset --hard [hash-du-commit]`, en utilisant les 8 premiers caractères du hash.

## Annuler des commits avec `git revert` et `git reset`

* `git revert HEAD^` : Annule le dernier commit en créant un nouveau commit d'annulation.
* `git reset` : Commande pour revenir à un état antérieur sans créer de nouveau commit. Utilisée avec différentes options :
  * `--soft` : Déplace `HEAD` mais conserve les modifications dans la zone de staging.
  * `--mixed` (par défaut) : Réinitialise la zone de staging mais garde les modifications dans le répertoire de travail.
  * `--hard` : Supprime toutes les modifications et revient à l'état du commit spécifié.

## Suivi des modifications et responsabilités avec `git log`, `git reflog`, `git checkout` et `git blame`

* `git log` : Affiche l'historique des commits de la branche courante.
* `git reflog` : Montre un journal des actions réalisées en local, y compris les commits, les changements de branches, et les resets.
* `git checkout [SHA-1]` : Permet de se positionner temporairement sur le commit identifié par le SHA-1 donné.
* `git blame [fichier]` : Montre ligne par ligne qui a modifié quoi et quand dans le fichier spécifié.

## En cas de conflis lors du `git push`

3 solutions :

  1) Pour conserver la version distante : `git checkout --theirs <nomFichier>`
  2) Pour conserver la version locale : `git checkout --ours <nomFichier>`
  3) Faire un mix des deux : Ouvrir le fichier et faire les modifications

## Differents Workflow

  1) le workflow centralisé
  2) le workflow basé sur la création de branches de fonctionnalités
  3) le workflow basé sur le tronc
  4) le workflow de duplication
  5) le GitFlow
