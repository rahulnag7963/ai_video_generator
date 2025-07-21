import os
from torch import autocast
from groq import Groq
from moviepy import *

from diffusers import DiffusionPipeline
def picture(title):
    #GROQ KEY USE YOUR OWN KEY
    API_KEY="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"
    client = Groq(
        api_key=API_KEY,
    )

    #SAVE_PATH HERE THE IMAGE WILL BE SAVED
    SAVE_PATH = r"C:\Users\Rahul\Desktop\shortform_videoGenerator\CosyVoice"

    model = "stabilityai/stable-diffusion-xl-base-1.0"

    pipeline = DiffusionPipeline.from_pretrained(model)
    pipeline.to("cuda")


    prompt = f":{title}"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": title+""": 
                Using this script, generate a single sentence description for the script.
                The sentence should not exceed 73 characters.
                The sentence should be a single line.
                The sentence shoud be a description of the script.
                
                example: 
                "vibrant sunset over a bustling cityscape, with warm orange and pink hues"
                """,
            }
        ],
        model="llama3-8b-8192",
    )
    prompt = chat_completion.choices[0].message.content
    images = pipeline(
        prompt=prompt,
        height=1080,
        width=1920,
        num_inference_steps=25,
    ).images[0]
    image_path = os.path.join(SAVE_PATH, f"image{1}.png")
    images.save(image_path)