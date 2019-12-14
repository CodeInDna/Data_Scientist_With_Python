# The Unix command line has survived and thrived for almost 50 years because it lets people do complex things with just a few keystrokes. Sometimes called "the universal glue of programming," it helps users combine existing programs in new ways, automate repetitive tasks, and run programs on clusters and clouds that may be halfway around the world. This course will introduce its key elements and show you how to use them efficiently.
# Manipulating files and directories
# How does the shell compare to a desktop interface?
# An operating system like Windows, Linux, or Mac OS is a special kind of program. It controls the computer's processor, hard drive, and network connection, but its most important job is to run other programs.

# Since human beings aren't digital, they need an interface to interact with the operating system. The most common one these days is a graphical file explorer, which translates clicks and double-clicks into commands to open files and run programs. Before computers had graphical displays, though, people typed instructions into a program called a command-line shell. Each time a command is entered, the shell runs some other programs, prints their output in human-readable form, and then displays a prompt to signal that it's ready to accept the next command. (Its name comes from the notion that it's the "outer shell" of the computer.)

# Typing commands instead of clicking and dragging may seem clumsy at first, but as you will see, once you start spelling out what you want the computer to do, you can combine old commands to create new ones and automate repetitive operations with just a few keystrokes.

# What is the relationship between the graphical file explorer that most people use and the command-line shell?

# Both take the user's commands (whether typed or clicked) and send them to the operating system.

# Where am I?
# The filesystem manages files and directories (or folders). Each is identified by an absolute path that shows how to reach it from the filesystem's root directory: /home/repl is the directory repl in the directory home, while /home/repl/course.txt is a file course.txt in that directory, and / on its own is the root directory.

# To find out where you are in the filesystem, run the command pwd (short for "print working directory"). This prints the absolute path of your current working directory, which is where the shell runs commands and looks for files by default.
# pwd

# How can I move to another directory?
# Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command cd (which stands for "change directory").

# If you type cd seasonal and then type pwd, the shell will tell you that you are now in /home/repl/seasonal. If you then run ls on its own, it shows you the contents of /home/repl/seasonal, because that's where you are. If you want to get back to your home directory /home/repl, you can use the command cd /home/repl.
$ cd seasonal
$ pwd
/home/repl/seasonal
$ ls
autumn.csv  spring.csv  summer.csv  winter.csv

# How can I move up a directory?
# The parent of a directory is the directory above it. For example, /home is the parent of /home/repl, and /home/repl is the parent of /home/repl/seasonal. You can always give the absolute path of your parent directory to commands like cd and ls. More often, though, you will take advantage of the fact that the special path .. (two dots with no spaces) means "the directory above the one I'm currently in". If you are in /home/repl/seasonal, then cd .. moves you up to /home/repl. If you use cd .. once again, it puts you in /home. One more cd .. puts you in the root directory /, which is the very top of the filesystem. (Remember to put a space between cd and .. - it is a command and a path, not a single four-letter command.)

# A single dot on its own, ., always means "the current directory", so ls on its own and ls . do the same thing, while cd . has no effect (because it moves you into the directory you're currently in).

# One final special path is ~ (the tilde character), which means "your home directory", such as /home/repl. No matter where you are, ls ~ will always list the contents of your home directory, and cd ~ will always take you home.

# If you are in /home/repl/seasonal, where does cd ~/../. take you?

/home

# How can I copy files?
# You will often want to copy files, move them into other directories to organize them, or rename them. One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

# cp original.txt duplicate.txt
# creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

# cp seasonal/autumn.csv seasonal/winter.csv backup
# copies all of the files into that directory.
$ cp seasonal/summer.csv backup/summer.bck
$ cp seasonal/spring.csv seasonal/summer.csv backup

$ ls backup
spring.csv  summer.bck  summer.csv

# How can I move a file?
# While cp copies a file, mv moves it from one directory to another, just as if you had dragged it in a graphical file browser. It handles its parameters the same way as cp, so the command:

# mv autumn.csv winter.csv ..
# moves the files autumn.csv and winter.csv from the current working directory up one level to its parent directory (because .. always refers to the directory above your current location).
$ ls
backup  bin  course.txt  people  seasonal
$ mv seasonal/spring.csv seasonal/summer.csv backup


# How can I rename files?
# mv can also be used to rename files. If you run:

# mv course.txt old-course.txt
# then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.

# One warning: just like cp, mv will overwrite existing files. If, for example, you already have a file called old-course.txt, then the command shown above will replace it with whatever is in course.txt.
$ cd seasonal
$ mv winter.csv winter.csv.bck
$ ls
autumn.csv  spring.csv  summer.csv  winter.csv.bck

# How can I delete files?
# We can copy files and move them around; to delete them, we use rm, which stands for "remove". As with cp and mv, you can give rm the names of as many files as you'd like, so:

# rm thesis.txt backup/thesis-2017-08.txt
# removes both thesis.txt and backup/thesis-2017-08.txt

# rm does exactly what its name says, and it does it right away: unlike graphical file browsers, the shell doesn't have a trash can, so when you type the command above, your thesis is gone for good.

$ cd seasonal
$ rm autumn.csv
$ cd ..
$ rm seasonal/summer.csv

$ ls
backup  bin  course.txt  people  seasonal
$ rm people/agarwal.txt
$ rmdir people
$ mkdir yearly
$ mkdir yearly/2017