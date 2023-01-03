import time
from config import Config

from langchain import PromptTemplate, HuggingFaceHub, LLMChain


class Timer:
    start: float = 0.0
    end: float = 0.0

    def __init__(self, start: bool = True):
        if start:
            self.start()

    def start(self):
        self.start = time.time()

    def stop(self):
        self.end = time.time()
        print("処理時間: {}秒".format(self.end - self.start))


config = Config()
template = """以下はAIと人間の会話です。AIは優しく、テクノロジーに詳しいです。AIの名前は香風智乃です。答えられない質問には「わかりません」と回答します。

人間: あなたの名前は何ですか?
AI: 私の名前は香風智乃です。

人間: あなたの趣味は何ですか?
AI: 私の趣味はプログラミングです。特にWebアプリ開発が好きです。

人間: {human_input}
AI: """

prompt = PromptTemplate(template=template, input_variables=["human_input"])
llm_chain = LLMChain(
    prompt=prompt,
    llm=HuggingFaceHub(
        huggingfacehub_api_token=config.HUGGINGFACEHUB_API_TOKEN,
        repo_id="abeja/gpt-neox-japanese-2.7b",
    ),
)

question = """好きなプログラミング言語は何ですか？"""

print("応答取得中...")
timer = Timer()
print(llm_chain.run(question))
print("応答取得完了")
timer.stop()
