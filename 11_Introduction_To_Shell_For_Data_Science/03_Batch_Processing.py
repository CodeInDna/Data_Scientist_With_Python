# How does the shell store information?
# Like other programs, the shell stores information in variables. Some of these, called environment variables, are available all the time. Environment variables' names are conventionally written in upper case, and a few of the more commonly-used ones are shown below.

# Variable	Purpose	Value
# HOME	User's home directory	/home/repl
# PWD	Present working directory	Same as pwd command
# SHELL	Which shell program is being used	/bin/bash
# USER	User's ID	repl
# To get a complete list (which is quite long), you can type set in the shell.

# Use set and grep with a pipe to display the value of HISTFILESIZE, which determines how many old commands are stored in your command history. What is its value?

# How can I print a variable's value?
# A simpler way to find a variable's value is to use a command called echo, which prints its arguments. Typing

# echo hello DataCamp!
# prints

# hello DataCamp!
# If you try to use it to print a variable's value like this:

# echo USER
# it will print the variable's name, USER.

# To get the variable's value, you must put a dollar sign $ in front of it. Typing

# echo $USER
# prints

# repl
# This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)


# How else does the shell store information?
# The other kind of variable is called a shell variable, which is like a local variable in a programming language.

# To create a shell variable, you simply assign a value to a name:

# training=seasonal/summer.csv
# without any spaces before or after the = sign. Once you have done this, you can check the variable's value with:

# echo $training
# seasonal/summer.csv
==> seasonal/winter.csv <==
Date,Tooth
$ head -n 1 $testing
Date,Tooth

# How can I repeat a command many times?
# Shell variables are also used in loops, which repeat commands many times. If we run this command:

# for filetype in gif jpg png; do echo $filetype; done
# it produces:

# gif
# jpg
# png
# Notice these things about the loop:

# The structure is for ...variable... in ...list... ; do ...body... ; done
# The list of things the loop is to process (in our case, the words gif, jpg, and png).
# The variable that keeps track of which thing the loop is currently processing (in our case, filetype).
# The body of the loop that does the processing (in our case, echo $filetype).
# Notice that the body uses $filetype to get the variable's value instead of just filetype, just like it does with any other shell variable. Also notice where the semi-colons go: the first one comes between the list and the keyword do, and the second comes between the body and the keyword done.
$ for filetype in docx odt pdf; do echo $filetype; done
docx
odt
pdf

# How can I repeat a command once for each file?
# You can always type in the names of the files you want to process when writing the loop, but it's usually better to use wildcards. Try running this loop in the console:

# for filename in seasonal/*.csv; do echo $filename; done
# It prints:

# seasonal/autumn.csv
# seasonal/spring.csv
# seasonal/summer.csv
# seasonal/winter.csv
# because the shell expands seasonal/*.csv to be a list of four filenames before it runs the loop.

$ for filename in people/*; do echo $filename; done
people/agarwal.txt

# How can I record the names of a set of files?
# People often set a variable using a wildcard expression to record a list of filenames. For example, if you define datasets like this:

# datasets=seasonal/*.csv
# you can display the files' names later using:

# for filename in $datasets; do echo $filename; done
# This saves typing and makes errors less likely.

# If you run these two commands in your home directory, how many lines of output will they print?

# files=seasonal/*.csv
# for f in $files; do echo $f; done

# How can I run many commands in a single loop?
# Printing filenames is useful for debugging, but the real purpose of loops is to do things with multiple files. This loop prints the second line of each data file:

# for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
# It has the same structure as the other loops you have already seen: all that's different is that its body is a pipeline of two commands instead of a single command.

$ for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done
# 2017-07-21,bicuspid
# 2017-07-23,bicuspid
# 2017-07-25,canine
# 2017-07-17,canine