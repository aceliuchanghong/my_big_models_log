# 我的公司上面跑的
from faster_whisper import WhisperModel

from config import config

model_size = config.model_path
files2 = config.test_files1
# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe(audio=files2, language='zh', vad_filter=True,
                                  vad_parameters=dict(min_silence_duration_ms=1000), beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
