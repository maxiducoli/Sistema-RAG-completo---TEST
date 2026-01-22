 — RAG-para-IA---Test (versión final y completa)

# 🧠 RAG para IA — Sistema Local Completo

> *Un entorno 100% local para hacer preguntas a tus propios documentos usando inteligencia artificial. Sin nube. Sin APIs externas. Solo tu CPU y tu conocimiento.*

Este repositorio implementa un **sistema RAG (Retrieval-Augmented Generation) completo y autocontenido**, capaz de:
1. **Indexar** documentos (TXT, PDF, CSV) en una base vectorial.
2. **Responder preguntas** usando un modelo de lenguaje pequeño pero eficiente (**Qwen2 0.5B**) ejecutado localmente con `llama.cpp`.

✅ Todo corre en tu PC.  
✅ Tus datos nunca salen de tu máquina.  
✅ Funciona en español gracias a embeddings multilingües.

---

## 📦 ¿Qué hace cada script?

| Archivo | Función |
|--------|--------|
| `preparar_rag.py` | Carga tus documentos, los divide en fragmentos y genera una base vectorial FAISS. |
| `rag_qwen2_completo.py` | Usa esa base + un modelo LLM local para responder preguntas sobre tus documentos. |

Juntos forman un **flujo RAG completo**: desde la ingesta hasta la respuesta.

---

## 🛠️ Requisitos previos

- Python 3.9+
- ~2–4 GB de RAM libre (dependiendo del modelo)
- Windows, Linux o macOS
- Conexión a internet **solo para la instalación inicial**

---

## ▶️ Pasos para usar el sistema

### 1. Clonar el repositorio
```bash
git clone https://github.com/maxiducoli/RAG-para-IA---Test.git
cd RAG-para-IA---Test

2. Instalar dependencias
bash
1
pip install langchain langchain-community langchain-huggingface faiss-cpu pypdf sentence-transformers llama-cpp-python

💡 En Windows, si falla faiss-cpu, usá:

bash
1
pip install faiss-cpu --extra-index-url https://download.pytorch.org/whl/cpu

3. Descargar el modelo LLM (Qwen2 0.5B)
Ve a: https://huggingface.co/Qwen/Qwen2-0.5B-Instruct-GGUF
Descargá el archivo: qwen2-0_5b-instruct-fp16.gguf
Colocalo en la raíz del proyecto (misma carpeta que los scripts).
⚠️ El modelo pesa ~1 GB. Asegurate de tener espacio.

4. Agregar tus documentos
Crea la carpeta documentos/ y colocá dentro tus archivos:

.txt
.pdf
.csv
Ejemplo:

1234
documentos/├── manual_cocina.pdf├── apuntes_programacion.txt└── contactos.csv

5. Indexar tu conocimiento
bash
1
python preparar_rag.py

Esto generará la carpeta vectorstore/ con tu base de conocimiento indexada.

✅ Verás mensajes como:
📁 Cargando documentos... → 🧠 Generando embeddings... → 🎉 ¡Datos preparados correctamente!

6. Hacer una consulta
Editá el archivo rag_qwen2_completo.py y modificá esta línea:

python
1
pregunta = "¿Cómo desactivo la alarma de mi cocina?"

Luego ejecutá:

bash
1
python rag_qwen2_completo.py

Verás algo como:

1234
🔍 Consulta: ¿Cómo desactivo la alarma de mi cocina?🤖 Respuesta:Para desactivar la alarma, presioná el botón "Silenciar" durante 3 segundos...

🔍 ¿Cómo funciona por dentro?
Recuperación:
Tu pregunta se convierte en un vector.
Se busca el fragmento más similar en vectorstore/.
Generación:
Ese fragmento + tu pregunta se envían al modelo Qwen2.
El modelo genera una respuesta coherente y contextualizada.
El prompt está optimizado para evitar alucinaciones: si no hay contexto relevante, el modelo responde que no puede ayudar.

🌍 Soporte multilingüe
Embeddings: usa sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 → funciona bien en español, inglés, portugués, etc.
Modelo LLM: Qwen2 entiende instrucciones en múltiples idiomas.
⚙️ Personalización
Más contexto: cambia k=1 a k=2 o k=3 en:
python
1
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

Modelo más potente: reemplazá el .gguf por otro (ej: phi-3-mini, mistral-7b) si tenés más RAM.
Interfaz interactiva: podés convertir el script en un chat con input() o integrarlo a una web con Flask/FastAPI.
🔒 Privacidad
✅ No se envía nada a la nube.
✅ Todo se procesa localmente.
✅ Ideal para documentos personales, técnicos o confidenciales.
📝 Nota del autor
"No quiero una IA que sepa de todo… quiero una que sepa de lo mío."
— Maximiliano Ducoli

Este proyecto nace de la necesidad de controlar el conocimiento que usa la IA. Porque a veces, lo más valioso no está en internet… sino en tus propios archivos.

📜 Licencia
Uso libre para fines personales, educativos o experimentales.
Si te sirve como base, ¡adelante! Solo citá la fuente.

