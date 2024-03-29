# Running Python 2 virtual envs on an M1 Mac

## Option 1 (untested) - Run a terminal in Rosetta mode
Mac comes shipped with a transpiler called Rosetta which will allow you to run
x86 programs on M1 chips.

I haven't tried this method, but this should allow you to run code designed for
Intel's x86 chips on your M1 Mac without problems, including old python binaries
and other programs.

### Method

1. Open `Applications/` in Finder.
1. Make a copy of your terminal program.
1. Rename this copy something useful, for example « Rosetta Terminal »
1. Right click the copy of your terminal program.
1. Click the checkbox that says « run in Rosetta mode » (or something like that)

From now on when you open that program, it will run as if it's on x86 architecture.

## Option 2: Hack up your terminal

Option 2 involves disabling some of the default safety features of your mac,
making changes to your `.bashrc` / `.zshrc` / equivalent file, and running a
command to launch your terminal into x86 mode.

1. Install {that python package}
1. Make a note of wherever your machine dumped the binary files
1. Add the following lines to your `.bashrc` / `.zshrc` / equivalent file:

```
```

1. Disable `csrutil`
  1. Restart your mac in recovery mode
  1. Open up a terminal
  1. Run `csrutil disable`
  1. Restart and log back into your Mac

1. Run `csrutil status` to check that `csrutil` has been successfully disabled.

If successful, your terminal should output:

```
csrutil status: disabled
```

1. Run the following command to enter x86 mode

```
$ arch ...
```

1. You should now be able to run the following commands without any issues


```
$ mkvirtualenv --python=python2
$ activate
$ python2 -V  # Check that pythno2 works
$ pip2 -V  # Check that pip is using pip2 and works successfully
```

Congratulations, you've set up python2 and virtual environments on your M1 Mac!
