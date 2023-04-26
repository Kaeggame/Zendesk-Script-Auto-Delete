# Zendesk Ticket Archiver

This script is designed to search for and delete Zendesk tickets that are closed and have had no activity for 5 years.

## Contents

The project consists of the following files:

1. **Script.py** : The main file that searches and displays tickets based on different criteria.
2. **Auth.py** : The file that handles authentication and connection to the Zendesk API.
3. **Test.py** : The file to test the various functionalities of the script.
4. **Time.py** : The file that calculates the current date and the date 5 years ago.

## Prerequisites

To use this script, you need to install the `zenpy` library. You can install it using the following command:

pip install zenpy


## Configuration

1. In the `Auth.py` file, replace the values of the `email`, `token`, and `subdomain` variables with your own credentials to access your Zendesk account.
2. Modify the value of `proactive_ratelimit` in the `Auth.py` file with your Zendesk account's API call limit.

## Usage

1. Run `Script.py` to search and display tickets that are closed or solved and have had no activity for 5 years.
2. Run `Test.py` to test various functionalities of the script, such as searching for tickets by assignment and tags.
3. To delete tickets, uncomment the line `#zenpy.tickets.delete(ticket)` in `Script.py` or `Test.py`.

## Warning

Ticket deletion is irreversible. Please make sure to thoroughly check the tickets before deleting them.

---

# Zendesk Ticket Archiver Doc FR

Ce script permet de rechercher et supprimer les tickets de Zendesk qui sont fermés et sans activité depuis 5 ans.

## Contenu

Le projet est constitué des fichiers suivants :

1. **Script.py** : Le fichier principal qui recherche et affiche les tickets en fonction de différents critères.
2. **Auth.py** : Le fichier qui gère l'authentification et la connexion à l'API Zendesk.
3. **Test.py** : Le fichier pour tester les différentes fonctionnalités du script.
4. **Time.py** : Le fichier qui calcule la date actuelle et la date il y a 5 ans.

## Prérequis

Pour utiliser ce script, vous devez installer la bibliothèque `zenpy`. Vous pouvez l'installer en utilisant la commande suivante :

pip install zenpy

## Configuration

1. Dans le fichier `Auth.py`, remplacez les valeurs des variables `email`, `token` et `subdomain` par vos propres informations d'identification pour accéder à votre compte Zendesk.
2. Modifiez la valeur de `proactive_ratelimit` dans le fichier `Auth.py` avec la limite d'appels d'API de votre compte Zendesk.

## Utilisation

1. Exécutez `Script.py` pour rechercher et afficher les tickets qui sont fermés ou résolus et sans activité depuis 5 ans.
2. Exécutez `Test.py` pour tester les différentes fonctionnalités du script, telles que la recherche de tickets par assignation et par tags.
3. Pour supprimer les tickets, décommentez la ligne `#zenpy.tickets.delete(ticket)` dans `Script.py` ou `Test.py`.

## Avertissement

La suppression des tickets est irréversible. Assurez-vous de bien vérifier les tickets avant de les supprimer.
