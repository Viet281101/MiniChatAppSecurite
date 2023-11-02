
# Projet Déveloper Chatbox App Sécurité -- Introduction à la Sécurité

La mise en place de fonctionnalités d'un mini-tchat sécurisé.

Viet NGUYEN -- L3B -- 20006303


L’Objectif est de créer une application de chat de base avec une interface simple utilisant la bibliothèque ‘tkinter’ et un serveur utilisant ‘socket’ avec les idées pour développer des systèmes de sécurité supplémentaires suivants:

1)  Crypter les messages avant de les envoyer:
	- Utilisez des algorithmes de chiffrement tels que AES ou RSA pour chiffrer les messages avant de les envoyer du client au serveur et les décrypter lors de la réception des messages.
	- Il doit y avoir un mécanisme pour échanger en toute sécurité les clés de chiffrement entre le client et le serveur.


J'utilise un projet [SmallChatAppPython](https://github.com/Viet281101/SmallChatAppPython/tree/main) sur mon GitHub avec 2 fichiers serveur.py et client.py disponibles.


2)  Cryptage de connexion (optional):
	- Utilisez SSL/TLS pour crypter la connexion entre le client et le serveur. Cela garanti que les messages ne sont pas capturés et lus en ligne.

Sur terminal:
```
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```
Il va créer 2 fichier **key.pem** et **cert.pem** puis importer openssl sur 2 fichier serveur.py et client.py


3) Authentification d’utilisateur (optional):
	- Ajoutez un système de connexion qui permet l’authentification des utilisateurs. Cela fournit une couche de sécurité supplémentaire et permet d’empecher d’autres utilisateurs malveillants.


4) Stockage des messages (optional):
	- Archiver des messages, assurer qu’ils sont cryptés avant de les enregistrer dans la base de données.

