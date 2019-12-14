# How can I edit a file?
# Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:

# Ctrl + K: delete a line.
# Ctrl + U: un-delete a line.
# Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
# Ctrl + X: exit the editor.

# How can I record what I just did?
# When you are doing a complex analysis, you will often want to keep a record of the commands you used. You can do this with the tools you have already seen:

# Run history.
# Pipe its output to tail -n 10 (or however many recent steps you want to save).
# Redirect that to a file called something like figure-5.history.
# This is better than writing things down in a lab notebook because it is guaranteed not to miss any steps. It also illustrates the central idea of the shell: simple tools that produce and consume lines of text can be combined in a wide variety of ways to solve a broad range of problems.

# How can I save commands to re-run later?
# You have been using the shell interactively so far. But since the commands you type in are just text, you can store them in files for the shell to run over and over again. To start exploring this powerful capability, put the following command in a file called headers.sh:

# head -n 1 seasonal/*.csv
# This command selects the first row from each of the CSV files in the seasonal directory. Once you have created this file, you can run it by typing:

# bash headers.sh
# This tells the shell (which is just a program called bash) to run the commands contained in the file headers.sh, which produces the same output as running the commands directly.

# Use nano dates.sh to create a file called dates.sh that contains this command:

# cut -d , -f 1 seasonal/*.csv
# to extract the first column from all of the CSV files in seasonal.

# To RUN
bash dates.sh

# How can I re-use pipes?
# A file full of shell commands is called a *shell script, or sometimes just a "script" for short. Scripts don't have to have names ending in .sh, but this lesson will use that convention to help you keep track of which files are scripts.

# Scripts can also contain pipes. For example, if all-dates.sh contains this line:

# cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq
# then:

# bash all-dates.sh > dates.out
# will extract the unique dates from the seasonal data files and save them in dates.out.
# $ nano teeth.sh
# $ bash teeth.sh > teeth.out
# $ cat teeth.out
#      15 bicuspid
#      31 canine
#      18 incisor
#      11 molar
#      17 wisdom

# How can I pass filenames to scripts?
# A script that processes specific files is useful as a record of what you did, but one that allows you to process any files you want is more useful. To support this, you can use the special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script".

# For example, if unique-lines.sh contains sort $@ | uniq, when you run:

# bash unique-lines.sh seasonal/summer.csv
# the shell replaces $@ with seasonal/summer.csv and processes one file. If you run this:

# bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv
# it processes two data files, and so on.

# As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.


#######################################

# How can I process a single argument?
# As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. You can use this to write commands that feel simpler or more natural than the shell's. For example, you can create a script called column.sh that selects a single column from a CSV file when the user provides the filename as the first parameter and the column as the second:

# cut -d , -f $2 $1
# and then run it using:

# bash column.sh seasonal/autumn.csv 1
# Notice how the script uses the two parameters in reverse order.

# The script get-field.sh is supposed to take a filename, the number of the row to select, the number of the column to select, and print just that field from a CSV file. For example:

# bash get-field.sh seasonal/summer.csv 4 2
# should select the second field from line 4 of seasonal/summer.csv. Which of the following commands should be put in get-field.sh to do that?
# head -n $2 $1 | tail -n 1 | cut -d , -f $3

# How can one shell script do many things?
# Our shells scripts so far have had a single command or pipe, but a script can contain many lines of commands. For example, you can create one that tells you how many records are in the shortest and longest of your data files, i.e., the range of your datasets' lengths.

# Note that in Nano, "copy and paste" is achieved by navigating to the line you want to copy, pressing CTRL + K to cut the line, then CTRL + U twice to paste two copies of it.

# As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.

# How can I write loops in a shell script?
# Shell scripts can also contain loops. You can write them using semi-colons, or split them across lines without semi-colons to make them more readable:

# # Print the first and last data records of each file.
# for filename in $@
# do
#     head -n 2 $filename | tail -n 1
#     tail -n 1 $filename
# done
# (You don't have to indent the commands inside the loop, but doing so makes things clearer.)

# The first line of this script is a comment to tell readers what the script does. Comments start with the # character and run to the end of the line. Your future self will thank you for adding brief explanations like the one shown here to every script you write.

# As a reminder, to save what you have written in Nano, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X to exit the editor.
$ nano date-range.sh
$ bash date-range.sh seasonal/*.csv
# 2017-01-05
# 2017-08-16
# 2017-01-25
# 2017-09-07
# 2017-01-11
# 2017-08-04
# 2017-01-03
# 2017-08-13
$ bash date-range.sh seasonal/*.csv | sort
# 2017-01-03
# 2017-01-05
# 2017-01-11
# 2017-01-25
# 2017-08-04
# 2017-08-13
# 2017-08-16
# 2017-09-07

for filename in $@
do
	cut -d, -f 1 $filename | grep -v Date | sort |head -n 1
	cut -d, -f 1 $filename | grep -v Date | sort |tail -n 1
done