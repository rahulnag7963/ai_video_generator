from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy import *
from PIL import Image
import os

def movie(image_paths, output_path, size=(1920, 1080)):
    # Create output directory
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    processed_images = []
    img_arr = []
    audio_dir = os.path.join(os.path.dirname(__file__), "audioFiles")
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav') or f.endswith('.mp3')]
    empty = AudioFileClip("10.mp3");    
        
    if not audio_files:
        raise ValueError("No audio files found in audioFiles directory")
            
        
    processed_audio = []
    for audio_file in audio_files:
        audio_path = os.path.join(audio_dir, audio_file)
        audio_clip = AudioFileClip(audio_path)
        # Concatenate empty audio to each clip
        extended_clip = concatenate_audioclips([audio_clip, empty])
        processed_audio.append(extended_clip)
        
    voice = concatenate_audioclips(processed_audio)    
    time =  voice.duration
    for img_path in image_paths:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            resized_path = f"temp_{os.path.basename(img_path)}"
            img.resize(size).save(resized_path)
    
            img_arr.append(resized_path)       
            img_clip = ImageClip(resized_path, duration=time)
            img_clip = img_clip.with_effects([vfx.FadeIn(1), vfx.FadeOut(1)])
            processed_images.append(img_clip)
    
    try:
        print(processed_images)
        clip = concatenate_videoclips(processed_images)
        music = AudioFileClip("music.mp3")
        music = music.with_effects([afx.MultiplyVolume(0.05)])        
        
        final_audio = CompositeAudioClip([voice, music])
        clip.audio=final_audio.subclipped(0, clip.duration)
        
        # Write video directly
        clip.write_videofile(output_path, fps=24)
    finally:
        # Cleanup temp files
        for img in img_arr:
            if os.path.exists(img) and img.startswith('temp_'):
                os.remove(img) 
