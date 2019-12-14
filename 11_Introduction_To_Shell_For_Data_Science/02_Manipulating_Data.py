# How can I view a file's contents?
# Before you rename or delete files, you may want to have a look at their contents. The simplest way to do this is with cat, which just prints the contents of files onto the screen. (Its name is short for "concatenate", meaning "to link things together", since it will print all the files whose names you give it, one after the other.)

# cat agarwal.txt
# name: Agarwal, Jasmine
# position: RCT2
# start: 2017-04-01
# benefits: full

$ ls
backup  bin  course.txt  people  seasonal
$ cat course.txt
# Introduction to the Unix Shell for Data Science

# The Unix command line has survived and thrived for almost fifty years
# because it lets people to do complex things with just a few
# keystrokes. Sometimes called "the duct tape of programming", it helps
# users combine existing programs in new ways, automate repetitive
# tasks, and run programs on clusters and clouds that may be halfway
# around the world. This lesson will introduce its key elements and show
# you how to use them efficiently.

# How can I view a file's contents piece by piece?
# You can use cat to print large files and then scroll through the output, but it is usually more convenient to page the output. The original command for doing this was called more, but it has been superseded by a more powerful command called less. (This kind of naming is what passes for humor in the Unix world.) When you less a file, one page is displayed at a time; you can press spacebar to page down or type q to quit.

# If you give less the names of several files, you can type :n (colon and a lower-case 'n') to move to the next file, :p to go back to the previous one, or :q to quit.

# Note: If you view solutions to exercises that use less, you will see an extra command at the end that turns paging off so that we can test your solutions efficiently.
$ ls
backup  bin  course.txt  people  seasonal
$ less seasonal/spring.csv seasonal/summer.csv

# How can I look at the start of a file?
# The first thing most data scientists do when given a new dataset to analyze is figure out what fields it contains and what values those fields have. If the dataset has been exported from a database or spreadsheet, it will often be stored as comma-separated values (CSV). A quick way to figure out what it contains is to look at the first few rows.

# We can do this in the shell using a command called head. As its name suggests, it prints the first few lines of a file (where "a few" means 10), so the command:

# head seasonal/summer.csv
# displays:

# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom
# 2017-01-21,bicuspid
# 2017-02-02,molar
# 2017-02-27,wisdom
# 2017-02-27,wisdom
# 2017-03-07,bicuspid
# 2017-03-15,wisdom
# 2017-03-20,canine
# What does head do if there aren't 10 lines in the file? (To find out, use it to look at the top of people/agarwal.txt.)

# Display as many lines as there are.

# How can I type less?
# One of the shell's power tools is tab completion. If you start typing the name of a file and then press the tab key, the shell will do its best to auto-complete the path. For example, if you type sea and press tab, it will fill in the directory name seasonal/ (with a trailing slash). If you then type a and tab, it will complete the path as seasonal/autumn.csv.

# If the path is ambiguous, such as seasonal/s, pressing tab a second time will display a list of possibilities. Typing another character or two to make your path more specific and then pressing tab will fill in the rest of the name.

# How can I control what commands do?
# You won't always want to look at the first 10 lines of a file, so the shell lets you change head's behavior by giving it a command-line flag (or just "flag" for short). If you run the command:

# head -n 3 seasonal/summer.csv
# head will only display the first three lines of the file. If you run head -n 100, it will display the first 100 (assuming there are that many), and so on.

# A flag's name usually indicates its purpose (for example, -n is meant to signal "number of lines"). Command flags don't have to be a - followed by a single letter, but it's a widely-used convention.

# Note: it's considered good style to put all flags before any filenames, so in this course, we only accept answers that do that.
$ head -n 5 seasonal/winter.csv
Date,Tooth
# 2017-01-03,bicuspid
# 2017-01-05,incisor
# 2017-01-21,wisdom
# 2017-02-05,molar

# How can I list everything below a directory?
# In order to see everything underneath a directory, no matter how deeply nested it is, you can give ls the flag -R (which means "recursive"). If you use ls -R in your home directory, you will see something like this:

