# rag_qwen2_completo.py

from langchain_community.llms import LlamaCpp
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# === CONFIGURACIÓN ===

# Ruta al modelo .gguf
MODEL_PATH = "./qwen2-0_5b-instruct-fp16.gguf"

# Carpeta donde está tu vectorstore FAISS
VECTORSTORE_PATH = "vectorstore"

# === CARGAR MODELO LOCAL ===

llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_ctx=2048,           # Tamaño máximo del contexto
    n_batch=512,          # Tamaño del batch
    n_threads=4,          # Núcleos de CPU a usar
    f16_kv=True,          # Usar FP16 para mayor velocidad
    verbose=False         # No mostrar logs internos
)

# === CARGAR EMBEDDINGS Y VECTORSTORE ===

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

vectorstore = FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

# === PROMPT OPTIMIZADO ===

template = """Usa la siguiente información recuperada para responder de forma clara y útil a la pregunta del usuario.
Si no hay información suficiente, responde que no puedes ayudar con eso.

Contexto:
{clean_context}

Pregunta:
{question}

Respuesta:"""

prompt = PromptTemplate(template=template, input_variables=["clean_context", "question"])

# === CADENA DE INFERENCIA ===

chain = LLMChain(llm=llm, prompt=prompt)

# === FUNCIONES AUXILIARES ===

def limpiar_contexto(contexto):
    lineas = [linea for linea in contexto.split("\n") if not linea.startswith(("Pregunta:", "Respuesta:"))]
    return "\n".join(lineas)

def hacer_consulta(pregunta):
    # Recuperar documentos relevantes
    docs = retriever.invoke(pregunta)
    contexto = "\n".join([doc.page_content for doc in docs])

    # Limpiar contexto
    clean_context = limpiar_contexto(contexto)

    # Generar respuesta
    respuesta = chain.invoke({"clean_context": clean_context, "question": pregunta})
    return respuesta["text"]

# === EJEMPLO DE USO ===

if __name__ == "__main__":
    pregunta = "¿Cómo desactivo la alarma de mi cocina?"
    print("🔍 Consulta:", pregunta)
    resultado = hacer_consulta(pregunta)
    print("\n🤖 Respuesta:")
    print(resultado)