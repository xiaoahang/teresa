# Sentiment Analysis 

## Basic Definations and Problems

**General goal**: Extract opinions, sentiments and emotions express by hummans in texts and use this information for business, intelligence, etc. purposes. Can't be done manually because of huge volume optionated text.

**Applications**:

- Product review mining
- Review classification
- Tracking sentiments towards topics over time
- Prediction (elction outcomes, market trends)

**Motivatons**
- objective Sentence
- Positive and negativte opinions about what?
- Targets of opinions
- Holders of opinions

**Definitions**:

- Current text processing methods (e.g., web search, information extraction) work with factual information.
- Current search ranking strategy not appropriate for opinion retrieval.
- Sentiment analysis focuses on **subjective statements - opinions, sentiments, emotions**: hard to express with a few keywords.

**Step of sentiment analysis** : 

- Subjectivity classification 

- Target objects: Product, person, event, organization, or topic. It is represented as

  - A hierarchy of components, sub-components 
  - Each node represent a component and has a set of attributes.

  <img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120152945657.png" alt="image-20200120152945657" style="zoom:23%;" />

  An opionion can be expressed on a component of attribute of the component - call them "feature"s of the objects. 

###  Bing Liu's model: 

An opinion is a quintuple ($o_ j , f_jk , so_ijkl , h_i , t_l$ ), where

  - $o_j$ is a target object.

  - $f_jk$ is a feature of the object $o_j$ .

  - $so_ijkl$ is the sentiment value of the opinion of the

  - opinion holder $h_i$ (usually the author of the post) 

  - on feature $f_jk$ of object $o_j$ at time $t_l$ .

    $so_ijkl$ is positive, negative, neutral, or a more granular rating, such as 1-5 stars as in movie reviews.
    


The task of opinion mining : 

- Discover all quintuples  ($o_ j , f_jk , so_ijkl , h_i , t_l$ ), or
- Discover some of these components

With that, one structure the unstructured.

### Granularity level: 粒度

**Document level**: classify a document based on the overall sentiment expressed by opinion holder into, e.g. positive or negative or neutral. 

- Assumption: Each document focuses on a single object and contains opinions from a single opinion holder($o_ j , f_jk , so_ijkl , h_i , t_l$ ),  where $o_j = f_jk$

**Sentence level:** idem, but for (subjective) sentences, so these need to be identified first.

**Feature level**: documents and sentences may contain mixed opinions and analysis at this level does not identify speciﬁcally what people like/dislike.

Feature level steps:

- indentify and extract objective features that have been commented on by opinion holder
- determine whether the opinions on the features are positive, negative or neutral
- group synonym features
- Optional: produce a feature-based opinion sumary of multiple reviews( thus we can do comparesion between different targets)

### Challenges 

($o_ j , f_jk , so_ijkl , h_i , t_l$ )
- $o_j$ is a target object. : **Named Entities Recognition** (well-known tools based on gazetteers and simple context rules) / **Bootstrap from seed gazetteers** 
- $f_jk$ is a feature of the object $o_j$ .  : **Information Extraction**
- $so_ijkl$ is the sentiment about  $f_jk$  : **Sentiment Determination**
- $h_i$ : opinion holder  : **Information (or metadata) Extraction**
- $t_l$ . : **Information (or metadata) Extraction**

Addtion challenges

- **Co-reference resolution** : Is important to resolve objects and features
- **Relation extraction**
- **Synonym match** (“voice” = “sound quality”)



## Sentiment analysis Approaches

  - Lexicon-based: use a lexicon of opinion/emotion words, like : good, bad, horrible, great, etc
    - Binary
    - Gradable 
  - Corpus-based/ Supervised learning
### Lexicon-based approach

Use a lexicon of opinion/emtion words, like: good, bad, horrible, great, etc.

####Lexicon-based approach : Binary

Rule-based sentiment classifier **(Sentence/ document level)**

