# Classical Philosophy Text Analysis

An interactive visualization platform for analyzing and comparing classical philosophical texts by Plato and Aristotle.

## 📚 Texts Included

### Aristotle's Works
- **Politics** (Aristotle Gov.docx) - 80,327 words
- **Poetics** (Aristotle Poetics.docx) - 13,985 words
- **Nicomachean Ethics** (Artistotle Ethics.docx) - 88,173 words

### Plato's Works
- **Phaedo** (Plato Phae.docx) - 31,980 words
- **Republic** (Plato Republic.docx) - 98,283 words
- **Symposium** (Plato Symp.docx) - 27,417 words

**Total Corpus:** 340,165 words across 6 classical texts

## 🎯 Features

### Text Analysis
- **Word frequency analysis** - Top 50 most common words per text
- **Vocabulary diversity** - Type-token ratios measuring lexical richness
- **Philosophical term tracking** - Frequency of key concepts (virtue, justice, soul, etc.)
- **Sentiment analysis** - Polarity and subjectivity scores (with caveats for historical texts)
- **Statistical metrics** - Average word/sentence length, question density
- **Vocabulary overlap** - Shared vocabulary between texts and authors

### Visualizations
- **Individual wordclouds** - Visual representation of each text's vocabulary
- **Comparison wordclouds** - Plato vs Aristotle combined works
- **Combined wordcloud** - All 6 texts merged
- **Interactive statistics** - Sortable tables and metrics
- **Responsive design** - Works on desktop and mobile devices

## 🚀 Quick Start

### View the Analysis

1. Open `output/index.html` in your web browser
2. Or start a local server:
   ```bash
   cd output
   python3 -m http.server 8000
   # Visit http://localhost:8000 in your browser
   ```

### Regenerate Analysis

If you want to re-run the analysis (e.g., after modifying the .docx files):

```bash
python3 analyze_texts.py
```

This will:
1. Extract text from all .docx files
2. Perform comprehensive text analysis
3. Generate wordcloud visualizations
4. Create `output/data/analysis.json` with all metrics
5. Save wordclouds to `output/wordclouds/`

## 📊 Analysis Metrics

### Vocabulary Diversity
Measures the richness of vocabulary used:
- **Aristotle's Ethics**: 13.74% (6,634 unique / 88,173 total)
- **Aristotle's Politics**: 13.12% (5,476 unique / 80,327 total)
- **Plato's Republic**: 15.51% (7,715 unique / 98,283 total)
- **Plato's Phaedo**: 26.77% (4,703 unique / 31,980 total)
- **Plato's Symposium**: 27.48% (4,036 unique / 27,417 total)
- **Aristotle's Poetics**: 30.04% (2,586 unique / 13,985 total)

Higher diversity indicates more varied vocabulary usage. Shorter texts tend to have higher diversity ratios.

### Philosophical Terms Tracked
- virtue, justice, good, evil
- soul, truth, knowledge, wisdom
- beauty, reason, nature
- form, idea, being, reality, existence

### Question Density
Measures use of questions (indicator of Socratic method in Plato's dialogues):
- Plato's works generally show higher question density
- Indicates dialectical vs. treatise writing styles

## 🛠️ Technical Details

### Requirements
- Python 3.7+
- python-docx
- wordcloud
- matplotlib
- nltk
- textblob

### Installation
```bash
pip install python-docx wordcloud matplotlib nltk textblob pillow
```

### Project Structure
```
Last-Stand/
├── *.docx                    # Source philosophical texts
├── analyze_texts.py          # Main analysis script
├── output/
│   ├── index.html           # Interactive visualization webpage
│   ├── data/
│   │   └── analysis.json    # Complete analysis results
│   └── wordclouds/
│       ├── *.png            # Individual text wordclouds
│       ├── plato_combined.png
│       ├── aristotle_combined.png
│       └── all_texts_combined.png
└── README.md
```

## 📖 How to Use the Webpage

### Overview Tab
- Summary statistics for all texts
- Combined wordcloud
- Clickable cards to explore individual texts

### Individual Texts Tab
- Select any text from dropdown
- View detailed statistics and metrics
- See text-specific wordcloud
- Top 30 most frequent words
- Philosophical terms found in that text

### Comparisons Tab
- Side-by-side comparison of Plato vs Aristotle
- Combined wordclouds for each author
- Aggregate statistics

### Vocabulary Overlap Tab
- Matrix showing shared vocabulary between all text pairs
- Overlap ratios and sample shared words
- Identifies thematic connections

### Philosophical Terms Tab
- Frequency of key philosophical concepts
- Distribution across all texts
- Sortable by total occurrences

## 🔍 Insights

### Teacher and Student
Plato was Aristotle's teacher, and this relationship is reflected in their shared philosophical vocabulary. The vocabulary overlap analysis reveals which concepts were transmitted from teacher to student and which diverged.

### Writing Styles
- **Plato**: Dialogue-heavy, Socratic method, higher question density
- **Aristotle**: Systematic treatises, lower question density, analytical approach

### Most Common Philosophical Themes
Analysis of philosophical terms shows the central concerns of each philosopher:
- Both emphasize "good," "virtue," and "soul"
- Plato focuses more on "beauty" and "form"
- Aristotle emphasizes "nature" and "reason"

## ⚠️ Known Issues

- `Artistotle Ethics.docx` has a typo in the filename (should be "Aristotle")
- Sentiment analysis is approximate for classical texts and may not capture philosophical nuance
- Translation effects may influence word frequency and vocabulary metrics

## 📝 License

These are classical philosophical texts in the public domain. The analysis code and visualizations are provided as-is for educational purposes.

## 🤝 Contributing

To add more texts or improve the analysis:

1. Add new .docx files to the root directory
2. Update the `DOCUMENTS` dictionary in `analyze_texts.py`
3. Run `python3 analyze_texts.py`
4. Refresh the webpage

---

**Created with:** Python, NLTK, WordCloud, TextBlob, and vanilla JavaScript
