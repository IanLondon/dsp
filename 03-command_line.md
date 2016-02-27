# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> `mkdir -p several/nested/"dirs just"/like/this` (`p` for path)

>> `ls -l` "list" detailed format

>> `ls -R` recursively show all files from pwd

>> `cp -r sourceDir/ destDir/` copy directories and contents

>> `less text.txt` You don't have to do `cat text.txt | less`.

>> `rm one.txt two.txt three.txt` remove multiple files in one line

>> `rm -r someDir/` for directories with contents & `rmdir` for empty directories

>> `command > file` takes the output of the program and writes it to the file (overwriting). In contrast, `command >> file` _appends_ the output to the file.

>> `find startDir -name "*.txt"` (or whatever filter you want)

>> `grep -R "import numpy" ~/Projects/*.py` to find all .py files in that directory and its subdirectories with "import numpy" in them.

>> `env` lists all your env vars

>> `export MYVAR="spam"` to set the var, then `echo $MYVAR` to show its value. Delete the var with `unset MYVAR`

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> `ls` lists the contents of directories.

>> `ls -a` shows hidden files & directories (eg `.gitignore`)

>> `ls -l` is the "long listing format", it shows extra info about each file (permissions & ownership, date/time last modified, size)

>> `ls -lh` shows the sizes in human-readable format: eg 4K (that's 4KB) instead of 4096.

>> `ls -a -lh` shows long listing with human-readable sizes, including hidden files.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> `xargs` takes piped input (usually file names from `find` or `grep`) and executes a specified command on that piped input.

>> For example, `find . -name "*.py" | xargs grep "function lostFunction"` may help you find a long-lost function.

---
