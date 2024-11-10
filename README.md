# Semantic NLP Filtering for Deep Learning Papers in Virology/Epidemiology

## Project Overview
This project uses semantic NLP techniques to filter, classify, and extract relevant academic papers on virology and epidemiology. Given an initial dataset [collection_with_abstarcts.csv](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/collection_with_abstracts.csv) from [PubMed](https://pubmed.ncbi.nlm.nih.gov/). The goal is to identify papers that implement deep learning neural network-based solutions in the fields of virology and epidemiology.

## Table of Contents
* [Preprocess the data](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#preprocess-the-data)
* [Semantic NLP Filtering of Papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/edit/main/README.md#semantic-nlp-filtering-of-papers)
    * [NLP technique for filtering the papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/edit/main/README.md#nlp-technique-for-filtering-the-papers)
    * [Why this approach is more effective than keyword-based filtering?](https://github.com/Pravitha92/Semantic_NLP_Filtering/edit/main/README.md#why-this-approach-is-more-effective-than-keyword-based-filtering)
* [Classification of Papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/edit/main/README.md#classification-of-papers)
* [Extract the name of the method]()
* [Dataset Statistics]()

## Preprocess the data
Selected relevant columns (`PMID`, `Title`, `Journal/Book`, and `Abstract`) from the dataset. Filled 213 missing values in the `Abstract` column by combining 
`Title`  and `Journal/Book`, ensuring data completeness for further analysis. Following this, data cleaning was applied to standardize the text by converting it 
to lowercase, removing stopwords, and eliminating punctuation, streamlining the dataset for processing.

## Semantic NLP Filtering of Papers
The `Abstract` field, which provides the most detailed insight into each paper's content, is used as the primary source for filtering.
### NLP technique for filtering the papers
SBERT (Sentence-BERT) is used for semantic NLP filtering, enabling more accurate identification of relevant papers based on meaning rather than simple keyword matching. This approach prioritizes contextual understanding to accurately capture deep learning papers to virology/epidemiology.
- **Model Selection:**
    A pretrained SBERT model, `all-MiniLM-L6-v2`, chose due to its efficiency and accurate embeddings, making it well-suited for filtering relevant papers. This 
   model provides a good balance of speed (5x faster than other models) and accuracy, making it ideal for filtering relevant papers.
  
- **Defining Target Terms:** 
    Target terms relevant to deep learning in virology/epidemiology were identified, and SBERT-generated embeddings were created for each term. These serve as          reference embeddings for semantic comparisons.
  
- **Filtering Process:**
 Each paper’s Abstract embedding was generated using the SBERT model. By comparing these embeddings with target term embeddings using cosine similarity, a score was calculated to gauge relevance. Papers meeting or exceeding the similarity threshold were retained.

### Why this approach is more effective than keyword-based filtering?
- Captures the contextual meaning of abstracts of each paper, recognizing relevant papers even with varied terminology.
- Reduces irrelevant results by minimizing false positives from mere keyword mentions.
- Scales easily, allowing flexible updates to target terms for ongoing research.
By focusing on the overall meaning of each paper’s abstract, this approach enables more precise filtering and captures a broader set of relevant papers.

## Classification of Papers
Papers are classified as text mining, computer vision, both, or other based on keywords in abstracts, titles, and journals, enabling effective filtering of deep learning applications relevant to virology and epidemiology.


