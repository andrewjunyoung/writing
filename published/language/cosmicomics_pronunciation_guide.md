# Pronouncing character names in Calvino's "Cosmicomics"

#### Hypothesis
Cosmicomics uses a partial *abjad* script like arabic, farsi, and hebrew, where the vowels have to be inferred by context.

In those languages, all consonants are written, while vowels (although not necessarily all vowels) are inferred from context. 
Hieroglyphics is another example of a language like this. When we first learned to read the sounds and meanings of hieroglyphics, we would insert vowels in order to make the text readable, but in doing so also admit that we dodn't know for sure which vowel(s) were meant to be in the word. [1]

[1] We later discovered a direct descendant language of ancient egyption, called *coptic*, which was still spoken in the 1800s, and allowed us to reconstruct the vowels used in ancient egyption with better accuracy, by comparing to similar coptic and arabic words.


For egyptian, we inserted the vowel "e", and would interpret consonants like "y" and "w" to as the long vowels "i" and "u" in some contexts.

This way, if a word ends up mostly unpronouncable, like:
```
Htp-di-nswt wsir xnty imntiw nTr aA nb AbDw wp-wAwt nb tA Dsr
```

we convert "w" → "u", "y" → "i", and insert "e" vowels to make it readable.
```
Hetep-di-nesuet usir xenti imentiu neTer neb AbDu up-wAut neb tA Deser
```

I propose the exact same system for cosmicomics. These aliens eventually became human, so it seems reasonable to assume they had vowels!

Their spelling system may look complex, but is simple and pronounceable, providing you understand the spelling rules we're going to invent here.

So, let's reconstruct how the cosmicomican language may have sounded, using real human languages as a reference point.

## Goals
1. Make cosmicomican pronounceable to most human language speakers
1. Make it apparent that the cosmicomican language is a valid language and culture, rather than gibberish.

## Assumptions
1. The phonology is "average". I don't want it to be like klingon. Therefore I also assume:
  1. Cosmicomicans syllable structure is (C) + (G) + V + (G) + (C) + (G), where:
    - C is a consonant
    - G is a glide (/j/, /w/, /l/, or /r/)
    - V is a vowel
  1. If a letter cluster would be unpronounceable, pick a close, reasonable pronunciation that it would stabilize to. This specifically applies to <uaeau>, as we'll see later.
1. Cosmicomican spellings are inspired by modern human languages. If they wrote a "y", their pronunciation of that letter must be inspired by some human language that used <y> that way.
1. Cosmicomican follows the alphabetical principle, meaning:
  - Every letter has exactly 1 pronunciation
  - Every letter *feature* has exactly 1 pronunciation. For example, superscript ^k should be modified from k the same way that ^p is modified from p.
  - No 2 letters share the same pronunciation in the same position of a word
  - If 2 words are spelled with a different letter, they must have different pronunciation (in linguistics, we say these sounds *contrast*)

# Pronouncing letters

Calvino really hates writing names with vowels. But human languages love vowels (especially the letters <e> and \<a\>). 

This suggests that many of the letters used are already vowels , like <y>; <w>; and <h> [GRC,ARA,HEB].

There are also some consonants which, in english, have difficult pronunciations, but in other languages don't. For example, <x> is pronounced /ks/ in english, but in other languages, just "sh" (/ʃ/) [POR, OSP].

|-------------|-------|------------------------------------------------------|
| Letter      | sound | natural language precedents                          |
|-------------|-------|------------------------------------------------------|
| h           | /i/   | GRC                                                  |
| x           | /ʃ/   | POR, OSP, CMN, MYN                                   |
| X           | /ʒ/   | modified version of <x>                              |
| K           | /x/   | modified version of <k>                              |
| '           | /ə/   | ARAB (alif); HEB                                     |
| w           | /u/   | ARAB; HEB; CYM; EGY                                  |
| y           | /y/   | ARAB; HEB; CYM; EGY                                  |
| _0          | /o/   | looks like an <o>                                    |
| ()          | /^w/  | CYRL uses letter mods and softening letters for this |
| superscript | /^j/  | analagous to <()>                                    |
|-------------|-------|------------------------------------------------------|

# Phonology
## Phonemes

### Consonants

