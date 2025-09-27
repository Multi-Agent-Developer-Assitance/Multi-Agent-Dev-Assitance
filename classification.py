# ===== IMPORTS =====
# pip install torch transformers

from transformers import pipeline  # for using pre-trained models from HuggingFace

# ===== LOAD MODEL =====
# facebook/bart-large-mnli is a zero-shot text classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# ===== DEFINE CATEGORIES =====
CATEGORIES = [
    "Research-Based",
    "Generative/Coding",
    "Testing/QA",
    "Debugging/Error Solving",
    "Comparison/Recommendation"
]

# ===== CLASSIFICATION FUNCTION =====
def classify_question(question):
    # Perform zero-shot classification
    result = classifier(question, CATEGORIES)
    
    # Extract the top predicted category and confidence
    best_category = result['labels'][0]
    confidence = result['scores'][0]
    
    # Print and return result
    print(f"\n Predicted Category: {best_category} (Confidence: {confidence:.2f})")
    return best_category

# ===== MAIN PROGRAM LOOP =====
if __name__ == "__main__":
    print("=== Open-Source Question Classifier ===")
    
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ").strip()
        if question.lower() == "exit":
            print("Goodbye ")
            break
        classify_question(question)