# backup          course.txt      people          seasonal

# ./backup:

# ./people:
# agarwal.txt

# ./seasonal:
# autumn.csv      spring.csv      summer.csv      winter.csv
# This shows every file and directory in the current level, then everything in each sub-directory, and so on.
$ ls -R
.:
backup  bin  course.txt  people  seasonal

./backup:

./bin:

./people:
agarwal.txt

./seasonal:
autumn.csv  spring.csv  summer.csv  winter.csv
$ ls -R -F
.:
backup/  bin/  course.txt  people/  seasonal/

./backup:

./bin:

./people:
agarwal.txt

./seasonal:
autumn.csv  spring.csv  summer.csv  winter.csv


# How can I get help for a command?
# To find out what commands do, people used to use the man command (short for "manual"). For example, the command man head brings up this information:

# HEAD(1)               BSD General Commands Manual              HEAD(1)

# NAME
#      head -- display first lines of a file

# SYNOPSIS
#      head [-n count | -c bytes] [file ...]

# DESCRIPTION
#      This filter displays the first count lines or bytes of each of
#      the specified files, or of the standard input if no files are
#      specified.  If count is omitted it defaults to 10.

#      If more than a single file is specified, each file is preceded by
#      a header consisting of the string ``==> XXX <=='' where ``XXX''
#      is the name of the file.

# SEE ALSO
#      tail(1)
# man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.

# The one-line description under NAME tells you briefly what the command does, and the summary under SYNOPSIS lists all the flags it understands. Anything that is optional is shown in square brackets [...], either/or alternatives are separated by |, and things that can be repeated are shown by ..., so head's manual page is telling you that you can either give a line count with -n or a byte count with -c, and that you can give it any number of filenames.

# The problem with the Unix manual is that you have to know what you're looking for. If you don't, you can search Stack Overflow, ask a question on DataCamp's Slack channels, or look at the SEE ALSO sections of the commands you already know.

$ man tail
$ tail -n +7 seasonal/spring.csv
# 2017-03-12,wisdom
# 2017-03-14,incisor
# 2017-03-21,molar
# 2017-04-29,wisdom
# 2017-05-08,canine
# 2017-05-20,canine
# 2017-05-21,canine
# 2017-05-25,canine
# 2017-06-04,molar
# 2017-06-13,bicuspid
# 2017-06-14,canine
# 2017-07-10,incisor
# 2017-07-16,bicuspid
# 2017-07-23,bicuspid
# 2017-08-13,bicuspid
# 2017-08-13,incisor
# 2017-08-13,wisdom
# 2017-09-07,molar


# How can I select columns from a file?
# head and tail let you select rows from a text file. If you want to select columns, you can use the command cut. It has several options (use man cut to explore them), but the most common is something like:

# cut -f 2-5,8 -d , values.csv
# which means "select columns 2 through 5 and columns 8, using comma as the separator". cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

# What command will select the first column (containing dates) from the file spring.csv?

$ cut -f 1 -d , seasonal/spring.csv
Date
# 2017-01-25
# 2017-02-19
# 2017-02-24
# 2017-02-28
# 2017-03-04
# 2017-03-12
# 2017-03-14
# 2017-03-21
# 2017-04-29
# 2017-05-08
# 2017-05-20
# 2017-05-21
# 2017-05-25
# 2017-06-04
# 2017-06-13
# 2017-06-14
# 2017-07-10
# 2017-07-16
# 2017-07-23
# 2017-08-13
# 2017-08-13
# 2017-08-13
# 2017-09-07



# What can't cut do?
# cut is a simple-minded command. In particular, it doesn't understand quoted strings. If, for example, your file is:

# Name,Age
# "Johel,Ranjit",28
# "Sharma,Rupinder",26
# then:

# cut -f 2 -d , everyone.csv
# will produce:

# Age
# Ranjit"
# Rupinder"
# rather than everyone's age, because it will think the comma between last and first names is a column separator.