|--------|----------|---------------|-------|-------------|
| labial | alveolar | post alveolar | velar | palatalized |
|--------|----------|---------------|-------|-------------|
|        | n        |               | ŋ     |             |
| p,b    | t,d      |               | k,g   | q           |
| f,v    | s,z      | ʃ,ʒ           | x     |             |
|        | nj       |               |       |             |
|        | tj,dj    |               |       |             |
|        | r        |               |       |             |
|        | l        | (j)           | w     |             |
|--------|----------|---------------|-------|-------------|

### Vowels

Although cosmicomican has a rich vowel inventory, many of these appear not to contrast with each other.

Cosmicomican has 6 distinct vowels, and 1 vowel cluster (diphthong).

|-------|-------|---------|------|
|       | front | central | back |
|-------|-------|---------|------|
| close | i~e   | ɨ~ə     | u    |
| mid   | ɛ     |         | o    |
| open  |       | a       |      |
|-------|-------|---------|------|

|----------|
| /waj.aw/ |
|----------|

We choose that <uaeau> should be pronounced /waj.aw/ because:
- /uaeau/ is hard to pronounce in almost any pronounciation scheme
- inserting glottal stops to make this different syllables is ugly
- cosmicomican shows a love for palindromic words like <XuaeauX>; <Qfwfq>; and <Pfwfp>. Giving these palindromic pronunciations would fit in with cosmicomican cultural practices
- this would be a reasonable sound change to have occured from the sounds these letters actually represent, as follows:
```
<e> no longer appears in isolation, and
\<u\> only appears at the end of words.
/ə.(w)ae/ > /waĕ/ > /waj/
and /a.ə/ > /aʊ/ > /aw/
<ae> as in latin; <au> as in french, english, etc.
```

#### Allophones

There are several allophones, which we can tell because many different letters are used to represent vowels, but certain vowels never appear in the same position as other vowels.

One minimal pairing is as follows:

|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| orthography | broad   | narrow  | translit | 1 | mid | -1 |                                    |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| y           | /i/     | /i/     | i        | - | o   | -  | ENG; latin, french; CYM; ARAB etc. |
| (i)         | /ji/    | /jɪ/    | ji       | - | o   | -  | common                             |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| w           | /j/     | /u/     | u        | - | o   | o  | CYM; ARAB; HEB                     |
| (w)         | /ju/    | /ju/    | ju       | - | o   | -  | derived from <w>                   |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| '           | /ɨ/     | /ɨ/     | y        | - | o   | -  | ARAB (alif); HEB; RUS; UKR         |
| u           | /ə/     | /ə/     | ~y       | o | -   | o  | TUR; ENG                           |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| h           | /e/     | /ɛ/     | e        | o | o   | -  | GRC; RUS; UKR                      |
| e           | /e/     | /e/     | e        | - | -   | o  | common                             |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| Ø           | /a/     | /a/     | a        | - | o   | -  | ARAB; hindi; malayalam; thai; ...  |
| a           | /a/     | /a/     | ~a       | - | -   | o  | common                             |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| \_0         | /o/     | /o/     | ~o       | - | -   | o  | common                             |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|
| uaeau       | /wajaw/ | /wajaw/ | waeaw    | o | -   | o  | see below                          |
|-------------|---------|---------|----------|---|-----|----|------------------------------------|

## Orthography

