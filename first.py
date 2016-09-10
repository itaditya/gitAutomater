import subprocess
# "git commit -m 'Hellopython'",
process = subprocess.Popen(
    "git config credential.helper store", stdout=subprocess.PIPE, shell=True)

cmds = [
    "git add .",
    "git commit -m ",
    "git status",
    "git push origin master",
]
print "Enter a commit message or $ for manual git"
commitMessage = "'" + raw_input().strip() + "'"
if commitMessage == "'$'":
    print "Manual Git selected"
else:
    cmds[1] += "_".join(commitMessage.split())
    for cmd in cmds:
        query = cmd.split()
        # process = subprocess.Popen(query, stdout=subprocess.PIPE)
        if(query[1] == "push"):
            process = subprocess.Popen(
                query, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            # process.stdin.write("itaditya")
            # process.stdin.write("9911502984.Ad")
        else:
            process = subprocess.Popen(query, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output

print 'All done!'
