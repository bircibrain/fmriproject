# Reference
Zhuang, J., & Devereux, B. J. (2017). Phonological and syntactic competition effects in spoken word recognition: evidence from corpus-based statistics. Language, Cognition and Neuroscience, 32(2), 221–235. http://doi.org/10.1080/23273798.2016.1241886

# Research Question
* How may different kinds of linguistic competition in spoken language be modulated by the presence or absence of a prior context?

# Findings
* Lexico-phonological competition associated with LIFG activation for words in isolation, but not in phrases
  - phrasal contexts reduce lexico-phonological competition by eliminating form-class inconsistent cohort candidates
* Lexico-syntactic competition associated with LIFG activation for verbs in phrases, but not in isolation
  - lexico-syntactic infrmation is boosted by the phrasal context
* LIFG serves a general purpose in resolving linguistic competition

# Methods
## Design and Stimuli
* event-related design
* task: auditory lexical decision task
* conditions: words presented in isolated stems (e.g., "examine") vs. in phrases ("you examine")
* 160 nouns and 160 verbs
  - matched in imageability, frequency, number of syllables, and number of phonemes
  - all are form-class-unambiguous
  - half of the stimuli are presented as isolated stems, half are presented in phrases
  - in phrases:
    + three articles ("a", "the", "this")
    + three pronouns ("I", "they", "you")
* 320 non-word fillers
* two baseline conditions
  - 80 null events (silence)
  - 280 items of envelope-shaped musical rain (MuR; pitch judgement on low vs. high)
* measurement for competition
  - lexico-phonological competition for all words: cohort size (i.e., total number of words sharing the fist two phonemes with the target word based on CELEX database)
  - lexico-syntactic competition for verbs: entropy (i.e., the possibility of a verb occuring in different subcategorization frames based on VALEX database)

## MRI Acquisition and Analysis
* fast sparse imaging protocol (1.4 seconds of silence between scans; 100ms gap between end of scan and following stimuli)
* Analysis 1:
  - design matrix events: isolated words, word phrases, non-words, MuR, null
  - parametric modulation of stimulus duration, word frequency, cohort size
* Analysis 2:
  - design matrix events: isolated verbs, verb phrases, nouns, non-words, MuR, null
  - parametric modulation of stimulus duration, word frequency, syntatic competition (entropy)
* apply bilateral fronto-temporo-parietal mask at group level analysis
* ROI analysis on LIFG, RIFG, LSTG, LMTG