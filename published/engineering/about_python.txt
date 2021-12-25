# About Python

## My history with Python

Let's begin this with a short story: my background and relationship with Python.

I've been working in Python now for the better part of 9 years, since I was 14.
I first picked it up during work shadowing of my dad on the advice of one of his
colleagues, Ryan. Ryan took me aside one day for lunch, and in the dazzling
light of the company cafe told me that learning programming was the skill for
the future.

I had known and appreciated this for a while at this point. I had picked up some
C-sharp (and Scratch) during high school, but stopped after the learning
opportunities for it dried up at my school. Ryan lent me his book «learn Python
the hard way», and I worked through all the exercises. I would look things up
online when I got home, bought a few more books, and eventually picked up the
ideas of object-oriented Python.

In the summer of my first year at university, I came into contact with the
language again for a research project in Imperial College's Opesci group, who
were working on a project to calculate stencil equations quickly. Their target
audience were big oil companies, who use this technology a lot when searching
for new sources of undersea oil. The research project I was working on was to
make some notebooks, learn their API, and solve some simple problems with it for
the sake of demos.

I then continued to use Python for the rest of my time at university on various
projects, and when it came to it, my thesis and first jobs all used Python.

My brush ins with Python have been at times convenient and at other times
painful. Let's go through some of these.

## The good

Python has so many redeeming properties, but to me, the best are its syntax and
its libraries.

Python's syntax is super minimal, and highly human readable. This makes it easy
to learn, hard to make typos that will make your code fail to run, and just
plainly _looks good_.

It's enjoyable and quick to write Python, especially if you just need a quick
script.

Its libraries are also very rich - by having a large userbase, particularly in
academia, Python has accumulated a huge numebr of packages, especially in
cutting-edge fields like machine learning, image processing, and graphing.

Its got good testing libraries too. Tests are quick to write, easy to run, and
have options for abstractions that allow less technical users to describe the
test conditions they want. This means that less technical users can write
specifications _for_ programmers.

This said, Python would benefit from some quicker-to-use plotting libraries. R
has some pretty awesome ones, and I do wish Python would take inspiration from
them.

All this means that Python is far and away the best language for data science
and scripting, in my opinion.


## The bad

### Math hacks

To start with, Python's math packages are, well, pretty good. I've never had
problems with their accuracy much, and they do almost anything you could ever
want math packages to do... except for representing infinity sensibly, sensibly
handle numerical errors, and deal with floats in any reasonable manner.

Inifinity is hard in any language, and while i don't like that Python's default
way to use it feels hacky, it does *work* well.

Next, «not a number» (NAN, for some contrived reason capitalized «NaN» in
Python) is not a reasonable way of handling numerical errors.  Firstly, the name
is just plain wrong in many cases: division by zero does not produce «not a
number», it's an undefined operation. It doesn't return anything. While NAN
allows sequential numerical operations to type check before deciding to carry
forward an error that probably represents something pretty bad happening in your
program, it is a pretty poor implementation of, well, anything.

When a program has a divide by zero error, is not terminating appropriate
behavior? Why is something that is «not a number» of type «float»? Does NAN
really help anyone, or just cover up serious programming errors?

NAN is a silent error that allows programs to keep humming away without
terminating when they ought to.

## The ugly

### Speed

Python is just slow. For most applications this doesnt matter. After all, Python
is a scripting language, and for most scripts, time doesnt matter much to the
user. In fact, usually development time does matter, which is why Python is a
great choice in these situations.

But as soon as anyone uses Python for a big project, they find that it takes a
really, really long time to run. It's not even compiled, so if you want to find
an error deep in the program, you'll either have to compile into C-Python
(surely this is overkill for the poor undergrad intern who just wants to debug
their Python cedo?), or run your program and wait.

So speed bites Python in 2 ways -- firstly that it's much slower to debug than
other languages (and hence slower to develop with for big projects); secondly
that its slow during run time, and operations simply take longer to do.

Normally, the way that we would fix both these issues is compilation. But, as a
scirpting language, Python doesn't take advantage of these tools.

### Compilation

Python desperately needs more tools to check the correctness of code prior to
run time. For most languages, we use compilation. In Python, we use between 0
and 10 different tools for type checking and compiling your program into to C,
which is a compiled language, and so makes up for the defects of Python's lack
of compilation.

Worse yet, were some poor programmer to try write a Python compiler, type
annotations are still only optional, and so the writers of most Python packages
dont bother adding them. MyPy is an awful type checking tool. It makes you, the
user, write stub files for your 3rd party packages if they don't exist. And they
very rarely do!

### A language with duck types, but lots of type errors

For a duck-typed language, Python really throws a lot of type errors. Maybe this
is proof that at least a weak type system is desireable?

In the real world, mathematics has a sort of type system: operations are only
defined on certain numbers (for example, division by zero is undefined). I've
never heard of complaints from mathematicians who really wanted to divide a
matrix by a circle.

Python's creators (and many of its users) don't see it this way. The number of
times I have seen type errors, and then had to wonder where on earth this type
error came from, is painful. These are some of the most common errors this
language produces, and the hardest to debug, and also very fixable!

Type checking can and should catch these errors immediately, and would save eons
of time for programmers trying to debug their cloudily typed code.

Even Javascript managed to pull of migrating to a type system -- typescript is
thriving, while type checking in Python seems to have been condemned to the
dustbin of history.

### Community

I wish the community were more proactive in adding new features to Python. It
does happen, but not nearly fast enough. Compare this with JVM languages like
Java and Kotlin, which regularly add new and innovative structures and features
active and better structured communities, like lambda functions, more leniant
syntax changes (like trailing commas), and so on.

Python is slow to add these changes. The community used to be heavily lead by
Guido van Rossum, but I still feel doesn't have the push to change that a lot of
other languages do. At least not right now.

The community is made up by a lot of data scientists and new programmers. This
is totally not a problem! But it means that the discussions about Python lean
towards serving the people who use it. Which is totally fair! But it means that
issues like speed and compilation get thrown under the rug when they wouldn't in
a language like Rust, where the community is dominated by programming nuts.

## Conclusion

I still use Python all the time, but wishing very much I could use something
with better runtime, typing and compilation. For big projects, I generally steer
away from python when I can. Maybe I'd rather use Go or Rust more. But, for now
they have their own problems.
