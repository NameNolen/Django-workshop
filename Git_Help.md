Generate ssh key:

    ssh-keygen -C 'your@email.address' -t rsa    

Put the obtained id_rsa.pub into your github setting.

Verify the key:

    ssh -T git@github.com    

Clone this object:

    git clone https://github.com/NameNolen/Django-workshop.git    

Then,

    git remote add origin https://github.com/NameNolen/Django-workshop.git    

If you get this error:

> fatal: remote origin already exists    

run:

    git remote rm origin    

then re-run the command before.

Before any changes, should obtain the newest version:

    git pull origin master    

Check the git status:

    git status    

Upload change:

    git add .    

    git rm [file]    

    git rm [dir] -r    

Then

    git commit    

This will rise a nano file, just uncomment the line and modify it.

At last:

    git push origin master    

If you want exclude some file for git, put them in _.gitignore_. For example, we don't want check _.pyc_ for commit, we put *.pyc into .gitignore. Before it works, you should rm *pyc in the repo.
