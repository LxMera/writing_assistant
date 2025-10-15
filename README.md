# 📝 AI Writing Assistant

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
- **FastAPI**: Framework moderno de Python para APIs.
- **OpenAI**: LLM (ej. gpt-4o-mini) para procesamiento de texto.
- **Pydantic**: Validación de datos.
- **Pytest**: Framework de pruebas.
- **Docker**: Containerización.

### Frontend
- **React 18**: Frontend moderno con hooks.

---

## 🔧 Requisitos Previos
- Python 3.11+  
- Node.js 16+  
- Docker (opcional, pero recomendado para el backend)  
- Variables de entorno de **Azure OpenAI**, **Openai** y **Anthropic (Claude)** configuradas en `.env` en la carpeta **backend** (no incluidas en el repo):

```env
AZURE_OPENAI_API_KEY=''
AZURE_OPENAI_ENDPOINT=''
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
OPENAI_API_KEY = ''
OPENAI_MODEL = 'gpt-4o-mini'
ANTHROPIC_API_KEY = ''
CLAUDE_MODEL = 'claude-sonnet-4-20250514'
```

---

## ⚙️ Instrucciones de Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/LxMera/writing_assistant.git
```

### 2. Backend, frontend and nginx
Desde la raíz del proyecto (writing_assistant):

```bash
docker compose up --build
```
La aplicación quedará disponible en: http://localhost
Inicialmente solicitará el usuario y contraseña, que, para este ejemplo práctico son: admin y admin123
Una vez realizado el login se accederá a la interfaz, tal como se muestra en la imagen.
