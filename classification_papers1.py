import pandas as pd
import re
import matplotlib.pyplot as plt

class PaperClassifier:
    def __init__(self, filepath):
        # Set the original dataset count manually
        self.original_count = 11450

        # Load data and drop unnecessary columns
        self.data = pd.read_csv(filepath)
        self.data = self.data.drop(columns=['abstract_embedding', 'similarity_score'], errors='ignore')
        self.data = self.data.rename(columns={'Journal/Book': 'Journal'})

        # Define keywords for each category
        self.text_mining_keywords = [
            "natural language processing", "text mining", "NLP", "computational linguistics", "RNN", "recurrent neural network",
            "language modeling", "text analysis", "computational semantics", "text data analysis", "text analytics",
            "textual data analysis", "speech and language technology", "language processing", "LSTM", "pretrained language model",
            "long short-term memory network", "large language model", "llm", "generative language model"
        ]

        self.computer_vision_keywords = [
            "computer vision", "vision model", "image processing", "vision algorithms", "computer graphics and vision",
            "object recognition", "diffusion model", "scene understanding", "vision transformer", "CNN", "convolutional neural network",
            "generative diffusion model", "diffusion-based generative model", "continuous diffusion model"
        ]

        self.both_keywords = [
            "neural network", "artificial neural network", "generative AI", "neural net algorithm",
            "foundation model", "multilayer perceptron", "transformer models", "self-attention models",
            "transformer architecture", "attention-based neural networks", "transformer networks", "transformer-based model",
            "multimodal neural network", "sequence-to-sequence models", "generative artificial intelligence"
        ]

        self.other_keywords = [
            "deep learning", "machine learning model", "deep neural networks", "generative deep learning", "GRNN", "regression",
            "artificial intelligence", "feedforward neural network", "generative models", "multimodal model"
        ]

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

    # Extract the name of the method used for each relevant paper
    def extract_method_name(self, row):
        content = f"{row['Abstract']} {row['Journal']} {row['Title']}".lower()
        methods = [kw for kw in self.text_mining_keywords + self.computer_vision_keywords + self.both_keywords + self.other_keywords if re.search(rf'\b{kw}\b', content)]
        return ', '.join(set(methods)) if methods else "None"

    def classify_and_save(self, classification_file="classified_papers.csv", detailed_file="filtered_papers_with_methods.csv"):
        # Classify papers
        self.data['method_type'] = self.data.apply(self.classify_paper, axis=1)

        # Calculate relevance
        relevant_papers = self.data[self.data['method_type'].isin(['text mining', 'computer vision', 'both', 'other'])]
        relevant_count = len(relevant_papers)
        relevant_percentage = (relevant_count / self.original_count) * 100
        irrelevant_percentage = 100 - relevant_percentage

        # Save classification-only data
        classification_data = self.data[['Title', 'Abstract', 'Journal', 'method_type']]
        classification_data.to_csv(classification_file, index=False)

        # Extract methods and save detailed data
        self.data["methods_used"] = self.data.apply(self.extract_method_name, axis=1)
        self.data.to_csv(detailed_file, index=False)

        # Display relevance summary
        print(f"Filtered Out Percentage: Approximately {irrelevant_percentage:.2f}% of the papers were filtered out as irrelevant, leaving {relevant_percentage:.2f}% as relevant for further analysis.")

        # Generate pie chart for trends in method types
        self.plot_method_distribution()

    def plot_method_distribution(self):
        # Get method type counts
        method_counts = self.report_method_counts()
        labels = method_counts.index
        sizes = method_counts.values
        print(method_counts)

        # Plot pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Trends in Method Types for Relevant Papers")
        plt.show()

    def report_method_counts(self):
        return self.data['method_type'].value_counts()


classifier = PaperClassifier("filtered_deep_learning_virology_epidemiology.csv")
classifier.classify_and_save()
