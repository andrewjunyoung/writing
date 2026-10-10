Time in softwaer is a messy affair.

In the present, we need to deal with time zones, which don't have consistent
naming conventions, change, and not even change on the same day in all places.
Managing the complexity of time zones alone is unbelievably hard, as any
programmer who has tried to work with them will know.

In the future, we will need to find a way of keeping time on the moon and mars,
at least. Mars has 2 moons, not one, which have different phases. Some moons
have no phases. A year on mars is also longer than one on earth.

These problems aren't ideas that are 10,000 years in the future, they're ideas
that are happening now. we already have sent people to the moon, and have robots
on Mars. We need long term thinking to give a long term fix for these problems.

We do already have a fix for these problems: UNIX time. UNIX time is a
seconds-based counter from "epoch", defined to be 1970 January 1, at 00:00. The
arbitrariness of epoch time is not important (much like the arbitrariness of the
year 1), but is essential to be agreed upon. After this, we just count how many
seconds we are before or after epoch. This doesn't need to be seconds. Any scale
will do, providing its standardized, and ideally easy to use (that is,
decimalized).

In the scales of the universe which we will encounter in the next 10,000 years,
it seems that epoch time is a good absolute measure of the passage of time, and
can be used on earth and mars alike. But, it's not easy for humans to use, or to
understand.

Because of this, we have already been using 2 systems in parallel. While UNIX
time runs our computers, and governs absolute time as we know it, our calendars
are a human-friendly way of understanding our position in time, and where we're
going next. From these human-friendly calendars, like the gregorian calendar, we
can track years; days; and weeks: the fundamental building blocks of our
society.

At this point, we want to design an interface that will make sense on any
planet, so that a robot in mars can reasonably get a human on earth to
understand its situation. All this needs is years and days. Some planets have
many moons, and many moons have no phases. Planets do have differently lengthed
years and days, but these constants can be easily stored and referenced, and
they change very slowly.

This means that no matter what planet we're on, we can show time as:

YYYY a DDD d SSSSS s (eg. 2018 a 289 d 10,851 s)

Why no hours? We want to show a planet's time of day as where the sun's position
in the sky. If we define an hour as 3,600 s, then the idea of "noon" is
different on each planet. This is harder. If we define an hour as 1 / 24 of a
day, then hours are different lengths. This too is harder.

Under this system, all we need to know is

YYYY a DDD d SSSSS s

That is, how many years have gone by on that planet since epoch; ¿how many days
have gone by since the start the current year (its shortest day)?; ¿Out of how
many days?; ¿how many seconds into that day are we? ¿out of how many seconds per
day?

This also allows us to quickly determine the day of the week: simply take the
day of the year d and calculate d (mod 7).

If we're on a moon, we don't usually track seasons in the same way, because
these are determined both by the body we're orbiting and by the nearest star. In
this case, a year is most usefully represented to mean orbits around the local
planet. Hence, the year on the moon since epoch will be just over 13 times the
year since epoch on Earth, but this is what we want to see, because it helps us
better understand the conditions of the planet or rock which we're on.

And of course, our universal time is holding it all together.
