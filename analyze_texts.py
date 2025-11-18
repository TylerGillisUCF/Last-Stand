#!/usr/bin/env python3
"""
Text Analysis Script for Classical Philosophy Texts
Extracts text from .docx files and performs comprehensive analysis
"""

import json
import os
import re
from collections import Counter
from pathlib import Path

from docx import Document
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Define the documents to analyze
DOCUMENTS = {
    'Aristotle Gov.docx': {
        'author': 'Aristotle',
        'title': 'Politics',
        'short_name': 'aristotle_politics'
    },
    'Aristotle Poetics.docx': {
        'author': 'Aristotle',
        'title': 'Poetics',
        'short_name': 'aristotle_poetics'
    },
    'Artistotle Ethics.docx': {  # Note: typo in filename
        'author': 'Aristotle',
        'title': 'Nicomachean Ethics',
        'short_name': 'aristotle_ethics'
    },
    'Plato Phae.docx': {
        'author': 'Plato',
        'title': 'Phaedo',
        'short_name': 'plato_phaedo'
    },
    'Plato Republic.docx': {
        'author': 'Plato',
        'title': 'Republic',
        'short_name': 'plato_republic'
    },
    'Plato Symp.docx': {
        'author': 'Plato',
        'title': 'Symposium',
        'short_name': 'plato_symposium'
    }
}

# Common stopwords including classical philosophy specific ones
STOP_WORDS = set(stopwords.words('english'))
ADDITIONAL_STOPS = {'said', 'would', 'could', 'shall', 'must', 'one', 'two', 'may',
                    'also', 'yet', 'thus', 'therefore', 'however', 'moreover'}
STOP_WORDS.update(ADDITIONAL_STOPS)


def extract_text_from_docx(filename):
    """Extract all text from a .docx file"""
    doc = Document(filename)
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            full_text.append(paragraph.text)
    return '\n'.join(full_text)


def clean_text(text):
    """Clean and normalize text"""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^a-z\s\.\,\;\:\!\?]', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_words(text, remove_stopwords=True):
    """Tokenize text into words"""
    words = word_tokenize(text)
    if remove_stopwords:
        words = [w for w in words if w.isalpha() and w not in STOP_WORDS and len(w) > 2]
    else:
        words = [w for w in words if w.isalpha() and len(w) > 2]
    return words


def analyze_text(text, metadata):
    """Perform comprehensive text analysis"""

    # Basic stats
    sentences = sent_tokenize(text)
    all_words = get_words(text, remove_stopwords=False)
    content_words = get_words(text, remove_stopwords=True)

    # Word frequency
    word_freq = Counter(content_words)
    top_50_words = dict(word_freq.most_common(50))

    # Vocabulary diversity
    unique_words = len(set(content_words))
    total_words = len(content_words)
    diversity_ratio = unique_words / total_words if total_words > 0 else 0

    # Average word and sentence length
    avg_word_length = sum(len(w) for w in all_words) / len(all_words) if all_words else 0
    avg_sentence_length = len(all_words) / len(sentences) if sentences else 0

    # Sentiment analysis (with caveat for philosophical texts)
    blob = TextBlob(text[:5000])  # Analyze first 5000 chars for speed
    sentiment = {
        'polarity': round(blob.sentiment.polarity, 3),
        'subjectivity': round(blob.sentiment.subjectivity, 3)
    }

    # Philosophical terms frequency
    philosophical_terms = ['virtue', 'justice', 'good', 'evil', 'soul', 'truth',
                          'knowledge', 'wisdom', 'beauty', 'reason', 'nature',
                          'form', 'idea', 'being', 'reality', 'existence']

    term_freq = {}
    for term in philosophical_terms:
        count = text.lower().count(term)
        if count > 0:
            term_freq[term] = count

    # Question density (Socratic method indicator)
    question_count = text.count('?')
    question_density = question_count / len(sentences) if sentences else 0

    return {
        'metadata': metadata,
        'statistics': {
            'total_words': len(all_words),
            'unique_words': unique_words,
            'vocabulary_diversity': round(diversity_ratio, 4),
            'total_sentences': len(sentences),
            'avg_word_length': round(avg_word_length, 2),
            'avg_sentence_length': round(avg_sentence_length, 2),
            'question_count': question_count,
            'question_density': round(question_density, 4)
        },
        'top_50_words': top_50_words,
        'philosophical_terms': term_freq,
        'sentiment': sentiment
    }


