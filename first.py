import subprocess
# "git commit -m 'Hellopython'",
cmds = [
    "git add .",
    "git commit -m ",
    "git status",
    "git push origin master",
]
commitMessage = "'" + raw_input().strip() + "'"
cmds[1] += "_".join(commitMessage.split())
for cmd in cmds:
    print ">>", cmd
    query = cmd.split()
    # process = subprocess.Popen(query, stdout=subprocess.PIPE)
    process = 0
    if(query[1] == "push"):
        print "push"
        process = subprocess.Popen(
            query, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        # process.stdin.write("itaditya")
        # process.stdin.write("9911502984.Ad")
    else:
        process = subprocess.Popen(query, stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

print 'All done!'
