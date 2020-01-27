#Natural Language Generation

Definition: generate text from non-linguistic input (Data --> Doucuments). Requires knowledge of the **domain** and the **language**.

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200121085336488.png" alt="image-20200121085336488" style="zoom:25%;" />

Usually 3 stages: 

**Document planning**: Content selection, Structure,

**Microplanning**: decide how to linguistically express the text (sentence, words) : lexcical / syntactic choice: 

**Realization**: grammatical details

Prestage: Data analysis : Look for trends and patterns in data.



Multimodel NLG:

- Speech output
- Text and visualizations
  - Produce separately, OR
  - Tight integration: 
    - E.g. text refers to graphic, OR
    - Graphs has text annotations

Building NLG systems:

- Knowledge and corpus analysis, source from

  Imitate a corpus of human-written texts,  Ask domain experts, Experiments with users

- Evaluation

## Document Planning

Goals:

Decide on **text**: what information to communicate (The most important part of NLG !, Also the most domain-dependent aspect)

Decide on **rhetorical structure:** how to structure the information to make a coherent context.

Approachs: 

- Theoretical approach: deep reasoning method based on deep knowledge of user, task, context, etc.
- Pragmatic approach: write schemes which try to imitate human-writen texts in a corpus
- Statistical approach: use learning techniques to learn content rule from a corpus

### Choose content?

#### Theoretical approach

Deduce what the user need to know, and comunicate this

Based on in-depth knowledge:

- User (knowledge, task, etc.)
- Context, domain, word

Use AI reasoning engine:

- e.g. applies logical rules to the knowledge base to deduce new information

Not feasible in practice: 

- Lack knowledge about user
- Lack knowledge of context
- Very hard to maintain knowledge base, e.g. new users, new regulations

#### Statistical Approach

Statistical / learning techniques (including deep learning)

- Parse corpus, align with source data, use machine learning algorithms to learn content selection rules / schemas / cases

Worth considering if large copora available.

#### Pragmatic approach

Analyse corpora texts (after aligning them to data), and manually infer content structure rules. 

Typically based on imitating patterns seen in human-written texts.

- Revised based on user feed back

Specially structure as well as content.

### Text Structure

**Rhetorical relations**: describe how the part of the text  are linked to each other. 修辞关系

The common ones are:

- CONCESSION(although, despite) 让步
- CONTRAST(but, however) 转折
- ELABORATION(usually no cue) 详尽阐述
- EXAMPLE(for example, for instance)
- REASON(because, since)
- SEQUENCE(and, also) 系列

Research community does not agree; many different sets of relations proposed.

We have just looked at one example here, We need to repeat process for at least 20-30 examples, which cover spread of possible cases (including special cases), Merge rules and deal with conflicts: Often caused by different corpus authors writing differently; May give priority to one particular author , and imitate his style.

Creating schemas: 

- usually just writen in as code in Java or other standard programming languages.
- creating schemes is an art, no solid methodology.
- problems:
  - corpus texts likely to be inconsistent
    - especially if several authors wrote texts.
  - Some cases not covered  in the corpus
    - unsuall cases, boundary cases.



**Advanced : User-adaptation**

Texts should depended on:

- user's personality
- user's domain knowledge(how much we need to explain)
- user's vocabulary(can we use techical terms in the text)
- user's task(what does he need to know)

Hard to get this information

**personality and perspectives**

text can communicate perspectives, e.g. 

- smoking is killing you
- if you keep on smoking, your health may keep on going worse
- if you stop smoking, your health is likely to improve
- if you stop smoking, you'll feel better

How to choose between these? 

Depends on personality of reader

- Some people react better to positive messages, others to negative 
- Some react better to short direct messages, others want these weakened.
- Hard to predict

**Conclusion**

Content  determination is the first and most important aspect of NLG(what information should we communicate)

Mostly based on imitating what is obseved in human-written texts(using schemas, writen in Java)

Also decide on structure(tree structure, rhetorical relations)

## Microplanning

Second stage of NLG. Choosing language to express content.

Several sub-tasks:

- lexical choice: which word to use
- reference: how to refer objects
- aggregation: how/when combine phrases into sentence

Problem: There are zillions of ways of expressing a message in words, which one should we use?

Approaches: 

- Theoretical:
  - Define what "best" means, making microplanning choices that optimised it
  - Hard to do in practice because we don't have good models of the effects of choices
- Pragmatic:
  - Imitate corpus: use statistical learning if corpus large enough
  - Problem: sometimes corpus texts may not be very good from a microplanning perspective.

### Lexica choice: 

the task of choosing the right words or lemmas to express the content of the message. (i.e. which word should be used to communicate a concept?)(buy vs sell, ascended vs rose vs surfaced, too fast vs too rapiddly, recommend vs suggest)

Issues that affect lexical choice

- Frequency
- Formality 
- Focus , expectations
- Technical terms
- Convention 

**Statistical-Based Lexical Choice for NLG from Quantitative  Information**

Goal: To develop a staticstical algorithm for lexical choice for quantitative information, which can 

- detect the relationship between data dimensions( aka. attributies) and words
- does not rely on hand-crafted rules
- predict both when and which words should be used
- one word can refer to multiple dimensions

**Methodology**

Each data record consists of attribute-value pairs.

**Representing data in vector**: represent each attribute as a combination of some weighted key-points.

- The key-points are derived by 
  - Taking the min and max values of attribute(from training data)
  - Key-points are evenly spaced between the min and max values
- The number of the key-points for an attribute are fixed

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200121212323798.png" alt="image-20200121212323798" style="zoom:25%;" />

The weight vector of ws = 9 is [0.1, 0.9, 0, 0, 0].

