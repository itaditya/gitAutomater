import subprocess

cmds = [
    "git add .",
    "git commit -m 'Hellopython'",
    "git status"
]
for cmd in cmds:
    query = cmd.split()
    print query
    process = subprocess.Popen(query, stdout=subprocess.PIPE)
    output = process.communicate()[0]
