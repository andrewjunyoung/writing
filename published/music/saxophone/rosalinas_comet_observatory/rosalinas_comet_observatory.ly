version "2.23.11"

\header {
  title = "Rosalina's comet observatory"
  subtitle = "from \"Super Mario Galaxy\""
  composer = "Andrew J. Young"
  tagline = #f
}

{
  \key b \major
  ^ \markup {
    \column { \italic jazzy }
  }

  \bar ".|:"

  \repeat volta 2 {

    | dis'8 fis'4 dis''2 ais'8
      cis''4. b'2 g'8
      ais'4. gis'2 \appoggiatura ais'4. b'4
    | b1

    | \acciaccatura ais'8 b'4. ais'4. dis'4
    | \acciaccatura ais'8 b'4. ais'4. dis'4
    | \acciaccatura fis'8 gis'4. eis'4 gis'4
    | fis'1

    \break

    | dis'8 fis'4 dis''2 ais'8
      cis''4. b'2 g'8
      gis'8 b'4 fis''2 b'8
      fis''4. e''8~ e''2
    | e''4. dis''4. fis'4
    | dis''4. cis''4. ais'4
    | b'1~
    | b'1

    \fine

    \break

    \sectionLabel "Bridge"

    | fis''2~ fis''8 b'8 dis''4 fis''2~ fis''8 fis''8 ais''4 fis''1 b'1

    | gis'1
    | ais'1
    | b'1
    | cis''1

  }
}

.    .. |.    .. |.       |.
4~  884  4~  884  4        4
# 1
# 2

ABCABCAB
