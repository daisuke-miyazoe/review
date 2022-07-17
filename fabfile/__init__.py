from fabric.api import local

def deploy():
    local("git add . && git commit -m 'commit message'")
    local("git push")