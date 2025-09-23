# 📝 AI Writing Assistant

Full-stack application that uses a **Large Language Model (LLM)** (e.g., OpenAI GPT) to rewrite text in different writing styles: **Professional, Casual, Polite, and Social Media**.

![Vista previa de la aplicación](./app.png)

---

## 🚀 Technology Stack

### Backend
- **FastAPI**: Modern Python framework for APIs.
- **OpenAI**: LLM (e.g., gpt-4o-mini) for text processing.
- **Pydantic**: Data validation.
- **Pytest**: Testing framework.
- **Docker**: Containerization.

### Frontend
- **React 18**: Modern frontend with hooks.

---

## 🔧 Prerequisites
- Python 3.11+  
- Node.js 16+  
- Docker (optional, but recommended for backend)  
- **Azure OpenAI** environment variables configured in `.env` in the **backend** folder (not included in repo):

```env
AZURE_OPENAI_API_KEY=''
AZURE_OPENAI_ENDPOINT=''
AZURE_OPENAI_DEPLOYMENT=''
```

---

## ⚙️ Installation and Execution Instructions

### 1. Clone the repository
```bash
git clone https://github.com/LxMera/writing_assistant.git
```

### 2. Backend (FastAPI with Docker)
From the project root:

```bash
docker build -t writing_assistant_backend ./backend
docker run -d -p 8000:8000 --name writing_backend writing_assistant_backend
```
The backend will be available at: http://localhost:8000/docs

### 3. Frontend (React)
Go to the frontend folder:

```bash
cd frontend
npm install   # only the first time
npm start
```

The frontend will be available at: http://localhost:3000

---

## 📄 Assumptions

- The `.env` file with credentials is not included in the repository.
- The frontend expects the backend to be running on http://localhost:8000.
- This project is designed for local test/demo environment.

# 📝 Asistente de Escritura con IA

Aplicación full-stack que utiliza un **Large Language Model (LLM)** (ej. OpenAI GPT) para reformular texto en diferentes estilos de escritura: **Profesional, Casual, Cortés y Redes Sociales**.  

---

## 🚀 Stack Tecnológico

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
- Variables de entorno de **Azure OpenAI** configuradas en `.env` en la carpeta **backend** (no incluidas en el repo):

```env
AZURE_OPENAI_API_KEY=''
AZURE_OPENAI_ENDPOINT=''
AZURE_OPENAI_DEPLOYMENT=''
```

---

## ⚙️ Instrucciones de Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/LxMera/writing_assistant.git
```

### 2. Backend (FastAPI con Docker)
Desde la raíz del proyecto:

```bash
docker build -t writing_assistant_backend ./backend
docker run -d -p 8000:8000 --name writing_backend writing_assistant_backend
```
El backend quedará disponible en: http://localhost:8000/docs

### 3. Frontend (React)
Ir a la carpeta del frontend:

```bash
cd frontend
npm install   # solo la primera vez
npm start
```

El frontend quedará disponible en: http://localhost:3000

📄 Supuestos

- El archivo .env con credenciales no se incluye en el repositorio.
- El frontend espera que el backend esté corriendo en http://localhost:8000.
- Este proyecto está diseñado para entorno local de prueba/demostración.
