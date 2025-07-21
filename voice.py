import sys
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import CosyVoice2
from cosyvoice.utils.file_utils import load_wav
import torchaudio
def voice(text):
    cosyvoice = CosyVoice2('pretrained_models/CosyVoice2-0.5B', load_jit=False, load_trt=False, fp16=False)

    # NOTE if you want to reproduce the results on https://funaudiollm.github.io/cosyvoice2, please add text_frontend=False during inference
    # zero_shot usage
    
    prompt_speech_16k = load_wav('./asset/prompt.mp3', 16000)
    # instruct usage
    for i, j in enumerate(cosyvoice.inference_instruct2(text, 'speak in a fine classy English accent and slowly to make sure the user can feel relaxed', prompt_speech_16k, stream=False)):
        torchaudio.save('audioFiles/instruct_{}.wav'.format(i), j['tts_speech'], cosyvoice.sample_rate)

# bistream usage, you can use generator as input, this is useful when using text llm model as input
# NOTE you should still have some basic sentence split logic because llm can not handle arbitrary sentence length
