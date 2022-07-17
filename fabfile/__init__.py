from fabric.api import local

def deploy():
    local("git add . && git commit -m '#'")
    local("git push")