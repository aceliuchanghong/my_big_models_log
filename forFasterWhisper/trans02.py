# 我的本机上面跑的
from faster_whisper import WhisperModel

# model_size = "large-v3"
path = r'C:\Users\lawrence\Documents\large_v3'
# Run on GPU with FP16
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="float16", local_files_only=True)

# or run on GPU with INT8
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="int8_float16", local_files_only=True)
# or run on CPU with INT8
model = WhisperModel(model_size_or_path=path, device="cpu", compute_type="int8", local_files_only=True)

segments, info = model.transcribe("../testfile/2.wav", language='zh', vad_filter=True,
                                  vad_parameters=dict(min_silence_duration_ms=1000), beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
