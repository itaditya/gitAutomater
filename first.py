import subprocess
# "git commit -m 'Hellopython'",
cmds = [
    "git add .",
    "git commit -m ",
    "git status"
]
commitMessage = "'" + raw_input().strip() + "'"
cmds[1] += "_".join(commitMessage.split())
for cmd in cmds:
    print ">>", cmd
    query = cmd.split()
    process = subprocess.Popen(query, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
