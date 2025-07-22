import os
from pyt2s.services import stream_elements
from groq import Groq

def shortForm(script):
    API_KEY="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"

    client = Groq(
        api_key=API_KEY,
    )
    print('Welcome to the Short Form Script Generator!')
    videoTitle = input("Enter the type of meditation of the video: ")

    msg =f"""    
Write a guided meditation script for a 5-10 minute YouTube video. The meditation should focus on {videoTitle}. The script should include:

1.) A brief and calming introduction (2 sentences) to set the intention 1 minute or 1000 characters long.
2.) Gentle breathwork guidance to help the listener relax 4000 characters or 4 minutes long.
3.) A visualization or mindfulness exercise that aligns with the theme 5000 chracters or 5 minutes long should be the bulk of the meditation script.
4.) A gradual return to awareness with soft closing words 1000 characters or 1 minute long.

The language should be soothing, with a steady and measured pace. 
The tone should be warm, inviting, and meditative.
At all costs FOLLOW THE INTRUCIONS BELOW: 
1.) Avoid saying in the beginning "Here is a guided meditation narration for a 10 minute YouTube video" or anything similair. 
2.) Ensure that each paragraph is separated by a blank line to improve readability for text-to-speech. 
3.) The script must be between 9500-10500 characters and should fit within a 10 to 15 minute audio format.
4.) Avoid use of square brackets or parentheses in the script. If a pause is needed, create a space.
5.) Avoid saying: "Soothing music plays in the background" or similar phrases. The music will be added later.

Here is an example of what the script should look like:
{script}

"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": msg,
            }, 
            {
                "role": "user",
                "content": "Create a Youtube guided meditation narration",
            }
        ],
        model="gemma2-9b-it",
    )
    s2 = chat_completion.choices[0].message.content
    print(s2)
   

    return s2
