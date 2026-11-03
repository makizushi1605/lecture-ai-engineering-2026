# 第3回 解答

## 演習
※"LoRA とQLoRAの違いは？"という質問を行った場合についての内容を記載

- 第1回（素のLLM）とエージェントの回答の違い：
素のLLMでは回答生成時にフォーマットの指定がない自由形式での回答に対して、エージェントの回答では呼び出す関数を指定して出力形式や内容を制御している。
具体的には、エージェントでは回答作成時、"search_glossary"で検索条件を絞り込み、さらにglossary.jsonで記載している内容にマッピングさせて出力している
そのため、出力フォーマットのゆらぎが限りなく抑制できている。

- `--trace` で見えたツール呼び出し（ツール名と引数）：
search_glossary({'query': 'LoRA'})
search_glossary({'query': 'QLoRA'})

- 1つの質問での LLM 呼び出し回数（`requests`）：
2回

- 追加したツールと、docstring に書いた説明：
追加したツール：make_quiz(lecture: int)
docstring に書いた説明：
    """指定した回の用語から1つを選び、
    確認問題と答えを返す。
    
    「第2回の確認問題を出して」のように、
    復習用の問題を求められたときに使う。
    """

## 宿題

- 取り組んだレベル：基礎
- やったこと：make_quiz() で出した問題の解説を出力するmake_answer()の関数を作成し、agentの呼び出し時に、"第2回の内容から確認問題を1問出して、答えを解説して"と入力してトレース
- 結果：【問題】に加え、【答えと解説】が出力された。
出力結果は、
**【答えと解説】**
* **答え**: **PEFT (Parameter-Efficient Fine-Tuning / パラメータ効率の良い微調整)**
* **解説**: 
  PEFTは、LLMの全パラメータを更新する従来のファインチューニングに比べ、ごく一部のパラメータだけを効率よく学習させることで、メモリや計算コストを大幅に削減する手法の総称です。代表例として、LoRAなどが挙げられます。

（関連する回：第2回）

--- trace ---
[tool call]   make_quiz({'lecture': 2})
[tool return] make_quiz -> None…
[tool call]   make_answer({'lecture': 2})
[tool return] make_answer -> None…
[usage] RunUsage(cost=Decimal('0.0009398'), details={'text_prompt_tokens': 1416}, input_text_tokens=1416, input_tokens=1416, output_tokens=206, requests=3, tool_calls=2)
となった。

- 気づき・疑問：
入れ子のツールでもmake_quiz　⇒　make_answerの順で問題なく動作することに気がついた。