# What is the output of cut -d : -f 2-4 on the line:

# first:second:third:
# (Note the trailing colon.)

# second:third:

# How can I repeat commands?
# One of the biggest advantages of using the shell is that it makes it easy for you to do things over again. If you run some commands, you can then press the up-arrow key to cycle back through them. You can also use the left and right arrow keys and the delete key to edit them. Pressing return will then run the modified command.

# Even better, history will print a list of commands you have run recently. Each one is preceded by a serial number to make it easy to re-run particular commands: just type !55 to re-run the 55th command in your history (if you have that many). You can also re-run a command by typing an exclamation mark followed by the command's name, such as !head or !cut, which will re-run the most recent use of that command.

$ head summer.csv
head: cannot open 'summer.csv' for reading: No such file or directory
$ cd seasonal
$ !head
head summer.csv
# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom
# 2017-01-21,bicuspid
# 2017-02-02,molar
# 2017-02-27,wisdom
# 2017-02-27,wisdom
# 2017-03-07,bicuspid
# 2017-03-15,wisdom
# 2017-03-20,canine
# $ history
#     1  head summer.csv
#     2  cd seasonal
#     3  head summer.csv
#     4  history
$ !3
head summer.csv
# Date,Tooth
# 2017-01-11,canine
# 2017-01-18,wisdom
# 2017-01-21,bicuspid
# 2017-02-02,molar
# 2017-02-27,wisdom
# 2017-02-27,wisdom
# 2017-03-07,bicuspid
# 2017-03-15,wisdom
# 2017-03-20,canine

# How can I select lines containing specific values?
# head and tail select rows, cut selects columns, and grep selects lines according to what they contain. In its simplest form, grep takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text. For example, grep bicuspid seasonal/winter.csv prints lines from winter.csv that contain "bicuspid".

# grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

# -c: print a count of matching lines rather than the lines themselves
# -h: do not print the names of files when searching multiple files
# -i: ignore case (e.g., treat "Regression" and "regression" as matches)
# -l: print the names of files that contain matches, not the matches
# -n: print line numbers for matching lines
# -v: invert the match, i.e., only show lines that don't match

$ grep molar seasonal/autumn.csv
# 2017-02-01,molar
# 2017-05-25,molar
$ grep molar -v -c seasonal/autumn.csv
# 19
$ grep molar -v -c -n seasonal/autumn.csv
# 19
$ grep molar -v -c -n seasonal/spring.csv
# 21
$ grep molar -v -n seasonal/spring.csv
# 1:Date,Tooth
# 2:2017-01-25,wisdom
# 3:2017-02-19,canine
# 4:2017-02-24,canine
# 5:2017-02-28,wisdom
# 6:2017-03-04,incisor
# 7:2017-03-12,wisdom
# 8:2017-03-14,incisor
# 10:2017-04-29,wisdom
# 11:2017-05-08,canine
# 12:2017-05-20,canine
# 13:2017-05-21,canine
# 14:2017-05-25,canine
# 16:2017-06-13,bicuspid
# 17:2017-06-14,canine
# 18:2017-07-10,incisor
# 19:2017-07-16,bicuspid
# 20:2017-07-23,bicuspid
# 21:2017-08-13,bicuspid
# 22:2017-08-13,incisor
# 23:2017-08-13,wisdom
$ ls
# backup  bin  course.txt  people  seasonal
$ grep incisor -c seasonal/autumn.csv seasonal/winter.csv
# seasonal/autumn.csv:3
# seasonal/winter.csv:6


# Why isn't it always safe to treat data as text?
# The SEE ALSO section of the manual page for cut refers to a command called paste that can be used to combine data files instead of cutting them up.

# Read the manual page for paste, and then run paste to combine the autumn and winter data files in a single table using a comma as a separator. What's wrong with the output from a data analysis point of view?



# How can I store a command's output in a file?
# All of the tools you have seen so far let you name input files. Most don't have an option for naming an output file because they don't need one. Instead, you can use redirection to save any command's output anywhere you want. If you run this command:

