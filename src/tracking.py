"""MLflow tracking helpers, shared by every guardrail.

Why this file exists:
    Every experiment (injection model, PII rules, router rules) should be logged
    the same way, so runs are easy to compare. Keeping the setup in one place
    means we never repeat it in each notebook or script.

Usage:
    from src.tracking import start_run

    with start_run("injection-detector", run_name="tfidf-logreg-v1") as run:
        mlflow.log_param("C", 1.0)
        mlflow.log_metric("recall", 0.93)
"""

import os

# Where MLflow stores runs. "./mlruns" is a local folder (ignored by Git).
# Later (V1.4 / V2.0) set MLFLOW_TRACKING_URI to a server and nothing else changes.
DEFAULT_TRACKING_URI = "./mlruns"

PROJECT_NAME = "ai-security"
PROJECT_VERSION = "v1.0"


def start_run(experiment: str, run_name: str | None = None):
    """Start an MLflow run inside the experiment `ai-security/<experiment>`.

    Returns the run, which you use in a `with` block so it closes itself.
    Also tags the run with the project version so you can filter by V1.0, V1.1...
    """
    import mlflow  # imported here so the rest of the project works without MLflow

    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", DEFAULT_TRACKING_URI))
    mlflow.set_experiment(f"{PROJECT_NAME}/{experiment}")
    run = mlflow.start_run(run_name=run_name)
    mlflow.set_tag("project_version", os.getenv("PROJECT_VERSION", PROJECT_VERSION))
    return run
