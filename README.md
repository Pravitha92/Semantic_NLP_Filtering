# Semantic NLP Filtering for Deep Learning Papers in Virology/Epidemiology

## Project Overview
This project uses semantic NLP techniques to filter, classify, and extract relevant academic papers on virology and epidemiology. Given an initial dataset [collection_with_abstarcts.csv](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/collection_with_abstracts.csv) from [PubMed](https://pubmed.ncbi.nlm.nih.gov/). The goal is to identify papers that implement deep learning neural network-based solutions in the fields of virology and epidemiology.

## Table of Contents
* [Preprocess the data](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#preprocess-the-data)
* [Semantic NLP Filtering of Papers]()
    * [NLP technique for filtering the papers]
    * [Why this approach is more effective than keyword-based filtering?]
* [Classification of Papers]()
* [Extract the name of the method]()
* [Dataset Statistics]()

## Preprocess the data
Selected relevant columns (`PMID`, `Title`, `Journal/Book`, and `Abstract`) from the dataset. Filled 213 missing values in the `Abstract` column by combining 
`Title`  and `Journal/Book`, ensuring data completeness for further analysis. Following this, data cleaning was applied to standardize the text by converting it 
to lowercase, removing stopwords, and eliminating punctuation, streamlining the dataset for processing.

## Semantic NLP Filtering of Papers
Since the `Abstract` field provides the most detailed insight into each paper's content, it is used as the primary source for filtering. This method prioritizes contextual understanding to accurately capture papers that apply deep learning techniques to virology/epidemiology.
#### NLP technique for filtering the papers
SBERT (Sentence-BERT) is used for semantic NLP filtering, enabling more accurate identification of relevant papers based on meaning rather than simple keyword matching, allowing precise identification of deep learning applications in virology and epidemiology.
###### Model Selection: 
A pretrained SBERT model, `all-MiniLM-L6-v2`, chosen for its efficiency and high-quality embeddings, suited for similarity tasks on large datasets.
###### Defining Target Terms: 
Target terms relevant to deep learning in virology/epidemiology were identified, and SBERT-generated embeddings were created for each term. These serve as reference embeddings for semantic comparisons.

