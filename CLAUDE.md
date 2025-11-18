# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains classical philosophical texts in Microsoft Word format (.docx):

**Aristotle's Works:**
- `Aristotle Gov.docx` - Politics (351KB)
- `Aristotle Poetics.docx` - Poetics (79KB)
- `Artistotle Ethics.docx` - Nicomachean Ethics (407KB) *[Note: filename has typo "Artistotle"]*

**Plato's Works:**
- `Plato Phae.docx` - Phaedo (161KB)
- `Plato Republic.docx` - The Republic (488KB)
- `Plato Symp.docx` - Symposium (132KB)

## Repository Structure

The repository uses a flat structure with all documents in the root directory. There is currently no build system, tests, or automation.

## Working with Documents

### File Format
All texts are stored as Microsoft Word 2007+ documents (.docx). To work with these programmatically:

```bash
# Convert .docx to plain text (requires pandoc)
pandoc "Aristotle Gov.docx" -t plain -o output.txt

# Convert to markdown
pandoc "Plato Republic.docx" -t markdown -o output.md

# Extract text using Python (requires python-docx)
python -c "from docx import Document; doc = Document('Plato Phae.docx'); print('\n'.join([p.text for p in doc.paragraphs]))"
```

### Known Issues
- `Artistotle Ethics.docx` has a typo in the filename (should be "Aristotle")

## Potential Development Directions

If transforming this into a structured project, consider:

1. **Text Format Conversion**: Convert .docx files to markdown or plain text for better version control and diffs
2. **Metadata Addition**: Add YAML frontmatter or JSON metadata files describing each work (author, date, translation info, etc.)
3. **Search/Analysis Tools**: Build tools for searching across texts or performing textual analysis
4. **Documentation**: Add a README.md explaining the purpose, sources, and any translation information
5. **Organization**: Consider organizing by author in subdirectories (`aristotle/`, `plato/`)

## Git Branch

Current development branch: `claude/init-project-setup-01FJLaq7SmLJQxZHNtr9snyf`