- Rule-based subjectivity classifier: a sentence/document is subjective if it has at least n( say 2) words from the emotion words lexicon.
- Rule-based sentiment classifier: for sujective sentences / documents, count positive. and negative words/phrases in the sentence/document.  If more negative than positive words/phrases, then negative; otherwise, positive; if equal , neutral.

Rule-based sentiment classifier **(Feature-level)**

- Assume features can be identified in previous step by information extracation techniques.
- For each feature,count positive. and negative words/phrases from the lexicon.
-  than positive words/phrases, then negative; otherwise, positive; if equal, neutral.
- simple approach 
  - Input: a pair $(f, s)$, where $f$ is a feature, and $s$ is a sentence contains $f$.
  - Output: $f$ is positive? Negative? Neutral?
  - Step1: work on the sentence $s$ containing $f$
  - Step2: select emotion words in $s$ : $w_{1}, w_{2},...,w_{n}$
  - Step3: assign orientations for these emotion words: 1=positive, -1 = negative, 0=neutral
  - Step4: sum up the orientation and assign the orientation to $(f, s)$ accordingly.

More advanced approaches split the sentence in parts, e.g. based on BUT words.

Caveats : need more fined-grained sentiment information 
- Context-independent 
- Context-dependent
- Negation
- Intensifiers

#### Lexicon-based approach: Gradable
Use ranges of sentiment (to deal with intensifiers)
-  like absolutely, utterly, totally, nearly, virtually, mainly, almost)

And grading adverbs 

- (Very, little, dreadful, extremely, fairly, hugely, immensely, intensely, rather, reasonably, slightly, unusually)

Rule-based gradable sentiment classifiers
- Classifiers general valence of a text(document-,sentence- or feature-level) based on the level of emotional content
- Level of emotional contents given by 
  - The lexicon: word-lists wirh pre-assigned emotional weights
  - Additional general rules to the original weight,   AS FOLLOWS: 

**Negation rule:**  否定词

- positive: -1, *-1
- negative: +1, *-1

**Captalization rule** 大写

- positive: +1
- negative: -1

**Intensifiers rule** 强调成分

- needs a list of intensifiers: 
- Each initensifiers has a weight
- the weight is added to positive words/ sustracted from negative words

**Diminisher rule:** 减少成分

- needs a list of diminishers:
- Weight:
- the weight is substracted to positive words/ added from negative words

**Exclamation rule**:  !!! 感叹号 Fuctions like intensifiers

**Emoticon rule** :小表情 Each has its own emotional weight, like an emtional word.

Final decision based on Allemotion words:
- if $|C_pos| > |C_neg|$ then ${positive}$
- if $|C_pos| < |C_neg|$ then ${neagative}$
- if $|C_pos| == |C_neg|$ then ${neutral}$

#### Advantages and Disadvantages of Lexicon-based approach
- Advantages 
  - Works eﬀectively with diﬀerent texts: forums, blogs, etc.
  - Language independent - as long as an up-to-date lexicon of emotion words is available 
  - Doesn’t require data for training 
  - Can be extended with additional lexica, e.g. for new emotion words/symbols as they become popular, esp. in social media
- Disadvantages:
  - Requires a lexicon of emotion words, which should be fairly comprehensive, covering new words, abbreviations (LOL, m8, etc.), misspelled words, etc.

#### Lexica of emotion words/phrases

How to obtain? 

*Adjectives, Verbs, Nouns, Phrases* 

Task: Collect relavant words/ phrases that can be used to express sentiment.Determine the emotion.

- **Manully**: word lists with pre-assigned emotional weights
  - Created resources: SentiWordNet, Linguistic Inquiry and Word Count (LIWC) Lexicon, General Inquirer.
- **Semi-automaticaly**: 
  - **Dictionary-based**: ﬁnd synonyms/antonyms of seed emotion words in dictionaries like WordNet
  - **Corpus-based**: ﬁnd synonyms/antonyms of seed emotion words in corpora
