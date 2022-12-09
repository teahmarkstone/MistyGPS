
import spacy
from spacy import displacy
from spacy.lang.en import English

NER = spacy.load("en_core_web_sm")


locationDict = {'JCC': ("Joyce Cummings Center", (42.408314813707236, -71.11588341066896)),
               'Cummings': ("Joyce Cummings Center", (42.408314813707236, -71.11588341066896)),
               'Cum Center': ("Joyce Cummings Center",(42.408314813707236, -71.11588341066896)),
               'Joyce': ("Joyce Cummings Center", (42.408314813707236, -71.11588341066896)),
               'SEC': ('Science & Engineering Complex', (42.40615190913599, -71.1166871506011))}



#Command Line Version
def getSpeech():
  return str(input())


# This function uses spaCy's pretrained model and assumes proper capitalization of the sentence
def namedEntityRecognition(userInput):
    recognizedSentence = NER(userInput)

    # Use first entity
    if len(recognizedSentence.ents) != 0:
      locationString = str(recognizedSentence.ents[0])
    else: # if no identity is identified 
      return 'Error'
  
    # remove any leading 'the' from location string
    locationString = locationString.replace('the', "")
    return locationString



# Assume user text is not properly capitalized.
def namedEntityRecognizerNotCap(userInput):
  nlp = English()
  ruler = nlp.add_pipe("entity_ruler")
  patterns = [
              {"label": "FAC", "pattern": [{"LOWER": "joyce"}, {"LOWER": "cummings"}, {"LOWER": "center"}]},
              {"label": "FAC", "pattern": [{"LOWER": "jcc"}]},
              {"label": "FAC", "pattern": [{"LOWER": "campus"},{"LOWER": "center"}]},
              {"label": "FAC", "pattern": [{"LOWER": "science"}, {"LOWER": "and"}, {"LOWER": "engineering"}, {"LOWER": "complex"}]}]
  ruler.add_patterns(patterns)
  doc = nlp(userInput)
  if len(doc.ents) != 0:
    return doc.ents[0]
  else: #if no entity was identified 
    print('Error')
  # print([(ent.text, ent.label_) for ent in doc.ents])
  

if __name__ == '__main__':
    print('Enter speech')
    locationString1 = namedEntityRecognition(getSpeech())
    print(locationString1)
    print('Enter speech')
    locationString2 = namedEntityRecognizerNotCap(getSpeech())
    print(locationString2)

