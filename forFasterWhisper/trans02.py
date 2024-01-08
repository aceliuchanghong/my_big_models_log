# 我的本机上面跑的
from faster_whisper import WhisperModel
import pysubs2

from config import config

files1 = config.test_files1
files2 = config.test_files2
srt_file_name = config.srt_file_name
# model_size = "large-v3"
path = config.model_path
# Run on GPU with FP16
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="float16", local_files_only=True)

# or run on GPU with INT8
# 启动大概20s,跑files2大概80s
model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="int8_float16", local_files_only=True)
# or run on CPU with INT8
# model = WhisperModel(model_size_or_path=path, device="cpu", compute_type="int8", local_files_only=True)

segments, info = model.transcribe(audio=files1, language='zh', vad_filter=True,
                                  vad_parameters=dict(min_silence_duration_ms=1000), beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

results = []
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    segment_dict = {'start': segment.start, 'end': segment.end, 'text': segment.text}
    results.append(segment_dict)

subs = pysubs2.load_from_whisper(results)
# save srt file
subs.save(srt_file_name + '.srt')
# save ass file
# subs.save(file_name + '.ass')