# head -n 5 seasonal/summer.csv
# it prints the first 5 lines of the summer data on the screen. If you run this command instead:

# head -n 5 seasonal/summer.csv > top.csv
# nothing appears on the screen. Instead, head's output is put in a new file called top.csv. You can take a look at that file's contents using cat:

# cat top.csv
# The greater-than sign > tells the shell to redirect head's output to a file. It isn't part of the head command; instead, it works with every shell command that produces output.

tail -n 5 seasonal/winter.csv > last.csv


# How can I use a command's output as an input?
# Suppose you want to get lines from the middle of a file. More specifically, suppose you want to get lines 3-5 from one of our data files. You can start by using head to get the first 5 lines and redirect that to a file, and then use tail to select the last 3:

# head -n 5 seasonal/winter.csv > top.csv
# tail -n 3 top.csv
# A quick check confirms that this is lines 3-5 of our original file, because it is the last 3 lines of the first 5.

$ tail -n 2 seasonal/winter.csv >  bottom.csv
$ head -n 1 bottom.csv
# 2017-08-11,wisdom

# What's a better way to combine commands?
# Using redirection to combine commands has two drawbacks:

# It leaves a lot of intermediate files lying around (like top.csv).
# The commands to produce your final result are scattered across several lines of history.
# The shell provides another tool that solves both of these problems at once called a pipe. Once again, start by running head:

# head -n 5 seasonal/summer.csv
# Instead of sending head's output to a file, add a vertical bar and the tail command without a filename:

# head -n 5 seasonal/summer.csv | tail -n 3
# The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.

$ cut -d, -f 2 seasonal/summer.csv | grep -v Tooth

# How can I combine many commands?
# You can chain any number of commands together. For example, this command:

# cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10
# will:

# select the first column from the spring data;
# remove the header line containing the word "Date"; and
# select the first 10 lines of actual data.
cut -d , -f 2 seasonal/summer.csv | grep -v Tooth | head -n 1

# How can I count the records in a file?
# The command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.

$ grep 2017-07 seasonal/spring.csv | wc -l

# How can I specify many files at once?
# Most shell commands will work on multiple files if you give them multiple filenames. For example, you can get the first column from all of the seasonal data files at once like this:

# cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv
# But typing the names of many files over and over is a bad idea: it wastes time, and sooner or later you will either leave a file out or repeat a file's name. To make your life better, the shell allows you to use wildcards to specify a list of files with a single expression. The most common wildcard is *, which means "match zero or more characters". Using it, we can shorten the cut command above to this:

# cut -d , -f 1 seasonal/*
# or:

# cut -d , -f 1 seasonal/*.csv
$ head -n 3 seasonal/s*

# What other wildcards can I use?
# The shell has other wildcards as well, though they are less commonly used:

# ? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
# [...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
# {...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.
# Which expression would match singh.pdf and johel.txt but not sandhu.pdf or sandhu.txt?

# How can I sort lines of text?
# As its name suggests, sort puts data in order. By default it does this in ascending alphabetical order, but the flags -n and -r can be used to sort numerically and reverse the order of its output, while -b tells it to ignore leading blanks and -f tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.
 cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r

#  How can I remove duplicate lines?
# Another command that is often used with sort is uniq, whose job is to remove duplicated lines. More specifically, it removes adjacent duplicated lines. If a file contains:

# 2017-07-03
# 2017-07-03
# 2017-08-03
# 2017-08-03
# then uniq will produce:

# 2017-07-03
# 2017-08-03
# but if it contains:

# 2017-07-03
# 2017-08-03
# 2017-07-03
# 2017-08-03
# then uniq will print all four lines. The reason is that uniq is built to work with very large files. In order to remove non-adjacent lines from a file, it would have to keep the whole file in memory (or at least, all the unique lines seen so far). By only removing adjacent duplicates, it only has to keep the most recent unique line in memory.
cut -f 2 -d , seasonal/winter.csv | grep -v Tooth | sort | uniq -c