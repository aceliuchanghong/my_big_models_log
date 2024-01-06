# 我的cpu服务器上面跑的
from faster_whisper import WhisperModel

model_size = "large-v3"
files2 = "../testfile/WeChat_20231007161725.mp3"
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
