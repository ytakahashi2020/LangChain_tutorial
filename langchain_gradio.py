import os
from langchain.tools import ElevenLabsText2SpeechTool
from elevenlabs import set_api_key
import gradio as gr

set_api_key(os.environ.get("ELEVENLABS_API_KEY"))
# Initialize ElevenLabsText2SpeechTool
tts = ElevenLabsText2SpeechTool()


def generate_speech(text_to_speech):
    speech_file = tts.run(text_to_speech)
    return speech_file

demo = gr.Interface(
    fn = generate_speech,
    inputs = gr.Textbox(lines=2, placeholder="Text to speech", label="Enter Text"),
    outputs = gr.Audio(label="Generated Speech"),
)

if __name__ == "__main__":
    demo.launch()

  