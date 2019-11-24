# Symbols for unclear phonemes in The International Phonetic Alphabet
Author: Andrew Jun Young

# Abstract
This short article proposes the addition of \<?\>, an unknown sound quality
marker, and various elements adopted from regular expressions (RE) which widen
the ability of the IPA to transcript sounds when there is uncertainty (either
through approximation or uncertainty of accuracy) in a sound's phonemic value.

We propose the use of \<?\> to indicate an uncertain sound, \<¿\> and \<?\> to bracket
uncertain sections, \<<sup>?</sup>\> to indicate that the preceeding phoneme is
uncertain. This can be used alongside other generalized symbols such as \<C\> and
\<V\> for consonants and vowels; \<?+\> to match with at least one uncertain
phoneme; and \<?\*\> to match with any number of uncertain phonemes.

# Introduction

We propose \<?\> to represent an indiscernable, unclear, or approximated phoneme
in transcription. This fills a gap in linguistics for describing uncertainty in
reconstructed historical pronunciations, and in transcription of speech into IPA
symbols. The ideas of this paper take partial inspiration from uncertainty
symbols used in the Uralic Phonetic Alphabet. Linguistically we propose it be
referred to as an \<uncertain phoneme\>.

By \<uncertainty\>, we mean that the true value of phoneme(s) are unknown,
partially known, unknowable, or approximated.

We propose the use of \<?\> to indicate an uncertain sound, and \<<sup>?</sup>\> to
indicate that the preceeding phoneme is uncertain. This can be used alongside
other generalized symbols such as \<C\> and \<V\> for consonants and vowels; \<?+\> to
match with at least one uncertain phoneme; and \<?\*\> to match with any number of
uncertain phonemes.

Similarly, using \<¿(\*)?\> indicates that the entire passage of (\*) is
uncertain.

# Applications

These symbols find many uses in fields of linguistics where sounds are
reconstructed, as this causes uncertainty. In historical reconstructions, this
is often the case, and so use of the question mark reflects this uncertainty.

It is also highly useful in real transliterations of human speech, as sound values are
often unclear in real scenarios, such as those with poor sound quality. Another
way in which this can me used is to mark when certain qualities of a phoneme are
known while others are not, including its exact value. For example, when a
phoneme is only known to be some vowel, it can be denoted by \<V<sup>?</sup>\>

Consider the following example:

| English phrase                                    | IPA transcription                                                      |
|---------------------------------------------------|------------------------------------------------------------------------|
| He took five ships down to the river this morning | hi: tʊk faɪv ʃi¿CC? dɑʊn tu: ðə rɪ.vɜ: ðV<sup>?</sup>? mɔ:.nɪn<sup>?</sup> |

The implication of this passage is that we do not know which 2 consonants we
heard in \<ships\>, or the final consonant of \<morning\>. We do know
that we heard consonants, but we can't discern what they are. Finally, we do not
know for sure what the last sound in \<morning\> was, but we believe it was
[n] as opposed to say, [ŋ].

We also indicate that we heard a vowel in \<this\> following [ð] but cannot
discern which vowel, and that we cannot discern what the final sound we heard in
this word was at all.
