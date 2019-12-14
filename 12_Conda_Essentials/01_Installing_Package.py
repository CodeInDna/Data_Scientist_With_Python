# Software is constantly evolving, so data scientists need a way to update the software they are using without breaking things that already work. Conda is an open source, cross-platform tool for managing packages and working environments for many different programming languages. This course explains how to use its core features to manage your software so that you and your colleagues can reproduce your working environments reliably with minimum effort.

# What version of conda do I have?
# The tool conda takes a variety of commands and arguments. Most of the time, you will use conda COMMAND OPTIONS --SWITCH. You will learn the collection of COMMANDs available in the next lessons. A summary is available on the help screen:

# $ conda --help
# usage: conda [-h] [-V] command ...

# conda is a tool for managing and deploying applications, environments and packages.

# Options:

# positional arguments:
#   command
#     clean        Remove unused packages and caches.
#     config       Modify configuration values in .condarc. This is modeled
#                  after the git config command. Writes to the user .condarc
#                  file (/Users/dmertz/.condarc) by default.
#     create       Create a new conda environment from a list of specified
#                  packages.
#     help         Displays a list of available conda commands and their help
#                  strings.
#     info         Display information about current conda install.
#     install      Installs a list of packages into a specified conda
#                  environment.
#     [... more commands ...]

# optional arguments:
#   -h, --help     Show this help message and exit.
#   -V, --version  Show the conda version number and exit.


# What is semantic versioning?
# Most Conda packages use a system called semantic versioning to identify distinct versions of a software package unambiguously. Version labels are usually chosen by the project authors, not necessarily the same people who bundle the project as a Conda package. There is no technical requirement that a project author's version label coincides with a Conda package version label, but the convention of doing so is almost always followed. Semantic version labels can be compared lexicographically and make it easy to determine which of two versions is the later version.

# Under semantic versioning, software is labeled with a three-part version identifier of the form MAJOR.MINOR.PATCH; the label components are non-negative integers separated by periods. Assuming all software starts at version 0.0.0, the MAJOR version number is increased when significant new functionality is introduced (often with corresponding API changes). Increases in the MINOR version number generally reflect improvements (e.g., new features) that avoid backward-incompatible API changes. For instance, adding an optional argument to a function API (in a way that allows old code to run unchanged) is a change worthy of increasing the MINOR version number. An increment to the PATCH version number is appropriate mostly for bug fixes that preserve the same MAJOR and MINOR revision numbers. Software patches do not typically introduce new features or change APIs at all (except sometimes to address security issues).

# Many command-line tools display their version identifier by running tool --version. This information can sometimes be displayed or documented in other ways. For example, suppose on some system, a certain version of Python is installed, and you inquire about it like this:

# python -c "import sys; sys.version"
# '1.0.1 (Mar 26 2014)'
# Looking at the output above, which statement below accurately characterizes thesemantic versioning of this installed Python?


# Find dependencies for a package version?
# The conda search package_name --info command reports a variety of details about a specific package. The syntax for specifying just one version is a little bit complex, but prefix notation is allowed here (just as you would with conda install).

# For example, running conda search cytoolz=0.8.2 --info will report on all available package versions. As this package has been built for a variety of Python versions, a number of packages will be reported on. You can narrow your query further with, e.g.:

# $ conda search cytoolz=0.8.2=py36_0 --info

# cytoolz 0.8.2 py36_0
# <hr />-----------------
# file name   : cytoolz-0.8.2-py36_0.tar.bz2
# name        : cytoolz
# version     : 0.8.2
# build string: py36_0
# build number: 0
# channel     : https://repo.continuum.io/pkgs/free
# size        : 352 KB
# arch        : x86_64
# constrains  : ()
# date        : 2016-12-23
# license     : BSD
# md5         : cd6068b2389b1596147cc7218f0438fd
# platform    : darwin
# subdir      : osx-64
# url         : https://repo.continuum.io/pkgs/free/osx-64/cytoolz-0.8.2-py36_0.tar.bz2
# dependencies:
#     python 3.6*
#     toolz >=0.8.0
# You may use the * wildcard within the match pattern. This is often useful to match 'foo=1.2.3=py36*' because recent builds have attached the hash of the build at the end of the Python version string, making the exact match unpredictable.

# Determine the dependencies of the package numpy 1.13.1 with Python 3.6.0 on your current platform.

# Installing from a channel
# We saw in the last exercise that there are about 100,000 linux-64 packages on conda-forge. Across all the channels there are about 50,000 packages, most of those for at least 3 of the 5 main platforms (osx-64, linux-32, linux-64, win-32, win-64; 32-bit support is of diminishing importance compared to 64-bit). There are around 2500 channels that have been active in the last 6 months; most are individual users, but a fair number belonging to projects or organizations. A majority of package names are published by more than one different channel; sometimes just as a copy, other times with a tweak or compiler optimization, or in a different version.

