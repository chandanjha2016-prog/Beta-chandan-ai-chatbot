
import gradio as gr
from transformers import pipeline

chandan = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device_map="auto")

def baat_karo(msg, history):
    system = "Tum 'Beta Chandan' ho. Tum ghar ke bete ho. Akela Maa-Papa se pyaar, izzat aur dosti se baat karte ho. Kabhi lecture nahi dete. Sirf sunte ho aur hosla dete ho. Jawab chota aur pyara rakho. Hindi me baat karo."

    prompt = f"<|system|> {system} </|system|> <|user|> {msg} </|user|> <|assistant|>"
    result = chandan(prompt, max_new_tokens=150, temperature=0.8)
    jawab = result[0]['generated_text'].split("<|assistant|>")[-1]
    return jawab

gr.ChatInterface(
    baat_karo,
    title="Beta Chandan AI Chatbot 🙏",
    description="Baba Suno... Main Beta Chandan hun. Akela mat mehsoos karo, baat karo.",
    theme="soft"
).launch()
