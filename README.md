## Project Description: Diabetes Query Assistant (RAG Application)
The Diabetes Query Assistant is a Retrieval-Augmented Generation (RAG) application designed to provide intelligent and accurate answers to queries related to diabetes. The application focuses on topics such as diet plans, exercises, meditation, and other diabetes management strategies. By leveraging advanced AI technologies, it aims to assist users in managing and understanding diabetes effectively.

### Key Features
Query Answering: Provides precise answers to user queries about diabetes management, including diet, exercises, and meditation.
Retrieval-Augmented Generation (RAG): Combines retrieval-based techniques with generative AI to deliver contextually relevant and accurate responses.
Custom Knowledge Base: Uses a curated dataset of diabetes-related content, including research articles, blogs, and guides, to ensure reliable information.
### Technologies Used
#### LangChain:
For document processing, intelligent text chunking, and embedding generation.
Enables seamless integration of retrieval and generation workflows.
#### Vector Databases:
Utilizes FAISS (or other vector databases) to store and retrieve vector embeddings of diabetes-related content.
Ensures fast and efficient similarity searches for relevant information.
#### FastAPI:
Provides a robust and scalable API for user interaction.
Handles query processing and response generation efficiently.
#### OpenAI:
Generates embeddings for documents and powers the generative AI model for answering queries.
### Workflow
#### Document Ingestion:
Diabetes-related documents (e.g., blogs, research papers, guides) are loaded and processed using LangChain.
Text is chunked into smaller, meaningful pieces for better embedding and retrieval.
#### Embedding Generation:
Each chunk is converted into vector embeddings using OpenAI's embedding models.
#### Vector Storage:
Embeddings are stored in a vector database (e.g., FAISS) for efficient similarity-based retrieval.
#### Query Processing:
User queries are processed via FastAPI.
Relevant chunks are retrieved from the vector database and passed to the generative AI model for response generation.
#### Response Generation:
The generative AI model combines retrieved information with its knowledge to generate accurate and context-aware answers.
### Use Cases
Diet Recommendations: Suggests personalized diet plans for diabetes management.
Exercise Guidance: Provides exercise routines to help regulate blood sugar levels.
Meditation Tips: Offers meditation techniques to reduce stress and improve overall well-being.
Symptom Awareness: Educates users about diabetes symptoms and prevention strategies.
### Goals
Empower users with reliable and actionable information about diabetes management.
Provide a seamless and interactive experience for answering diabetes-related queries.
Leverage state-of-the-art AI technologies to ensure accuracy and relevance.
This project is ideal for healthcare providers, diabetes educators, and individuals seeking to improve their understanding and management of diabetes.

# Component of PDF Assistant Project
 
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