|----------|--------------------|---------------------------|
| IPA      | script             | examples                  |
|----------|--------------------|---------------------------|
| /n/      | n                  | Zahn                      |
| /ŋ/      | N                  | Ph(i)Nk\_0                |
| /p/      | p                  | Pfwfp                     |
| /b/      | b                  | Bb'b                      |
| /t/      | t                  | Xlthlx                    |
| /d/      | d                  | Vhd Vhd                   |
| /k/      | k                  | Ph(i)Nk\_0; Kgwgk         |
| /g/      | g                  | Kgwgk                     |
| /q/      | q                  | Qfwfq                     |
| /f/      | f                  | Qfwfq; Rwzfs              |
| /v/      | v                  | Vhd Vhd                   |
| /s/      | s                  | Rwzfs                     |
| /z/      | z                  | Rwzfs; Zahn; Z'zu         |
| /x/      | x                  | De XuaeauX; H'x           |
| /ʒ/      | X                  | De XuaeauX                |
| /x/      | K                  | (k)yK                     |
| /n^j/    | ^n                 | G'd(w)^n                  |
| /t^j/    | ^t                 | Pber^t Pber^d             |
| /d^j/    | ^d                 | Pber^t Pber^d             |
| /r/      | r, er              | Pber^t Pber^d; Rwzfs      |
| /l/      | l                  | Lll; Ayl                  |
| /w/      | uaeau; ()          | De XuaeauX; (k)yK         |
| /j/      | uaeau; superscript | De XuaeauX; Pber^t Pber^d |
|----------|--------------------|---------------------------|
| /kw/     | (k)                | (k)yK                     |
|----------|--------------------|---------------------------|
| /wi/     | (i)                | Ph(i)Nk\_0                |
| /wu/     | (w)                | G'd(w)^n                  |
| /u/      | w                  | Qfwfq                     |
| /ɛ/      | h                  | Zahn                      |
| /ɨ/      | '                  | Bb'b                      |
| /i/      | y                  | Ayl                       |
| /e/      | e                  | De XuaeauX                |
| /o/      | \_0                | Ph(i)Nk\_0                |
| /ə/      | u                  | Z'zu                      |
| /a/      | Ø                  | -                         |
|----------|--------------------|---------------------------|
| /waj.aw/ | uaeau              | De XuaeauX                |
|----------|--------------------|---------------------------|

# How to pronounce any name

1. De-capitalize the first letter
1. Convert all the consonants to vowels following the table above, for example <w> → /u/
1. From left to right, insert <a> into the word to make each syllable (CG)V(GCG)

You're done!

If you want things to be even more pronounceable, feel free to mentally transliterate some of the letters. You'll find cosmicomican has a lot in common with slavic languages' phonologies, so let that help you pronounce things!

# Results

|--------------------------|-------------------|-------------------|---------------|
| name                     | IPA (narrow)      | IPA (broad)       | translit      |
|--------------------------|-------------------|-------------------|---------------|
| Qfwfq                    | /qa.fuf.qa/       | /qa.fuf.qa/       | qafufqa       |
| Vhd Vhd, captain and mrs | /vɛd.vɛd/         | /ved.ved/         | ved ved       |
| Xlthlx                   | /ʃal.tɛl.ʃa/      | /ʃal.tel.ʃa/      | xaltelxa      |
| G'd(w)^n                 | /gɨd.wunj/,       | /gəd.wuɲ/,        | gyd'wunj      |
| Granny Bb'b              | /ba.bɨb/          | /ba.bəb/          | babyb         |
| Rwzfs                    | /ruz.fas/         | /ruz.fas/         | ruzfas        |
| Mr. Hnw                  | /ɛ.nu/            | /e.nu/            | enu           |
| Kgwgk                    | /ka.gug.ka/       | /ka.gug.ka/       | kagugka       |
| Mrs. Ph(i)NK\_0          | /pɛ.wɪŋ.xo/       | /pe.wiŋ.ho/       | pewiŋho       |
| De XuaeauX               | /de ʃwaj.awʒ/     | /di ʃwaj.awʒ/     | di xwaeawʒ    |
| Mr. Pber^t Pber^d        | /pa.bɹtj pa.bɹdj/ | /pa.bɹtj pa.bɹdj/ | pabrtj pabrdj |
| The Z'zu Family          | /zɨ.zə/           | /zə.zə/           | zyzy          |
| Ayl                      | /a.il/            | /a.il/            | ail           |
| Pfwfp                    | /pa.fuf.pa/       | /pa.fuf.pa/       | pafufap       |
| Lll                      | /lal.la/          | /lal.la/          | lalla         |
| Dean (k)yK               | /kwik/            | /kwik/            | kwik          |
| Zahn                     | /za.ɛn/           | /za.en/           | zaen          |
| Ursula H'x               | /ɛ.ɨʃ/            | /e.əʃ/            | eyx           |
|--------------------------|-------------------|-------------------|---------------|
| Father                   |                   |                   |               |
| Mother                   |                   |                   |               |
| Aunt and Uncles          |                   |                   |               |
| The Cleaning Woman       |                   |                   |               |
| Fern-flower              |                   |                   |               |
| The Half-Breed           |                   |                   |               |
| Narrator                 |                   |                   |               |
| The Deaf One             |                   |                   |               |
| Lieutenant Fenimore      |                   |                   |               |
| Narrator                 |                   |                   |               |
|--------------------------|-------------------|-------------------|---------------|
