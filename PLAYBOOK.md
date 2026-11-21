# PLAYBOOK

Mon aide-mémoire pour démarrer un projet proprement.

## Environnement
- Je travaille dans `~/dev` (Linux), pas dans `/mnt/c` : pour plus de rapidité, pour éviter des erreurs de droits d'accès (pas de conservation des droits d'accès `chmod` ignoré) (`/mnt/c` est le couloir qui mène de windows à Linux(`~/dev`) et au milieu duquel il y a une porte qui fait des contrôles à chaque fois qu'on quitte de windows à linux et vice versa)
- Docker  : corriger l'erreur « permission denied » : il faut que je me rajoute à la liste des membres du groupe docker avec `sudo -aG docker $USER` puis fermer ma session actuelle avec `wsl shutdown` dans powershell puis rouvrir ubuntu sinon quand je ferai le `docker run hello-world` on m'affichera "permission denied" car cette commande en l'exécutant, linux me réfusait l'accès au fichier `/var/run/docker.sock`.

## Git et GitHub
- Git a besoin de mon nom et e-mail pour : afin de savoir qui est à l'origine de chaque commit émis (traçabilité) -> `git config --global user.name leslienguiamba6-sudo` `git config --global user.email leslienguiamba6@gmail.com` `git config --global init.defaultBranch main` `git config --global core.autocrlf input`
- Je clone en SSH parce que : déjà pour plus de sécurité mais plus précisement parce qu'avec ssh la clé privée utilisée reste sur ma machine et je dois juste dévérouiller cette clé par le billet d'une phrase secrète qui par la suite prouvera à git que je l'ai en générant une signature alors qu'avec https, on utilise un jeton qui reste sur ma machine et s'il est volé, il donne accès à mon compte car il n'est pas protégé pas une phrase secrète
- Avant de répondre yes à SSH : il faut se rassurer que non seulement le nom de domaine affiché est bien celui de git (car tout faute peut entrainer un attaque nommée typosquatting) mais aussi que l'empreinte est bien celui qui apparait sur le site officiel de github sinon on peut être subir une attque du type man in the middle.

## SSH
-  `ssh-keygen -t ed25519 -C "felicie-wsl-ubuntu"` : création des paires de clé
- `ls -l ~/.ssh` : vérification des droits d'accès aux fichiers .ssh
- `cat ~/.ssh/id_ed25519.pub` : récupération de la clé public pour le dépôt git
- `ssh -T git@github.com` : ajout du serveur github à la liste des hôtes de ssh
- `ssh-keygen -R githuh.com` : suppression du faux serveur à la liste des hôtes ssh
- `ssh-keygen -p -f ~/.ssh/id_ed25519` : création d'une nouvelle phrase secrète