def generate_wordcloud(words_dict, output_path, title):
    """Generate and save a wordcloud"""
    if not words_dict:
        print(f"No words to generate wordcloud for {title}")
        return

    wordcloud = WordCloud(
        width=1200,
        height=800,
        background_color='white',
        colormap='viridis',
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(words_dict)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=20, pad=20)
    plt.tight_layout(pad=0)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Generated wordcloud: {output_path}")


def main():
    """Main analysis pipeline"""

    # Create output directories
    os.makedirs('output/wordclouds', exist_ok=True)
    os.makedirs('output/data', exist_ok=True)

    all_analyses = {}
    all_texts = {}

    print("Starting text extraction and analysis...\n")

    # Process each document
    for filename, metadata in DOCUMENTS.items():
        if not os.path.exists(filename):
            print(f"WARNING: {filename} not found, skipping...")
            continue

        print(f"Processing: {metadata['title']} by {metadata['author']}")

        # Extract and clean text
        raw_text = extract_text_from_docx(filename)
        cleaned_text = clean_text(raw_text)
        all_texts[metadata['short_name']] = cleaned_text

        # Analyze
        analysis = analyze_text(cleaned_text, metadata)
        all_analyses[metadata['short_name']] = analysis

        # Generate individual wordcloud
        wordcloud_path = f"output/wordclouds/{metadata['short_name']}.png"
        generate_wordcloud(
            analysis['top_50_words'],
            wordcloud_path,
            f"{metadata['title']} by {metadata['author']}"
        )

        print(f"  - Total words: {analysis['statistics']['total_words']:,}")
        print(f"  - Unique words: {analysis['statistics']['unique_words']:,}")
        print(f"  - Diversity: {analysis['statistics']['vocabulary_diversity']:.2%}\n")

    # Generate comparison wordclouds
    print("Generating comparison wordclouds...\n")

    # Combined all texts
    all_words = Counter()
    for analysis in all_analyses.values():
        all_words.update(analysis['top_50_words'])

    generate_wordcloud(
        dict(all_words.most_common(100)),
        'output/wordclouds/all_texts_combined.png',
        'All Philosophical Texts Combined'
    )

    # Plato vs Aristotle
    plato_words = Counter()
    aristotle_words = Counter()

    for short_name, analysis in all_analyses.items():
        if analysis['metadata']['author'] == 'Plato':
            plato_words.update(analysis['top_50_words'])
        else:
            aristotle_words.update(analysis['top_50_words'])

    generate_wordcloud(
        dict(plato_words.most_common(75)),
        'output/wordclouds/plato_combined.png',
        'Plato - All Works Combined'
    )

    generate_wordcloud(
        dict(aristotle_words.most_common(75)),
        'output/wordclouds/aristotle_combined.png',
        'Aristotle - All Works Combined'
    )

    # Calculate vocabulary overlap
    print("Calculating vocabulary overlap...\n")

    overlap_data = {}
    doc_names = list(all_analyses.keys())

    for i, name1 in enumerate(doc_names):
        for name2 in doc_names[i+1:]:
            words1 = set(all_analyses[name1]['top_50_words'].keys())
            words2 = set(all_analyses[name2]['top_50_words'].keys())

            overlap = words1.intersection(words2)
            overlap_ratio = len(overlap) / min(len(words1), len(words2)) if words1 and words2 else 0

            key = f"{name1}_vs_{name2}"
            overlap_data[key] = {
                'doc1': name1,
                'doc2': name2,
                'shared_words': len(overlap),
                'overlap_ratio': round(overlap_ratio, 4),
                'shared_word_list': sorted(list(overlap))[:20]  # Top 20 shared words
            }

    # Save all analysis data to JSON
    output_data = {
        'individual_analyses': all_analyses,
        'vocabulary_overlap': overlap_data,
        'summary': {
            'total_documents': len(all_analyses),
            'authors': {
                'Plato': len([a for a in all_analyses.values() if a['metadata']['author'] == 'Plato']),
                'Aristotle': len([a for a in all_analyses.values() if a['metadata']['author'] == 'Aristotle'])
            }
        }
    }

    with open('output/data/analysis.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("Analysis complete!")
    print(f"Results saved to: output/data/analysis.json")
    print(f"Wordclouds saved to: output/wordclouds/")
    print(f"\nTotal documents analyzed: {len(all_analyses)}")


if __name__ == '__main__':
    main()
