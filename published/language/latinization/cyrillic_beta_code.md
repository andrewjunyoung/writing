# Cyrillic beta code

## Abstract

Beta code is a method of representing characters and formatting of texts written
in the ancient greek alphabet. Beta code is useful for transcribing the letters
of greek almost 1:1 into the latin alpbabet, and is used by the Perseus projet
to record ancient greek material as it was written originally.

This system has several other benefits:
  - *Transcription*: It gives an intuitive unique transcription from modern greek into latin
  - *Keyboard input*: It provides an intuivite key map for inputting polytonic
  greek letters on a latin keyboard
  - *Conversion*: Beta code can easily be converted to and from other encoding
  methods (EG unicode) because it is an injective map.

Cyrillic would doubtlessly benefit from the same type of transcription.

We present a beta code for cyrillic which takes inspiration from the writing
conventions used latinized slavic languages, and standardized in ISO 9. Cyrillic
beta code provides the same benefits of transcription; keyboard input; and
conversion with the latin script.

The current application of cyrillic beta code is in keyboard input. We apply
this convention in «Symboard» to design a cyrillic input layer using the
Cyrillic beta code convention.

## Background

### Modern cyrillic to latin transcription

Cyrillic, latin, and modern greek all derive from the ancient greek script, and
have similar typography rules in print and in handwriting (this makes them
potential candidates for script unification).

Slavic languages are split between those that use the cyrillic script (EG
Russian, ukrainian, bulgarian), and those that use the latin script (EG czech,
polish, and slovenian) [^1]. The writing systems of latin slavic languages is
mostly consistent. These practices are therefore very common when latinizing
slavic languages which use the cyrillic script. For example, in czech and all
south slavic languages, «c» is written for /ts/, and «č» for /tʃ/. Hence, «ц» is
usually transcribed as «c»; and «ч» as «č».

These practices are standardized in ISO 9, which provides comprehensive
transcription of every cyrillic letter into the latin alpabet, using diacritics
to give every cyrillic letter exactly 1 latin equivalent (with diacritics).

ISO 9 is only one out of many transcription systems used for russian, though it
is one of the most popular, logical, and consistent, and maintains writing
conventions common in other slavic languages.

### Influences

