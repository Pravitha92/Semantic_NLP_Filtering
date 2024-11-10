# Semantic NLP Filtering for Deep Learning Papers in Virology/Epidemiology

## Project Overview
This project uses semantic NLP techniques to filter, classify, and extract relevant academic papers on virology and epidemiology. Given an initial dataset [collection_with_abstarcts.csv](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/collection_with_abstracts.csv) from [PubMed](https://pubmed.ncbi.nlm.nih.gov/). The goal is to identify papers that implement deep learning neural network-based solutions in the fields of virology and epidemiology.

## Table of Contents
* [Preprocess the data](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#preprocess-the-data)
* [Semantic NLP Filtering of Papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#semantic-nlp-filtering-of-papers)
    * [NLP technique for filtering the papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#nlp-technique-for-filtering-the-papers)
    * [Why this approach is more effective than keyword-based filtering?](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#why-this-approach-is-more-effective-than-keyword-based-filtering)
* [Classification of Papers](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#classification-of-papers)
* [Extract the name of the method](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#extract-the-name-of-the-method)
* [Resulting Dataset Statistics](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#resulting-dataset-statistics)
* [Tools and Libraries](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#tools-and-libraries)
* [Conclusion](https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/README.md#conclusion)

## Preprocess the data
Selected relevant columns (`PMID`, `Title`, `Journal/Book`, and `Abstract`) from the dataset. Filled 213 missing values in the `Abstract` column by combining 
`Title`  and `Journal/Book`, ensuring data completeness for further analysis. Following this, data cleaning was applied to standardize the text by converting it 
to lowercase, removing stopwords, and eliminating punctuation, streamlining the dataset for processing.

## Semantic NLP Filtering of Papers
The `Abstract` field, which provides the most detailed insight into each paper's content, is used as the primary source for filtering. Semantic NLP filtering is done in [filtering_DL_papers_virology_epidemiology.ipynb(https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/notebooks/filtering_DL_papers_virology_epidemiology.ipynb) to identify papers applying deep learning in virology/epidemiology.
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
Classified papers based on the presence of specific keywords related to **text mining**, **computer vision**, **both** or **other**. It checks if any of the keywords from each category appear in the combined text fields (`Abstract`, `Title`, and `Journal`), and assigns the appropriate classification.

```python
    def classify_paper(self, row):
        text = f"{row['Abstract']} {row['Title']} {row['Journal']}".lower()
        contains_text_mining = any(keyword in text for keyword in self.text_mining_keywords)
        contains_computer_vision = any(keyword in text for keyword in self.computer_vision_keywords)
        contains_both = any(keyword in text for keyword in self.both_keywords)

        if contains_both:
            return "both"
        elif contains_text_mining:
            return "text mining"
        elif contains_computer_vision:
            return "computer vision"
        return "other"

```

## Extract the Name of the Method
To provide deeper insights, extracts specific terms related to deep learning methods from each paper’s content. This step identifies and lists methods by matching each `Abstract`, `Title`, and `Journal` with keywords across four categories. The extracted methods are saved in a `methods_used` column for further analysis.

```python
    def extract_method_name(self, row):
        content = f"{row['Abstract']} {row['Journal']} {row['Title']}".lower()
        methods = [kw for kw in self.text_mining_keywords + self.computer_vision_keywords + self.both_keywords + self.other_keywords if re.search(rf'\b{kw}\b', content)]
        return ', '.join(set(methods)) if methods else "None"

```

## Resulting Dataset Statistics
* **Total Records:** 11,450 papers (original count before filtering)
* **Filtered Dataset:** After applying semantic filtering to the `Abstract` field, only papers relevant to deep learning in virology/epidemiology were kept.
* **Filtered Out Percentage:** Approximately **6.38%  of the papers are relevant** for further analysis, 93.62% of the papers were filtered out as irrelevant.

* **Classification Results:**
The papers were classified into the following categories based on the techniques they apply:
   - **Both (Text Mining & Computer Vision)**: 316 papers
   - **Text Mining**: 165 papers
   - **Computer Vision**: 35 papers
   - **Other (Not directly related to primary focus)**: 214 papers

* The pie chart below visualizes the distribution of relevant methods across the dataset:
    <img src="https://github.com/Pravitha92/Semantic_NLP_Filtering/blob/main/trends_in_methoods_types.png" width="700" alt="Trends in Methods Types">

## Tools and Libraries
This project relies on the following tools and libraries:
- Pandas 
- nltk
- Matplotlib
- SBERT
- Google collab
- Pycharm

## Conclusion
This project provides an efficient solution for filtering and classifying academic papers that apply deep learning techniques in virology and epidemiology. By using semantic NLP methods, it enables researchers to quickly identify and analyze relevant studies, categorized by specific techniques like text mining and computer vision. This approach accelerates literature review processes, helping researchers focus on impactful work in their fields.

