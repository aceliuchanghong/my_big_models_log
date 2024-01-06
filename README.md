### my_big_models_log

the log of doing faster-whisper model

### purpose

build a saas in server then give api,so i can use

* 语音转文字==>faster-whisper git@github.com:SYSTRAN/faster-whisper.git
* 文字转语音==>TTS没想好看谁的
* 声音克隆
* llm==>ChatGLM git@github.com:THUDM/ChatGLM3.git
* sd的lora也可以试试==>之后再说

### install
#pip freeze > requirements.txt

git clone git@github.com:aceliuchanghong/my_whisper_log.git

conda create -n FasterWhisper python=3.10

conda activate FasterWhisper

pip install -r requirements.txt

## 查看cuda版本和占用情况
nvidia-smi