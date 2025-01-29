from transformers import pipeline 
# Use a pre-trained model for intent recognition 
def process_intent(text): 
    classifier = pipeline("zero-shot-classification") 
    labels = ["general query", "device control", "set a reminder"] 
    result = classifier(text, labels) 
    intent = result["labels"][0] # Highest-confidence intent 
    return intent