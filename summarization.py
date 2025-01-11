from transformers import pipeline
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization", model="./trained_model", tokenizer="./trained_model")

def summarize_text_in_chunks(text, chunk_size=3, max_length=90, min_length=30):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-ZİĞÜŞÖÇ][a-zığüşöç]\.)(?<=\.|\?)\s', text)
    
    chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
        summaries.append(summary)
    
    combined_summary = " ".join(summaries)
    combined_summary = clean_redundancies(combined_summary)
    
    return combined_summary

def clean_redundancies(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-ZİĞÜŞÖÇ][a-zığüşöç]\.)(?<=\.|\?)\s', text)
    seen_sentences = set()
    cleaned_sentences = []
    
    for sentence in sentences:
        cleaned_sentence = remove_repeated_phrases(sentence)
        if cleaned_sentence.lower() not in seen_sentences:
            seen_sentences.add(cleaned_sentence.lower())
            cleaned_sentences.append(cleaned_sentence)
    
    return " ".join(cleaned_sentences)

def remove_repeated_phrases(sentence):
    words = sentence.split()
    seen_words = set()
    cleaned_words = []
    
    for word in words:
        if word not in seen_words:
            seen_words.add(word)
            cleaned_words.append(word)
    
    return " ".join(cleaned_words)

def post_process_summary(summary):
    summary = summary.strip()
    summary = summary.capitalize()
    summary = re.sub(r" +", " ", summary)
    summary = re.sub(r"(?<=[.,])(?=[^\s])", " ", summary)
    return summary

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    article = data.get("article", "")


    if not article:
        return jsonify({"error": "No article provided"}), 400

    processed_article = summarize_text_in_chunks(article)
    processed_summary = post_process_summary(processed_article)
    
    words = processed_summary.split()
    title = ' '.join(words[:2]) + "..."

    return jsonify({
        "title": title,
        "summary": processed_summary,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)