- Start with **seed positive and negative words**
- **Search** for synonyms/ antonyms in **dictionaries** like WordNet 
- or **Build patterns** from **seed** words/phrases tp search on large **corpora**

Manually created resources, such as:

- **SentiWordNet**: Wordnet is a database with words grouped into sets of synonyms (synsets), and organised by semantic relations between them: synonyms, antonyms, hypernyms, etc. SentiWordNet is a version of it with one of three sentiment scores for each synset: positivity, negativity, objectivity.
- **Linguistic Inquiry and Word Count (LIWC) lexicon**: made by psychologists with lists of words with various emotional and other dimensions.
- **General Inquirer**: terms with various types of positive or negative semantic orientation.

### A corpus-based approach to SA

Idea: Mostly “**supervised learning**”: **corpora** of examples **annotated with sentiment** are used with machine learning algorithms to learn a classiﬁer for each sentence/document. 

Corpora can be built:

- **Manually**: reliable, can be used as gold-standards
- From **crowd-annotated resources**, like Amazon Product Reviews (1-5 stars); Rotten Tomatoes, complaints.com, bitterlemons.com

#### **Corpus**:

a collection of text segments (e.g. webpages, blog posts, reviews, tweets, etc) with humanly-annotated emotional indicators (e.g. positive, negative, etc).

E.g.: “If you are reading this because it is your darling fragrance, please wear it at home exclusively and tape the windows shut.” → {negative}

Examples of corpora:

- Subjectivity corpus
  - 10,000 sentences: subjective/objective
  - Objective: IMDB plot summaries
  - Subjective: Rotten Tomatoes website.
- “Movie Review” corpus (Pang, Lee and Vaithyanathan, 2002):
  - 2, 000 movie reviews (equal number of positive/negative)
  - Source: IMDB

#### Features

Mostly words, but also other linguistic traits describing positive/negative examples:

- Words (unigrams)
- n-grams (sequences of n words)
- Emotions from words/phrases extracted from dictionaries
- Part-of-speech (POS) tags
- Syntactic patterns (e.g. sequences of POS tags)
- Language model scores: similarities to positive/negative corpora
- Negations

All automatically extracted from the corpus

#### Steps

1. Subjectivity classifier: first run binary classifier to identify and then eliminate objective segments.
2. Sentiment classifier with remaining segments: learn how to combine and weight different attributes to make decisions. E.g. Naive Bayes

Pre-processing of corpus similar to IR

- Remove HTML or other tags
- Remove stopwords
- Perform word stemming/lemmatisation
- etc.

## Corpus-based (machine learning) SA

### Two Event Models for Naive Bayes

Naïve Bayes classiﬁer:

- How to turn Bayes rule into a classiﬁer
- A supervised probabilistic model of the observed data
- Can be used to predict the class label of new/unseen data

Multi-variate Bernoulli Model: a document is a binary vector over the space of words.

Multinomial Model: captures word frequency information in documents.

### Supervised Classification

**Supervised learning**: the machine learning task of inferring a function from labeled training data.

**Given:**

- Target: a ﬁxed set of classes: Y = y 1 , y 2 , . . . , y n , e.g. {sports, politics, . . . , music}
- Training data: a collection of data objects X with known classes Y, i.e. (X, Y ) = (x 1 , y 1 ), (x 2 , y 2 ). . . (x n , , y n ). E.g {(d1, sports), (d2, sports), (d3, music) . . . }.
- Testing data: a description of an unseen instance, Dnew e.g. a new document without class label information

**Goal**: Predict the category/class of D new : y(x) ∈ Y , where y(x) is a classiﬁcation function, aka trained model, whose domain is X and whose range is Y .

**The Bayes Rule:**

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214195548088.png" alt="image-20191214195548088" style="zoom:33%;" />

