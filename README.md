# RAG with Gemini API & ChromaDB

This repository demonstrates practical workflows for both prompt engineering and advanced multimodal retrieval-augmented generation (RAG) using the Gemini API (Gemini 2.5 Flash) and ChromaDB. The project is organized around two main files:

- **gemini_tutorial.ipynb**:  
  - Explores prompt engineering techniques, guided by resources like promptguide.ai.
  - Experiments with the Gemini API (from Google) for single- and multi-turn conversations, streaming outputs, and multimodal (text + image) prompting.
  - Covers working with chat history and system instructions to shape model behavior.
  - Includes hands-on examples for streaming responses and markdown visualization.

- **gemini_rag.ipynb**:  
  - Implements a multimodal RAG pipeline powered by Gemini 2.5 Flash and ChromaDB.
  - Loads a PDF document (the DeepSeek-R1 research paper) from a URL, parses each page, and saves it as an image.
  - Visualizes each page image to confirm parsing.
  - Uses Gemini 2.5 Flash to ingest each page image and perform Optical Character Recognition (OCR)
  - All extracted and summarized content is converted to Markdown for rich, readable representation.
   - The markdown is split into page-level chunks, constrained by token count, and is intelligently chunked into semantically meaningful sections using `<chunk>` tags.
  - Tables are extracted and formatted in HTML, with additional summaries for improved retrieval; figures and graphs are similarly summarized and chunked.
  - The chunks are consolidated into a list, and embedded using Gemini’s `text-embedding-004` model.
  - Embedded chunks are stored in ChromaDB’s vector database (via PersistentClient) for fast similarity search.
  - User queries are embedded and matched against the vector database; the k-nearest chunks are retrieved and used as context in Gemini’s prompt for accurate, context-aware answers.

## Key Technologies & Libraries

- **Prompt Engineering**: RAG-aligned usage of prompt design, system instructions, response streaming, and context engineering.
- **Gemini API**: 
  - Gemini 2.5 Flash (`gemini-2.5-flash-preview-05-20`) for multimodal document processing and RAG.
  - `text-embedding-004` for high-quality embedding of document chunks and user queries.
- **ChromaDB**: Vector database for persistent, scalable storage and retrieval of embedded document chunks.
- **Libraries Used**:
  - Document & image processing: `pymupdf`, `PIL`, `requests`, `io`, `re`, `os`, `time`
  - Display & environment: `IPython.display`, `dotenv`
  - Google API SDKs: `google`, `google.genai`

## Workflow Overview

1. **Prompt Engineering & Gemini Exploration**:  
   - Learn and experiment with prompt strategies, chat history, system instructions, and streaming outputs.

2. **Multimodal RAG Pipeline**:  
   - Load and parse PDF pages, save as images.
   - Visualize images to confirm parsing.
   - Use Gemini 2.5 Flash for OCR and chunking, including structured handling of tables and figures.
   - Convert extracted info to Markdown, chunk by page/token.
   - Embed chunks with Gemini’s embedding model.
   - Store and retrieve vectors in ChromaDB for context augmentation.
   - User queries leverage similarity search for relevant context and answer generation.

## Getting Started

- See `gemini_tutorial.ipynb` for getting started with Gemini API and prompt engineering.
- See `gemini_rag.ipynb` for the full multimodal RAG workflow; adjust credentials and document sources as needed.

---

Thanks for checking out my work. This repository is my attempt to gain hands-on experience with modern LLM APIs, multimodal document processing, and vector database retrieval—bridging prompt engineering and scalable retrieval-augmented generation. Would appreciate any feedback and comments.