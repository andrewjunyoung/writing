package main

import (
  "encoding/csv"
  "fmt"
  "os"
  "io/ioutil"
  "regexp"
)

// A record for mapping from one unicode string to another (IE transcribing).
type HonjiRecord struct {
  From string // IPA symbols may not be single unicode characters.
  To   string // Their mappings certainly aren't always single characters.
}

type HonjiScheme struct {
  Records []HonjiRecord // The list of records in the scheme
}

func (scheme HonjiScheme) Transcribe(text string) string {
  fmt.Println(scheme.Records)
  for _, record := range scheme.Records {
    // There's obviously faster ways to do this, but early optimization is the
    // root of all evil, so I'm leaving it like this till the need arises to
    // change it.

    // Go through all the rules in the scheme and apply them one by one to the
    // regex, in the order they exist.
    re := regexp.MustCompile(record.From)
    text = re.ReplaceAllString(text, record.To)
  }
  return text
}

func getHonjiScheme(data [][]string) HonjiScheme {
  // TODO: There's got to be a nicer way to do this.
  var scheme HonjiScheme
  for i, line := range data {
    if i > 0 { // Omit header line.
      var record HonjiRecord
      record.From = line[0]
      record.To = line[4]
      scheme.Records = append(scheme.Records, record)
    }
  }
  return scheme
}

func main() {
  const TranscribeSchemePath = "transcribe.csv"
  const TargetPath = "target.txt"

  // Try to open the CSV
  f, err := os.Open(TranscribeSchemePath)
  if err != nil {
    f.Close()
    os.Exit(1)
  }

  // Try to parse the CSV
  csvReader := csv.NewReader(f)
  data, err := csvReader.ReadAll()
  if err != nil {
    f.Close()
    os.Exit(2)
  }

  // Convert the CSV data into a transcription scheme.
  scheme := getHonjiScheme(data)

  // Try to open the target file
  targetText, err := ioutil.ReadFile(TargetPath)
  if err != nil {
    os.Exit(3)
  }

  transcribedText := scheme.Transcribe(string(targetText))

  // Print the transcription scheme.
  fmt.Println(transcribedText)
}