Cyrillic beta code is inspired by the following sources:
  - Czech (Jan Hus' czech alphabet)
  - South slavic writing systems (Gaj's latin alphabet) [^2].
  - ISO 9 [^3].

In order to make cyrillic beta code easy to learn and use, we try to maintain
the conventions of ISO 9. This hopes to reduce the amount the user has to learn
to use it, and to maintain some of the logical conventions used in ISO 9.

Where possible, we use the same base letters as ISO 9. When ISO 9 has a
diacritic attached to the base letter, we encode this as a second, separate
letter.

### Limited scope

Cyrillic beta code is not comprehensive: it does not encode every letter used in
modern cyrillic alphabets into a single latin script character. It only encodes
letters used in slavic alphabets which are «sufficiently grahically unique» or
«sufficiently important».

#### Why scope is limited

1. *It is impossible to encode all cyrillic letters into a unique latin script
   character without diacritics.* There are 51 cyrillic letters used in slavic
   scripts. There are 26 in the ISO basic latin alphabet. Even if we also use
   numbers 0-9, that only 36 letters. Even if we use every key on the ISO (or
   ansi) keyboard, that still only adds up to 48 (or 47 for ansi). We cant
   put all slavic letters on the same keyboard, let alone encode them into an
   alphabet with far fewer letters.
2. *Not all slavic letters are grahically unique.* Many letters, such as «Ё» and
   «Ѓ» are very clearly just other cyrillic letters with accent marks slapped
   over them («Е» and «Г» respectively, in this case). Why bother making a map
   without diacritics if slavic alphabets use diacritics all the time themselves?!

#### What the scope is

We therefore only want to encode slavic letters which are _unique_, and _do not make
use of diacritics_. We make one, notable exception: «Й», which is used in
Russian, and generally not considered interchangeable with «И» [^j vs ë].

Encoding russian fully is particularly important. Russian has an estimated 260
M speakers (of which 150 M are native speakers). Slavic languages are estimated
to have 315 M speakers at the turn of the 20 th century. This makes native
russian speakers around half of all slavic language speakers, and russian by far
the most spoken slavic language: around 83 % of all slavic speakers speak
russian.

The scope therefore covers 41 letters:

А; Б; В; Г; Д; Ђ; Е; Є; Ж; З; Ѕ; И; І; Й; Ј; К; Л; Љ; М; Н; Њ; О; П; Р; С; Т; Ћ;
У; Ф; Х; Ц; Ч; Ю; Я; Џ; Ш; Щ; Ъ; Ы; Ь; Э

#### Understanding ISO 9

I wont write pages of praise for ISO 9 (though I think it's well deserving).
This section should help clarify the logic of ISO 9, and act as a short user
guide for learning ISO 9 and cyrillic beta code.

In general, the caret (ˆ) and hacek (ˇ) provide most of the modifications needed
for the basic cyrillic alphabet.

##### Hacek (ˇ)

###### Palatization

On a consonant, The hacek is used to represent palatalization. This follows
czech and south slavic convention.
  - z (/z/) → ž (zh, /ʒ/)
  - s (/s/) -> š (sh, //)
  - c (/ts/) -> č (ch, //)

###### Graphical similarity

When a similar looking and sounding letter is already being used, a caret is
used to disambiguate.
  - «ǰ» for cyrillic «ј» («J» is already used for «Й»)
  - «Ì» for cyrillic «I» («I» is already used for «И»)

##### Caret (ˆ)

###### Palatization

On a vowel, it is sometimes used to represent palatization _before_ the vowel.
  - a → â (ja, /ja/)
  - u → û (ju, /ju/)
  - e → ê (je, /je/)

It is used to represent slavic letters which are combined with the soft sign
(Ь), including «Њ» and «Љ». These represent palatalized consonants.
  - l (/l/) -> l̂ (/lj/)
  - n (/n/) -> n̂ (like spanish ñ, //)
  - d (/d/) -> d̂ (dzh, /dʒ/)

###### Upper case

We also use the caret alongside the hard and soft sign to represent upper case.
Upper case hard and soft signs are not encoded in ISO 9.
  - «'» represents cyrillic «ь»
  - «^'» represents cyrillic «Ь»
  - «"» represents cyrillic «ъ»
  - «^"» represents cyrillic «Ъ»

#### Others

Letters which do not easily fall into the above categories are:
- «Ð» for cyrillic «ђ» («Ð» is standard in latinized serbo-croat, hence ISO 9 also uses it)
- «Ć» for cyrillic «ћ» («Ć» is standard in latinized serbo-croat, hence ISO 9 also uses it)
- «Ẑ» for cyrillic «S»
- «Ŝ» for cyrillic «щ»

## Results (Cyrillic beta code table)

### Table

| Index | Cyrillic letter | Latin transcription | ISO 9 |
|-------|-----------------|---------------------|-------|
| 00    | А а             | A  a                | A a   |
| 01    | Б б             | V  v                | V v   |
| 02    | В в             | B  b                | B b   |
| 03    | Г г             | G  g                | G g   |
| 04    | Д д             | D  d                | D d   |
| 05    | Ђ ђ             | -D -d               | Ð ð   |
| 06    | Е е             | E  e                | E e   |
| 07    | Є є             | ^E ^e               | Ê ê   |
| 08    | Ж ж             | vZ vz               | Ž ž   |
| 09    | З з             | Z  z                | Z z   |
| 10    | Ѕ ѕ             | ^Z ^z               | Ẑ ẑ   |
| 11    | И и             | I  i                | I i   |
| 12    | І і             | -I -i               | Ì ì   |
| 13    | Й й             | J  j                | J j   |
| 14    | Ј ј             | vJ vj               | ǰ ǰ   |
| 15    | К к             | K  k                | K k   |
| 16    | Л л             | L  l                | L l   |
| 17    | Љ љ             | ^L ^l               | L̂ l̂   |
| 18    | М м             | M  m                | M m   |
| 19    | Н н             | N  n                | N n   |
| 20    | Њ њ             | ^N ^n               | N̂ n̂   |
| 21    | О о             | O  o                | O o   |
| 22    | П п             | P  p                | P p   |
| 23    | Р р             | R  r                | R r   |
| 24    | С с             | S  s                | S s   |
| 25    | Т т             | T  t                | T t   |
| 26    | Ћ ћ             | -C -c               | Ć ć   |
| 27    | У у             | U  u                | U u   |
| 28    | Ф ф             | F  f                | F f   |
| 29    | Х х             | H  h                | H h   |
| 30    | Ц ц             | C  c                | C c   |
| 31    | Ч ч             | vC vc               | Č č   |
| 32    | Ю ю             | ^U ^u               | Û û   |
| 33    | Я я             | ^A ^a               | Â â   |
| 34    | Џ џ             | ^D ^d               | D̂ d̂   |
| 35    | Ш ш             | vS vs               | Š š   |
| 36    | Щ щ             | ^S ^s               | Ŝ ŝ   |
| 37    | Ъ ъ             | ^"  "               | ^" "  |
| 38    | Ы ы             | Y  y                | Y y   |
| 39    | Ь ь             | ^'  '               | ^' '  |
| 40    | Э э             | -E -e               | È è   |

### Discussion of results

#### Use of diacritics

ISO 9 uses the following 5 diacritics to transcribe these 40 characters:
  - Caret (ˆ)
  - Hacek (ˇ)
  - Macron (¯)
  - Acute accent (´)
  - Grave accent (\`)

Note that in this character set, we can simplify this system to 3 diacritics:
  - Caret (written as «^»)
  - Hacek (written as «v»)
  - Macron / acute accent / grave accent (written as «-»)

This provides the basis for our transcription system.

After that, the rule simply follows: put the character that represents the
diacritic before the alphabetical character (for example: «^s», not «s^»).

#### Hard sign and soft sign

The soft sign and hard sign generally cant appear at the front of words, as per
orthography rules. Although they have capital forms, these only appear as part
of words written in all caps. It is usually sufficient to write these
case-insentitively, and infer from context.

In order to provide the possibility for upper case forms of these letters, we
allow them to be combined with the caret, which will produce the upper case form
of the hard and soft signs.

#### Use of digraphs

We use digraphs to create 41 distinct letters, but we easily could have chosen
to use individual characters, if we used the latin script's 36 alphanumeric
letters, plus punctuation [^case and number of chars]. This is few enough to fit
on a keyboad, but would require a user to memorize around 30 arbitrarily chosen
symbols and punctuation -- a pain.

If a user doesnt know where a character is in our keyboard, they can usually
guess well. If a user doesnt know what a symbol maps to in the above case, they
may be searching painfully for a while -- on average 15 guesses.

Under the ISO system, if a user has any knowledge of other slavic languages it
is a huge help in learning and using cyrillic beta code. Consider the above
example again. A user doesn't know how to type a letter. With knowledge of
jther slavic languages and basic knowledge of ISO 9, they can most likely guess
it in under 3 random guesses (by trying each of the diacritics).

Exceptions to this rule (such as Ð and Ẑ) are rare, and the sound values they
represent are not rare for the letters used to represent them -- using english
examples: «Ð» as in «Django»; «Ẑ» as in «Pizza».

## Foot-notes

[^1]: Note that there are slavic languages which use more than one script and do
  not fall neatly into our categories. Croatia speaks serbo-croat and uses the
  latin script, while serbia (also serbo-croat speakers) use both the latin and
  cyrillic script interchangeably.
[^2]: Gaj's latin alphabet is inspired by and based on Jan Hus' czech alphabet.
[^3]: ISO 9 is based on the conventions used in south slavic languages and
  czech.
[^j vs ë]: Russian does have one other widely used character with a diacritic:
  «ё» (yo). But, yo is widely and readily interchanged with e by many speakers
  and publications. «й» (i kratkoe) is rarely interchanged with «и» (i).
[^case and number of chars]: Due to upper and lower case character forms, we
  would need to use the 26 × 2 letters of the alphabet, 10 alphanumeric letters,
  and 20 punctuation symbols (26 × 2 + 10 + 20 = 41 × 2 = 82).
