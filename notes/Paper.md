1. a) In the context of Information Retrieval, explain the diﬀerence between algorithms that perform boolean search and algorithms that perform a ranked search. What type of algorithm would be better for a regular user (such as an undergraduate student in the Humanities area) who is using a search query with multiple terms, which he/she expects to appear in many documents? Explain the reasons behind your choice of algorithm type. 

   Boolean search:

   - Binary decision: is document relavant or not
   - Presence of term is necessasy and sufficient for match
   - Boolean operation is set of operators(AND, OR)

   Ranked algorithm:

   - Frequency of document terms
   - not all search terms necessarily present in document
   - Incarcerations: 
     - The Vector Space Model
     - The probabilistic model
     - Web Search Engines

   d) Assume we have a small set of seed words with positive and negative opinions, e.g.:positive = {good, fast, cheap} and negative = {slow, boring, fragile}. Explain the two most common (semi-)automated approaches to expand these sets with more opinion words or phrases to create lexica for Sentiment Analysis, providing examples whenever possible. Give one advantage and one disadvantage of each approach. [20%]