# The whole point of having channels is to be able to install packages from them. For this exercise, you will install a version of a package not available on the default channel. Adding a channel to install from simply requires using the same --channel or -c switch we have seen in other conda commands, but with the conda install command.

# For example:

# conda install --channel my-organization the-package


# Environments and why are they needed?
# Conda environments allow multiple incompatible versions of the same (software) package to coexist on your system. An environment is simply a file path containing a collection of mutually compatible packages. By isolating distinct versions of a given package (and their dependencies) in distinct environments, those versions are all available to work on particular projects or tasks.

# There are a large number of reasons why it is best practice to use environments, whether as a data scientist, software developer, or domain specialist. Without the concept of environments, users essentially rely on and are restricted to whichever particular package versions are installed globally (or in their own user accounts) on a particular machine. Even when one user moves scripts between machines (or shares them with a colleague), the configuration is often inconsistent in ways that interfere with seamless functionality. Conda environments solve both these problems. You can easily maintain and switch between as many environments as you like, and each one has exactly the collection of packages that you want.

# For example, you may develop a project comprising scripts, notebooks, libraries, or other resources that depend on a particular collection of package versions. You later want to be able to switch flexibly to newer versions of those packages and to ensure the project continues to function properly before switching wholly. Or likewise, you may want to share code with colleagues who are required to use certain package versions. In this context, an environment is a way of documenting a known set of packages that correctly support your project.

# What packages are installed in an environment? (I)
# The command conda list seen previously displays all packages installed in the current environment. You can reduce this list by appending the particular package you want as an option. The package can be specified either as a simple name, or as a regular expression pattern. This still displays the version (and channel) associated with the installed package(s). For example:

# (test-env) $ conda list 'numpy|pandas'
# # packages in environment at /home/repl/miniconda/envs/test-env:
# #
# # Name                    Version                   Build  Channel
# numpy                     1.11.3                   py35_0
# pandas                    0.18.1              np111py35_0
# Without specifying 'numpy|pandas', these same two lines would be printed, simply interspersed with many others for the various other installed packages. Notice that the output displays the filepath associated with the current environment first: in this case, /home/repl/miniconda/envs/test-env as test-env is the active environment (as also shown at the prompt).

# Following this example, what versions of numpy and pandas are installed in the current (base/root) environment?+

# What packages are installed in an environment? (II)
# It is often useful to query a different environment's configuration (i.e., as opposed to the currently active environment). You might do this simply to verify the package versions in that environment that you need for a given project. Or you may wish to find out what versions you or a colleague used in some prior project (developed in that other environment). The switch --name or -n allows you to query another environment. For example,

# (course-env) $ conda list --name test-env 'numpy|pandas'
# # packages in environment at /home/repl/miniconda/envs/test-env:
# #
# # Name                    Version                   Build  Channel
# numpy                     1.11.3                   py35_0
# pandas                    0.18.1              np111py35_0
# Without specifying the --name argument, the command conda list would run in the current environment. The output would then be the versions of numpy and pandas present in the current environment.

# Suppose you created an environment called pd-2015 in 2015 when you were working on a project. Identify which versions of numpy and pandas were installed in the environment pd-2015.

# Switch between environments
# Simply having different environments is not of much use; you need to be able to switch between environments. Most typically this is done at the command line, using the conda command. With some other interfaces (like Anaconda Navigator or Jupyter with nb_conda installed), other techniques for selecting environment are available. But for this course, you will learn about command-line use.

# To activate an environment, you simply use conda activate ENVNAME. To deactivate an environment, you use conda deactivate, which returns you to the root/base environment.

# If you used conda outside this course, and prior to version 4.4, you may have seen a more platform specific style. On older versions, Windows users would type activate ENVNAME and deactivate, while Linux and OSX users would type source activate ENVNAME and source deactivate. The unified style across platforms is more friendly. Related to the change to conda activate, version 4.4 and above use a special environment called base that is equivalent to what was called root in older versions. However, in old versions of conda you would not typically see an environment listed on the terminal prompt when you were in the root environment.


# Switch between environments
# Simply having different environments is not of much use; you need to be able to switch between environments. Most typically this is done at the command line, using the conda command. With some other interfaces (like Anaconda Navigator or Jupyter with nb_conda installed), other techniques for selecting environment are available. But for this course, you will learn about command-line use.

# To activate an environment, you simply use conda activate ENVNAME. To deactivate an environment, you use conda deactivate, which returns you to the root/base environment.

