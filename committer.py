from datetime import date
import os
import random as rd


def MakeCommits(dirs):
    for directory in dirs:
        os.chdir(directory)
        os.system("git init")
        with open("README.md", "w") as f:
            f.write(str(' '))
        os.system('git add README.md')
        os.system(f'git commit -m "piece" --date="' + str(date.today()) + 'T00:00:00+0300"')
        os.chdir("..")


def PushAll(dirs):
    for d in dirs:
        os.chdir(d)
        os.system("git remote add origin " + dirs[d])
        os.system("git push -u origin master")
        os.chdir("..")


def commit(dirs, dates):
    MakeCommits(dirs)
    PushAll(dirs)

if __name__ == "__main__":
    main({'github_auto_commiter':'https://github.com/alexbod/github-auto-committer.git'})
