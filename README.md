# Enhanced Question Classifier

An intelligent question classification system that uses multiple AI approaches to understand and categorize programming and technical questions.

## Features

- **Multi-Method Classification**: Combines zero-shot classification, keyword analysis, and semantic understanding
- **8 Comprehensive Categories**: Covers all aspects of software development and technical work
- **Detailed Analysis**: Shows reasoning behind classification decisions
- **Interactive Interface**: User-friendly menu system with examples
- **High Accuracy**: Uses state-of-the-art NLP models for better understanding

## Categories

1. **Code Generation and Implementation** - Writing new code, creating functions, implementing algorithms
2. **Debugging and Error Handling** - Fixing bugs, resolving errors, troubleshooting issues
3. **Code Review and Optimization** - Analyzing code quality, performance optimization, refactoring
4. **Testing and Quality Assurance** - Writing tests, unit testing, integration testing, QA processes
5. **Documentation and Explanation** - Writing documentation, explaining concepts, creating tutorials
6. **Research and Learning** - Learning new technologies, understanding concepts, finding resources
7. **System Design and Architecture** - Designing systems, architectural decisions, scalability
8. **Data Analysis and Processing** - Data manipulation, analysis, visualization, machine learning

## Installation

1. Install Python 3.7 or higher
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the classifier:
```bash
python classification.py
```

The program will present you with a menu:
- **Option 1**: Classify a question
- **Option 2**: Show all categories
- **Option 3**: Show example questions
- **Option 4**: Exit

## How It Works

### 1. Zero-Shot Classification
Uses Facebook's BART-large-MNLI model to understand the semantic meaning of questions and match them to categories.

### 2. Keyword Analysis
Analyzes keywords in the question to find patterns that match category-specific terms.

### 3. Combined Analysis
Intelligently combines both methods to provide the most accurate classification with confidence scores.

## Example Questions

- **Code Generation**: "How do I create a REST API in Python?"
- **Debugging**: "My code is throwing a null pointer exception"
- **Testing**: "How to write unit tests for this function?"
- **Documentation**: "Explain how this algorithm works"
- **Research**: "What is machine learning?"
- **System Design**: "How to design a scalable web application?"
- **Data Analysis**: "How to analyze this dataset?"

## Technical Details

- **Model**: facebook/bart-large-mnli (zero-shot classification)
- **Preprocessing**: Text cleaning, keyword extraction, stopword removal
- **Confidence Scoring**: Combines semantic and keyword-based confidence
- **Fallback Logic**: Uses best available method when others fail

## Requirements

- Python 3.7+
- PyTorch
- Transformers
- scikit-learn
- NLTK
- NumPy

## Performance

The classifier provides:
- **High Accuracy**: Multiple validation methods ensure correct classification
- **Confidence Levels**: Very High (80%+), High (60%+), Medium (40%+), Low (<40%)
- **Reasoning**: Explains why a particular category was chosen
- **Fallback**: Graceful handling of edge cases and unclear questions
