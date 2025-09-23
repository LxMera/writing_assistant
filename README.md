# AI Writing Assistant

A full-stack application that uses OpenAI's GPT to rephrase text in different writing styles (Professional, Casual, Polite, Social Media).

## Features

### Base Features ✅
- **Frontend**: ReactJS with modern hooks and components
- **Backend**: FastAPI with Python
- **AI Integration**: OpenAI gpt-4o-mini
- **Writing Styles**: Professional, Casual, Polite, Social Media
- **Process Control**: Disable input during processing, cancel button
- **Error Handling**: Graceful error handling and user feedback

### Bonus Features ✅
- **Streaming Output**: Real-time text generation with word-by-word streaming
- **Separate Text Areas**: Each writing style in its own dedicated area
- **Production-Grade UI**: Clean, modern, responsive design
- **Modern Framework Features**: React hooks, async/await, modern ES6+
- **Modular Architecture**: Well-structured components and services
- **Testing**: Unit and integration tests
- **Containerization**: Docker support for backend
- **Accessibility**: ARIA labels, keyboard navigation, high contrast support

## Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **OpenAI**: gpt-4o-mini for text processing
- **Pydantic**: Data validation
- **Pytest**: Testing framework
- **Docker**: Containerization

### Frontend
- **React 18**: Modern React with hooks
- **Axios**: HTTP client
- **CSS3**: Modern styling with gradients, animations
- **Jest**: Testing framework

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 16+
- Docker (optional)
- OpenAI API key

### Backend Setup

1. **Clone the repository**
```bash
   git clone <repository-url>
   cd writing_assistant/backend