from types import SimpleNamespace

from app import ask as ask_module


def test_ask_prints_token_usage_and_returns_response(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=8),
        text="回答",
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )
    monkeypatch.setattr(ask_module.genai, "Client", lambda **kwargs: client)

    assert ask_module.ask("質問") == "回答"
    assert "[トークン] 入力: 12, 出力: 8" in capsys.readouterr().out


def test_ask_handles_missing_token_usage(monkeypatch, capsys):
    response = SimpleNamespace(usage_metadata=None, text="回答")
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )
    monkeypatch.setattr(ask_module.genai, "Client", lambda **kwargs: client)

    assert ask_module.ask("質問") == "回答"
    assert "[トークン] 入力: 不明, 出力: 不明" in capsys.readouterr().out