# 🧠 RAG para IA — Sistema Local Completo

> *Un entorno 100% local para hacer preguntas a tus propios documentos usando inteligencia artificial. Sin nube. Sin APIs externas. Solo tu CPU y tu conocimiento.*

Este repositorio implementa un **sistema RAG (Retrieval-Augmented Generation) completo y autocontenido**, capaz de:
1. **Indexar** documentos (TXT, PDF, CSV) en una base vectorial.
2. **Responder preguntas** usando un modelo de lenguaje pequeño pero eficiente (**Qwen2 0.5B**) ejecutado localmente con `llama.cpp`.

Todo corre en tu PC. Tus datos nunca salen de tu máquina.

---

## 🔧 Componentes del sistema

| Etapa | Tecnología | Descripción |
|------|-----------|-------------|
| **Indexación** | LangChain + FAISS + Hugging Face | Carga documentos y genera embeddings multilingües |
| **Modelo LLM** | Qwen2 0.5B (GGUF) + `LlamaCpp` | Modelo ligero, rápido y capaz, optimizado para CPU |
| **Recuperación** | FAISS | Busca los fragmentos más relevantes para cada pregunta |
| **Generación** | Prompt optimizado + cadena LangChain | Combina contexto y pregunta para generar respuestas útiles |

---

## 📂 Estructura del proyecto



---

## ▶️ Cómo usarlo

### 1. Instalá las dependencias
```bash
pip install langchain langchain-community langchain-huggingface faiss-cpu pypdf sentence-transformers llama-cpp-python

bajar modelo qwen2-0_5b-instruct-fp16.gguf (yo los bajo directamente de LLM Studio o OLLama)