- **P(Y ):** **Prior** belief (probability of hypothesis Y before seeing any data)
- **P(X 1 , ..., X n |Y ):** **Likelihood** (probability of the data if the hypothesis Y is true)
- **P(X 1 , ..., X n ):** Data **evidence** (marginal probability of data)
- **P(Y |X 1 , ..., X n ):** **Posterior** (probability of hypothesis Y after having seen the data)

**The Independence Assumption:**

- Assume A and B are Boolean Random variables, then “A and B are independent”, if and only if  $$P(A|B) = P(A)$$

- “A and B are independent” is often notated as **A⊥B**

- Features (term presence) are **independent** of each other given the class:

  P(X 1 , ..., X 5 |Y ) = P(X 1 |Y ) • P(X 2 |Y ) • ... • P(X 5 |Y )

**Naïve Bayes Classifier:** estimate the probability of each class given a text:

- Compute the posterior probability (Bayes rule) of each class c i for text segment T

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214210940741.png" alt="image-20191214210940741" style="zoom:33%;" />

- Assumption of independence between features (“naive” assumption)

  <img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214211007548.png" alt="image-20191214211007548" style="zoom:33%;" />

  where T is described by a number of attributes or features $t_{1} , ..., t$

  I.e. joint probability of the features given the class is approximated by the product of the probabilities of each feature given the class.

- **Likelihood**: product of probabilities of each feature value of segment occurring with class c

  <img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214212401024.png" alt="image-20191214212401024" style="zoom:33%;" />

  Add **smoothing** to feature counts (add 1 to every count). where |V | is the number of distinct attributes in training (all classes).

  <img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214220831261.png" alt="image-20191214220831261" style="zoom:33%;" />

- **Prior**: probability of segment having class $c_{i}$

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214212415472.png" alt="image-20191214212415472" style="zoom:33%;" />

- **Evidence**: product of probabilities of features of segment – constant term for all classes, so can be disregarded 

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214212426859.png" alt="image-20191214212426859" style="zoom:33%;" />

- **Final decision:**<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214212439767.png" alt="image-20191214212439767" style="zoom:33%;" />

Given a trained classiﬁer that classiﬁes arbitrary segments of text we can use it to:

- Classify entire documents
- Classify sentences in a document (perhaps just those identiﬁed as subjective) and then compute a classiﬁcation of the document by aggregating the sentiments of individual sentences, according to some function.
- Classify sentences or phrases identiﬁed as discussing an aspect/feature of a target object (e.g. a sentence discussing battery life of a phone) and interpret the sentiment as the sentiment of opinion holder towards the speciﬁc aspect under discussion

#### Example exercise

| Doc  | Words                                                        | Class    |
| ---- | ------------------------------------------------------------ | -------- |
| 1    | **Great** movie, **excellent** plot, **renowned** actors     | Positive |
| 2    | I had not seen a **fantastic** plot like this in **good** 5 years. **amazing !!!** | Positive |
| 3    | **Lovely** plot, **amazing** cast, somehow I am in love with the **bad** guy | Positive |
| 4    | **Bad** movie with **great** cast, but very **poor** plot and **unimaginative** ending | Negative |
| 5    | I hate this ﬁlm, it has nothing **original**. Really **bad** | Negative |
| 6    | **Great** movie, but not...                                  | Negative |
| 7    | Very **bad** movie, I have no words to express how I dislike it | Negative |

Relative frequency in corpus is the simplest approach to estimating probabilities: 

**Priors**: (where N = total training examples)

$$p(positive) = count(positive) / N = 3/7 = 0.43$$

$$p(negative) = count(negative) / N = 4/7 = 0.57$$

Assume standard pre-processing: tokenisation, lowercasing, punctuation removal (except special punctuation like !!!)

**Likelihoods**: $$p(t_j|c_i) = \frac {count(t_j,c_i)}{count(c_i)}$$

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120165420280.png" alt="image-20200120165420280" style="zoom:23%;" /> 

