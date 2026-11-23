# PLAYBOOK

Mon aide-mémoire pour démarrer un projet proprement.

> Il faut utiliser comme terminal Ubuntu et non Gitbash car le Gitbash est dans Windows.

## Environnement
- Je travaille dans `~/dev` (Linux), pas dans `/mnt/c` : pour plus de rapidité, pour éviter des erreurs de droits d'accès (pas de conservation des droits d'accès `chmod` ignoré) (`/mnt/c` est le couloir qui mène de Windows à Linux(`~/dev`) et au milieu duquel il y a une porte qui fait des contrôles à chaque fois qu'on quitte de Windows à Linux et vice versa)
- Docker  : corriger l'erreur « permission denied » : il faut que je me rajoute à la liste des membres du groupe docker avec `sudo usermod -aG docker $USER` puis fermer ma session actuelle avec `wsl --shutdown` dans powershell puis rouvrir Ubuntu sinon quand je ferai le `docker run hello-world` on m'affichera "permission denied" car cette commande en l'exécutant, Linux me refusait l'accès au fichier `/var/run/docker.sock`.

## Git et GitHub
- Git a besoin de mon nom et e-mail pour : afin de savoir qui est à l'origine de chaque commit émis (traçabilité) -> `git config --global user.name leslienguiamba6-sudo` `git config --global user.email leslienguiamba6@gmail.com` `git config --global init.defaultBranch main` `git config --global core.autocrlf input`
- Je clone en SSH parce que : déjà pour plus de sécurité mais plus précisement parce qu'avec ssh la clé privée utilisée reste sur ma machine et je dois juste déverrouiller cette clé grâce à une phrase secrète qui par la suite prouvera à git que je l'ai en générant une signature alors qu'avec https, on utilise un jeton qui reste sur ma machine et s'il est volé, il donne accès à mon compte car il n'est pas protégé par une phrase secrète
- Avant de répondre yes à SSH : il faut se rassurer que non seulement le nom de domaine affiché est bien celui de git (car tout faute peut entrainer un attaque appelée typosquatting) mais aussi que l'empreinte est bien celle qui apparait sur le site officiel de github sinon on peut subir une attaque du type man in the middle.

## SSH
- `ssh-keygen -t ed25519 -C "felicie-wsl-ubuntu"` : création des paires de clé
- `ls -l ~/.ssh` : vérification des droits d'accès aux fichiers .ssh
- `cat ~/.ssh/id_ed25519.pub` : récupération de la clé public pour le dépôt git ; la clé publique se colle dans GitHub, Settings, SSH and GPG keys.
- `ssh -T git@github.com` : teste la connexion à GitHub ; à la première fois, vérifier l’empreinte avant de répondre yes
- `ssh-keygen -R githuh.com` : suppression du faux serveur à la liste des hôtes ssh
- `ssh-keygen -p -f ~/.ssh/id_ed25519` : création d'une nouvelle phrase secrète


## Python
- Au début de chaque projet Python, je crée un environnement virtuel dans le dossier du projet : `python3 -m venv .venv`, puis je l'active avec `source .venv/bin/activate` (le prompt affiche `(.venv)`).
- Je ne lance jamais `pip install` sans `(.venv)` actif, sinon le paquet va dans le système (dans ce cas, les projets se mélangent, je risque de perturber les outils du système, et mon requirements-dev.txt n’est plus fiable.).
- requirements.txt contient ce dont l’application a besoin pour tourner (fastapi, uvicorn) ; requirements-dev.txt commence par `-r requirements.txt` et ajoute les outils de développement (pytest, httpx). `pip freeze` liste tout ce qui est installé, donc je trie les paquets à la main entre les deux fichiers.
- `.venv` n'est pas dans Git (le `.gitignore` Python l'exclut) : il se recrée à partir de `requirements-dev.txt`. 

> Dans mon cas, `python3 -m venv` a échoué avec "ensurepip is not available", j’ai dû d'abord installer le module qui permet de créer des environnements virtuels avec `sudo apt install python3-venv`.

> Il ne faut pas confondre `apt` qui la commande qui permet d'installer des logiciel dans le système grâce à sudo et `pip` qui est la commande qui permt d'installer des paquets python dans l'environnement virtuel (Venv)