# If you used conda outside this course, and prior to version 4.4, you may have seen a more platform specific style. On older versions, Windows users would type activate ENVNAME and deactivate, while Linux and OSX users would type source activate ENVNAME and source deactivate. The unified style across platforms is more friendly. Related to the change to conda activate, version 4.4 and above use a special environment called base that is equivalent to what was called root in older versions. However, in old versions of conda you would not typically see an environment listed on the terminal prompt when you were in the root environment.

# Remove an environment
# From time to time, it is worth cleaning up the environments you have accumulated just to make management easier. Doing so is not pressing; as they use little space or resources. But it's definitely useful to be able to see a list of only as many environments as are actually useful for you.

# The command to remove an environment is:

# conda env remove --name ENVNAME
# You may also use the shorter -n switch instead.

# Create a new environment
# This course is configured with several environments, but in your use you will need to create environments meeting your own purposes. The basic command for creating environments is conda create. You will always need to specify a name for your environment, using --name (or short form -n), and you may optionally specify packages (with optional versions) that you want in that environment initially. You do not need to specify any packages when creating; either way you can add or remove whatever packages you wish from an environment later.

# The general syntax is similar to:

# conda create --name recent-pd python=3.6 pandas=0.22 scipy statsmodels
# This command will perform consistency resolution on those packages and versions indicated, in the same manner as a conda install will. Notice that even though this command works with environments it is conda create rather than a conda env ... command.

# Export an environment
# Using conda list provides useful information about the packages that are installed. However, the format it describes packages in is not immediately usable to let a colleague or yourself to recreate exactly the same environment on a different machine. For that you want the conda env export command.

# There are several optional switches to this command. If you specify -n or --name you can export an environment other than the active one. Without that switch it chooses the active environment. If you specify -f or --file you can output the environment specification to a file rather than just to the terminal output. If you are familiar with piping, you might prefer to pipe the output to a file rather than use the --file switch. By convention, the name environment.yml is used for environment, but any name can be used (but the extension .yml is strongly encouraged).

# Without saving to a file, the output might look similar to the below. Notice that this gives exact versions of packages, not simply ranges or prefixes. This assures exact reproducibility of computation within the same environment on a different machine.

# $ conda env export -n pd-2015
# name: pd-2015
# channels:
#   - defaults
# dependencies:
#   - certifi=2018.1.18=py35_0
#   - libffi=3.2.1=hd88cf55_4
#   - libgcc-ng=7.2.0=h7cc24e2_2
#   - libgfortran-ng=7.2.0=h9f7466a_2
#   - mkl=2018.0.1=h19d6760_4
#   - numpy=1.9.3=py35hff6eb55_3
#   - openssl=1.0.2n=hb7f436b_0
#   - pandas=0.17.1=np19py35_0
#   - pip=9.0.1=py35h7e7da9d_4
#   - python=3.5.4=h417fded_24
#   - python-dateutil=2.6.1=py35h90d5b31_1
#   - pytz=2017.3=py35hb13c558_0
#   - readline=7.0=ha6073c6_4
#   - setuptools=38.4.0=py35_0
#   - six=1.11.0=py35h423b573_1
#   - xz=5.2.3=h55aa19d_2
#   - zlib=1.2.11=ha838bed_2
#   - pip:
#     - chardet==3.0.4
#     - pexpect==4.2.1
#     - urllib3==1.22
# prefix: /home/repl/miniconda/envs/pd-2015

conda env export -n course-env --file course-env.yml

# Create an environment from a shared specification
# You may recreate an environment from one of the YAML (Yet Another Markup Language) format files produced by conda env export. However, it is also easy to hand write an environment specification with less detail. For example, you might describe an environment you need and want to share with colleagues as follows:

# $ cat shared-project.yml
# name: shared-project
# channels:
#   - defaults
# dependencies:
#   - python=3.6
#   - pandas>=0.21
#   - scikit-learn
#   - statsmodels
# Clearly this version is much less specific than what conda env export produces. But it indicates the general tools, with some version specification, that will be required to work on a shared project. Actually creating an environment from this sketched out specification will fill in all the dependencies of those large projects whose packages are named, and this will install dozens of packages not explicitly listed. Often you are happy to have other dependencies in the manner conda decides is best.

# Of course, a fully fleshed out specification like we saw in the previous exercise are equally usable. Non-relevant details like the path to the environment on the local system are ignored when installing to a different machine or to a different platform altogether, which will work equally well.

# To create an environment from file-name.yml, you can use the following command:

# conda env create --file file-name.yml
# As a special convention, if you use the plain command conda env create without specifying a YAML file, it will assume you mean the file environment.yml that lives in the local directory.
