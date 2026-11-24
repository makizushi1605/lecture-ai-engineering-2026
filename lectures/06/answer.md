# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary:glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase': 'Amazon S3 Versioning', 'topics': ['general']})
- 気づき・疑問：
質問ごとに最適なツールが呼ばれている。また、STEP 4ではawsにAPI接続し、適切に結果を返していることから、azureやgcp等他のクラウドサービスでも同様のことができるのではと気が付いた。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎
- やったこと：server.tool()(tools.get_lecture_summary)をmcpサーバーのツールに追加し、MCPサーバー経由でget_lecture_summaryが呼ばれることを確認する。
- 結果：
uv run python -m app.mcp_agent --trace \ "第2回では何を学びますか？ 
と入力すると、
[tool call]   glossary_get_lecture_summary({'lecture': 2})
と出力され、MCPサーバー経由でget_lecture_summaryが呼ばれることを確認した。

- 気づき・疑問：
MCPサーバー経由で呼ばれた場合、利用トークン数やコストは増加するのか疑問を持った。
