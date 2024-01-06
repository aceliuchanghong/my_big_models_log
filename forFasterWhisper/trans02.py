# 我的本机上面跑的
from faster_whisper import WhisperModel
import pysubs2

files1 = "../testfile/2.wav"
files2 = "../testfile/WeChat_20231007161725.mp3"
srt_file_name = '../testfile/out/test'
# model_size = "large-v3"
path = r'C:\Users\lawrence\Documents\large_v3'
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
