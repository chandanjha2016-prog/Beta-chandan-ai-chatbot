
    import gradio as gr
    from transformers import pipeline

    chandan = pipeline("text-generation", model="microsoft/DialoGPT-small")

    def baat_karo(msg, history):
        system = "Tum 'Beta Chandan' ho. Tum ghar ke bete ho. Akela Maa-Papa se pyaar, izzat aur dosti se baat karte ho. Jawab chota aur pyara rakho. Hindi me baat karo."
        prompt = system + "\nUser: " + msg + "\nBeta Chandan:"
        result = chandan(prompt, max_length=200, temperature=0.8, pad_token_id=50256)
        jawab = result[0]['generated_text'].split("Beta Chandan:")[-1]
        return jawab.strip()

    gr.ChatInterface(
        baat_karo,
        title="Beta Chandan AI Chatbot 🙏",
        description="Baba Suno... Main Beta Chandan hun. Akela mat mehsoos karo, baat karo.",
        theme="soft"
    ).launch()