Relative frequencies for prior $(P(c_i ))$ and likelihood $(P(t_j |c_i ))$ make the model in a Naive Bayes classiﬁer.

At decision (test) time, given a new segment to classify, this model is applied to ﬁnd the most likely class for the segment: 
<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120165836962.png" alt="image-20200120165836962" style="zoom:25%;" />

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120165907328.png" alt="image-20200120165907328" style="zoom:25%;" />

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120165935387.png" alt="image-20200120165935387" style="zoom:25%;" />

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120170056420.png" alt="image-20200120170056420" style="zoom:25%;" />

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120170121822.png" alt="image-20200120170121822" style="zoom:25%;" />

<img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20200120170149530.png" alt="image-20200120170149530" style="zoom:25%;" />

Given a trained classiﬁer that classiﬁes arbitrary segments of text we can use it to:

- Classify entire documents, e.g an entire review.

- Classify sentences in a document (perhaps just those identiﬁed as subjective) and then compute a classiﬁcation of the document by aggregating the sentiments of individual sentences, according to some function.

- Classify sentences or phrases identiﬁed as discussing an aspect/feature of a target object (e.g. a sentence discussing battery life of a phone) and interpret the sentiment as the sentiment of opinion holder towards the speciﬁc aspect under discussion

灵魂拷问 Questions:

- Is this a good solution? Is it robust? 
  It’s simple and will work well if data is not sparse 
- What is the role of the prior?
  Prior is very important esp. on biased cases 
- How can we improve this solution?
  - Other features? Are we missing out critical information?
    Using all words (in Naive Bayes) works well in some tasks
    Finding subsets of words may help in other tasks
    Using only adjectives can be limiting. Verbs like hate, dislike; nouns like love; words for inversion like not; intensiﬁers like very
    Pre-built polarity lexicons can be helpful 
    Negation is important
  - Other algorithms?
    MaxEnt & SVM tend to do better than Naive Bayes
- What about non-binary classiﬁcation (e.g. 5-grades of sentiment)?
  5-class ordinal classiﬁcation or regression algorithms can be used

Can contrast direct opinions versus more complex comparative opinions:

- Direct sentiment expressions on target objects
- e.g., “the picture quality of this camera is great.” Comparisons expressing similarities or diﬀerences between objects,  e.g., “car x is cheaper than car y.”

Bing Liu distinguishes 4 types of comparative relations:

- **Gradable** Non-equal gradable: Relations of the type greater or less than. E.g.: “lenses of camera A are better than those of camera B”
- **Equative**: Relations of the type equal to. E.g.: “camera A and camera B both come in 7MP”
- **Superlative**: Relations of the type greater or less than all others. E.g.:“camera A is the cheapest camera available in market”
- **Non-gradable comparisons**: Relations that compare aspects of two or more entities, but do not grade them. e.g., “Coke tastes diﬀerently from Pepsi.”

### Evaluation

- Create experimental datasets (aka test corpora): i.e., text segments that have been classiﬁed by humans, e.g. positive vs negative

- Compare (positive vs negative) system to human classiﬁcations

- Compute metrics like

  <img src="/Users/weihangzhang/Library/Application Support/typora-user-images/image-20191214222717310.png" alt="image-20191214222717310" style="zoom:33%;" />

  Same for negative class.

  Baseline: most frequent class in the training set.

  ###Conclusions

  Naïve Bayes classiﬁer:

  - Really easy to implement and often works well 
  - Often a good ﬁrst thing to try

  Actually, the Na¨ıve Bayes assumption is almost never true

  Still, Na¨ıve Bayes often performs surprisingly well even when its assumption does not hold.

  SA is an exciting topic, many applications, huge market for systems, particularly in focused domains.

  Promising results with simple techniques, but many interesting research challenges to be addressed for high accuracy.
