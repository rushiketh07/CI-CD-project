# OpenShift CI/CD Pipeline Final Project

[![CI workflow configured](https://img.shields.io/badge/GitHub%20Actions-configured-lightgrey)](.github/workflows/workflow.yml)

## Architecture

This repository contains a small Flask HTTP service, a GitHub Actions lint and test workflow, and Tekton Tasks/Pipeline for fetch, cleanup, lint, test, image build, and deployment to OpenShift. The service listens on port 8080 and exposes `/health` for Kubernetes probes. The Tekton workspace is intended to be backed by a PersistentVolumeClaim.

```text
Git push / pull request -> GitHub Actions -> flake8 -> nosetests + coverage
OpenShift PipelineRun -> fetch-repository -> cleanup -> lint -> test
                    -> build-image -> deploy -> Service / Route
```

## Run locally

Use Python 3.12, then run:

```sh
python -m pip install -r requirements.txt
python -m flake8 app.py test_app.py
nosetests --with-coverage --cover-package=app --cover-min-percentage=100
gunicorn --bind 0.0.0.0:8080 app:app
```

## GitHub Actions

The workflow is at `.github/workflows/workflow.yml`. It runs on pushes and pull requests, installs the pinned dependencies, runs flake8, then runs nosetests with coverage.

## OpenShift setup

1. Create or select the `openshift-ci-final` project and ensure the internal image registry is available.
2. Apply the Tasks and Pipeline: `oc apply -f .tekton/tasks.yml -f .tekton/pipeline.yml`.
3. Apply `pvc.yaml` and bind the PipelineRun's `source` workspace to `oc-pipelines-workspace`. It requests 1Gi with ReadWriteOnce and uses the cluster's default StorageClass.
4. Start a PipelineRun with `repository-url`, `revision`, `image-url`, and the PVC workspace binding. Ensure the service account can push to the target image and update Deployments. The Buildah task also needs a cluster-approved SCC that permits its privileged step.
5. Apply `deployment.yaml` if the deploy task's deployment does not already exist.

## Build status

The badge above reports that the workflow is configured. A repository-specific live status badge and public GitHub file URLs become available after this project is pushed to a public GitHub repository. No public repository URL or live run is claimed in this local deliverable. `SAMPLE_LOGS.md` contains illustrative output formats, not captured run evidence.