Similarly, a data record( i.e. a set of attribute-value pairs) canbe represented by multiple groups of key-points. 

ws=9 --> [0.1, 0.9, 0, 0, 0]

dir = 2 --> [0.97, 0.03, 0, 0, 0]

 Thus, to present a set of attributes-value pairs, we concatenate the individual weight vectors.

{ws=9,dir=2} -->[0.1, 0.9, 0, 0, 0, 0.97, 0.03, 0, 0, 0]

Then the entire data-text corpus can be represented with avector matrix( **K**), whose row corresponds to the weight vector of a data record.

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200121212954546.png" alt="image-20200121212954546" style="zoom:25%;" />

**Representing word in a vector**

We use a column vector (namely $e_i$) to represent the text of a data record Each element of $e_i$ indicates whether a word appears in the data record.

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200121213313415.png" alt="image-20200121213313415" style="zoom:25%;" />



So far, data are represented by weight vectors, whose values can be calculated using key points.

We represent words in the corpus using the same weight vectors whose values are unknown.

{ws = 9, dir = 2} → v data = [0.1, 0.9, 0, 0, 0, 0.97, 0.03, 0, 0, 0] 

“muggy” → v muggy = [?, ?, ?, ?, ?, ?, ?, ?, ?, ?]

Methodology

**Task**: To estimate $v_i$ for word $i$ given a data-to-text corpus as input.

**Assumption**: $v_i$ and $v_d$ should be close to each other in the vector space if word $i$ appears in data record $d$

$\frac {v_{d1} · v_i} {||v_d1|| \ ||v_i||} = appear(i,d1)$

 $\frac {v_{d2} · v_i} {||v_d2|| \ ||v_i||} = appear(i,d2)$

NB: $appear(i, d1) = 1$ if word $i$ appears in data record $d$ and 0 otherwise

Our task is to find the weight vector $v_i$ for each word $i$, such that the similarity of $v_i$ and $v_d$ is close to $appear(i,d)$ as much as possible for each data record ($d$)

$v_i = \sqrt { \sum _{d}{(sim(v_i,v_d) - appear(i,d))}^2 }$

Finding $v_i$ equivalent to finding the optimal solution the following equation using least squares.

$k^{'} · \frac {v_i} {||v_i||} = e_i$

$opt(\frac {v_i} {||v_i||}) = (k^{'T}k^{'})^{-1}k^{'T}e_i$

Once $v_i$ is solved, we can then estimate the most appropriate words for unseen data.

### Reference

Which phrase should be used to indentify an object?

Referring expression generation: the task of selesting the content(and, to some extent , the form) of referential noun phrases in text.

Types of reference: 

Pronoun - it, them, him, you

Name - Dr Adam Smith, Adam Smith, Adam, Dr Smith

Definite NP: the big black dog, the big dog, the black dog, the dog

Suggestion: 

- Use pronoun if possible
  - Referent mentioned recently  
  - Pronoun is not ambiguous 
- Else use name if possible  
  - Shortest form which is unambiguous and stylistically allowed

- Else use deﬁnite NP
  - Shortest one, prefer basic-level words

- Only use forms seen in corpus

### Aggregation 聚合

Aggregation: the task of merging distinct representations into a single, more concise representation 

When/how should we combine phrases?

Suggestion on Aggregation:

- Generally use the deepest one we can
- Depends on how similar phrases are
- Depends on genre (corpus)

### Conclusion

Microplanning

- Decide how to best express a message in language

  Essential for producing “nice” texts

- Imitating corpus works to some degree, but not perfectly

  Currently more of an art than a science

- Key is better understanding of how linguistic choices aﬀected readers: 

  Our SumTime weather-forecast generator microplans better than human forecasters

## Realisation

Third (last) NLG stage

Creating linear text from (typically) structured input; ensuring syntactic correctness

Take care of details of language

- Syntactic details 句法
- Morphological details 形态
- Presentation details

Problem: There are lots of ﬁnicky details of language which most people developing NLG systems don’t want to worry about

Solution: Automate this using a realiser

### Syntax

Sentences must obey the rules of English grammar

- Speciﬁes which order words should appear in, extra function words, word forms

Many aspects of grammar are somewhat bizarre

Just tell realiser verb, tense, whether negated, and it will ﬁgure out the verb group

- (watch, future) -> will watch
- (watch, past, negated) -> did not watch
- e t c

Similarly automate other “obscure” encodings of informati

### Morphology

In linguistics, morphology is the study of words, how they are formed, and their relationship to other words in the same language. E.g.,

- Variations of a root form of a word, e.g., preﬁxes, suﬃxes

- Inﬂectional morphology - same core meaning
  - plurals, past tense, superlatives, e.g., dog, dogs 
  - part of speech unchanged
- Derivational morphology - change meaning
  - preﬁx re means do again: reheat, resit s
  - suﬃx er means one who: teacher, baker 
  - part of speech changed

**Realiser** 

Calculates morphological variants automatically: (dog, plural) -> dogs; (box, plural) -> boxes; (child, plural) -> children; etc

Automatically insert appropriate punctuation for a structure

Many possible output formats: Simple text HTML MS Word

**Realiser systems**

simpleNLG – relatively limited functionality, but well documented, fast, easy to use, tested

- Most popular, easy-to-use, programmatically controllable and extendable realisation engine.
- Has adapted into many (western) languages: French, German, Mandarin . . .

KPML – lots of functionality but poorly documented, buggy, slow

openCCG – somewhere in between

many more

### Realiser

creates linear text from (typically) structured input; ensuring syntactic correctness

automates the ﬁnicky details of language

- So NLG developer doesn’t have to worry about these
-  One of the advantages of NLG

