# ChatBot
## Cornell Movie Dataset
 The datset from cornell will be used to build seq2seq model on keras. We only need 2 files from this dataset for our ChatBot.

 The dataset can be downloaded from the link: https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
 These are:

#### movie_lines.txt
- contains the actual text of each utterance
- fields:
  - lineID
  - characterID (who uttered this phrase)
  - movieID
  - character name
  - text of the utterance

#### movie_conversations.txt
- the structure of the conversations
- fields
  - characterID of the first character involved in the conversation
  - characterID of the second character involved in the conversation
  - movieID of the movie in which the conversation occurred
  - list of the utterances that make the conversation, in chronological
    order: ['lineID1','lineID2',É,'lineIDN']
    has to be matched with movie_lines.txt to reconstruct the actual content
