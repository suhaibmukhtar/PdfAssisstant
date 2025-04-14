# PDF Assistant

A powerful document processing tool that can handle multiple document formats (PDF, DOCX, HTML, TXT, MD) with intelligent text chunking capabilities.

## Features

- **Multi-format Support**: Process various document formats including:
  - PDF files
  - Word documents (DOCX)
  - HTML files
  - Plain text files (TXT)
  - Markdown files (MD)

- **Intelligent Document Processing**:
  - Automatic document loading and parsing
  - Smart text chunking with configurable size and overlap
  - Source tracking for processed documents
  - Comprehensive logging system

- **Built with Modern Tools**:
  - Uses LangChain for document processing
  - OpenAI integration for advanced text processing
  - Efficient recursive text splitting

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd PdfAssisstant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your documents in the `data` directory.

2. Run the assistant:
```bash
python main.py
```

The assistant will:
- Load all supported documents from the data directory
- Process and chunk the documents
- Log the progress in the `logs` directory

## Project Structure

```
PdfAssisstant/
├── data/               # Directory for input documents
├── logs/              # Log files directory
├── main.py            # Main application entry point
├── document_parsers.py # Document loading and parsing
├── chunking.py        # Text chunking functionality
├── logger.py          # Logging configuration
└── requirements.txt   # Project dependencies
```

## Configuration

- **Chunk Size**: Default chunk size is 500 characters
- **Chunk Overlap**: Default overlap is 100 characters
- Modify these values in `chunking.py` if needed

## Supported File Types

- PDF (`.pdf`)
- Word Documents (`.docx`)
- HTML (`.html`)
- Text files (`.txt`)
- Markdown files (`.md`)

## Logging

The application maintains detailed logs of:
- Document loading process
- Number of documents processed
- Chunking operations
- Any errors or warnings during processing

Logs are stored in the `logs` directory.

## License

This project is licensed under the terms included in the LICENSE file.

## Requirements

Key dependencies include:
- langchain
- openai
- python-dotenv
- pypdf
- docx2txt
- And others listed in requirements.txt

## Error Handling

The application includes robust error handling for:
- Invalid file types
- File reading errors
- Processing failures
- API-related issues

All errors are logged for debugging purposes.

---

For bug reports and feature requests, please open an issue in the repository.