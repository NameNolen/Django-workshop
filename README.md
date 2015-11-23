# Django-workshop
This project is for learning Django.
## 1. Do the tutorial in Django
Build a site following the steps in Django's document.
## 2. Collaborate with other through github.com
Useful Github command:
Generate ssh key:
> ssh-keygen -C 'your@email.address' -t rsa
Put the obtained id_rsa.pub into your github setting.
Verify the key:
> ssh -T git@github.com
Clone this object:
>git clone https://github.com/NameNolen/Django-workshop.git
Then,
>git remote add origin https://github.com/NameNolen/Django-workshop.git
If you get this error:
>fatal: remote origin already exists
run:
>git remote rm origin
then re-run the command before.
Before any changes, should obtain the newest version:
>git pull origin master
Upload change:
>git add .
>
>git rm [file]
>
>git rm [dir] -r
Then
>git commit
This will rise a nano file, just uncomment the line and modify it.
At last:
>git push origin master
