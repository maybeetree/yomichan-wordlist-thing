# How to run command-line programs

Many projects on github (including this one!)
have instructions that tell you to run commands,
often formatted like this: `python3 somefile.py`.

If you've never used a terminal before,
this can be seem quite confusing.
*What does it mean?*
*Where do I type this?*

This file hopefully explains the basics of using the command line.

## Windows

You can open a terminal by pressing `Win + R`
on your keyboard,
typing `cmd` into the dialog box,
and pressing Enter.

You will see a black window with a "prompt"
that looks like
`C:\Users\yourusername`.
This means you are currently in your home directory.
You can type `dir` and press enter
to see what files and directories are in your home
directory.
You will likely see directories such as `Desktop`,
`Downloads`, and so forth.

You can type `cd <name of directory>` to go into that directory.
You can also type `cd ..` to go up a directory.
Typing `python3 <filename>` will run `<filename>`
with the Python interpreter.

So, for example,
if you saved `server.py` on your desktop,
and you want to run it,
you could open a new command prompt,
type `cd Desktop` to go into your
desktop,
and then type `python3 server.py`
to run it.

You will see that
`C:\Users\yourname\Desktop` prompt will no longer appear.
This means that `server.py` is running,
and the terminal cannot accept commands right now.
You can stop the server by pressing `Ctrl + C`,
which will allow you to run commands once again
(you can also just close the `cmd` window).

### If your Python is missing

If the command prompt complains that
`'python' is not recognized as an internal or external command,
operable program or batch file.`,
that means you don't have Python installed.

You can install Python through the official website,
or through the Windows store.
For this program,
a relatively recent version of Python3 is needed
(3.10, 3.11, and 3.12 should all work).

Some versions of Windows also automatically open
windows store
if you type `python` into cmd while it is not installed.

### If Python complains that it can't find the file.

If Python yells at you that it
can't open `server.py`,
this might mean that you're in the wrong directory.
Use the `dir` command to show the files in the current directory,
and if you can't see `server.py`,
navigate to the correct directory using the `cd` command
as described above.

## Linux

On most desktop environments,
you can open a terminal by pressing
`Ctrl + Alt + T`.
If that doesn't work,
try searching for "Terminal"
in your app launcher.

Once you open a terminal,
you can see a prompt,
which means the terminal is ready to accept commands.
You can type `pwd` and press enter,
which will show which directory you're currently in.
Normally, it's something like
`/home/yourusername`,
which is your home directory.

Depending on configuration, the prompt text
will also show what directory you're in,
so you don't have to type `pwd` every time.
Usually, your home directory
is abbreviated as the character `~`.

You can type `ls` to show which files and folders
are in the current directory.
You will likely see things like `Desktop`,
`Downloads`, and `Documents`
in your home directory.
You can run `cd <dirname>` to go inside of a directory,
and `cd ..` to go up a directory level.

To run a Python program,
you can type `python3 <filename>`.
So, to run `server.py`,
you would run `python3 server.py`.

You will see that
the prompt text will no longer appear.
This means that `server.py` is running,
and the terminal cannot accept commands right now.
You can stop the server by pressing `Ctrl + C`,
which will allow you to run commands once again
(you can also just close the terminal window).

### If your Python is missing

If the shell complains that `python3: command not found`,
that means Python is not installed.
You can install python with your system's package manager.
For this program,
Python 3 is needed, not Python 2.

Some distros like Ubuntu will even tell you what command to
run to install Python if it is not found.

### If Python complains that it can't find the file.

If Python yells at you that it
can't open `server.py`,
this might mean that you're in the wrong directory.
Use the `ls` command to show the files in the current directory,
and if you can't see `server.py`,
navigate to the correct directory using the `cd` command
as described above.

