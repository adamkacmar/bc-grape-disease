import gradio as gr


def predict(image):
    return "Hello, " + image


demo = gr.Interface(predict, gr.Image(), "image")

demo.launch()
