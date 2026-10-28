"""V1.0 smoke tests: prove the project is wired up correctly."""

import importlib

import pytest


@pytest.mark.parametrize(
    "module",
    [
        "src.guardrails.injection",
        "src.guardrails.pii",
        "src.guardrails.router",
        "src.pipeline",
        "src.tracking",
    ],
)
def test_modules_import(module):
    """Every module in the skeleton can be imported."""
    importlib.import_module(module)


def test_mlflow_logs_a_run(tmp_path, monkeypatch):
    """MLflow can create an experiment and log a param + metric."""
    mlflow = pytest.importorskip("mlflow")
    monkeypatch.setenv("MLFLOW_TRACKING_URI", f"sqlite:///{(tmp_path / 'mlflow.db').as_posix()}")

    from src.tracking import start_run

    with start_run("smoke-test", run_name="hello") as run:
        mlflow.log_param("hello", "world")
        mlflow.log_metric("answer", 42)

    saved = mlflow.get_run(run.info.run_id)
    assert saved.data.params["hello"] == "world"
    assert saved.data.metrics["answer"] == 42
    assert saved.data.tags["project_version"] == "v1.0"
