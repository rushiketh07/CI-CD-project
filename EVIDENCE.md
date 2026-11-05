# Evaluation evidence checklist

This local project contains the source and configuration deliverables. Evidence that must come from a real GitHub account or OpenShift cluster is not simulated here.

## Task 1 — README

Capture the public URL after publishing this directory, for example `https://github.com/<owner>/<repository>/blob/main/README.md`.

## Task 2 — GitHub Actions

The workflow is `.github/workflows/workflow.yml`. Push to GitHub and capture the Actions run page and its successful step log. A local run is not a GitHub Actions run.

## Task 3 — Tekton Tasks

The complete task definitions are in `.tekton/tasks.yml`. Capture the public file URL after publishing.

## Task 4 — PVC screenshot

In OpenShift Web Console, select the project, open **Storage → PersistentVolumeClaims**, select the pipeline workspace PVC, and capture its details. The image must visibly show Name, **Bound** status, StorageClass, access mode (`ReadWriteOnce` or `ReadWriteMany`), and capacity. Save as `oc-pipelines-console-pvc-details.png`.

## Task 5 — GitHub Actions log

Capture the actual successful run log with `Set up job`, checkout, Python setup, dependency installation, flake8, nosetests/coverage, and `Complete job` / success. `SAMPLE_LOGS.md` provides a clearly labeled format example, not proof of execution.

## Task 6 — Pipeline details screenshot

Open **Pipelines → Pipelines → oc-pipelines-oc-final** in the selected project and capture the task flow: `fetch-repository → cleanup → lint → test → build-image → deploy`.

## Task 7 — PipelineRun screenshot

Open the PipelineRuns view and select the completed run. Capture green success indicators for all six tasks and the **Succeeded/Completed** result. Save as `oc-pipelines-oc-green.png`.

## Task 8 — application logs

After a real deployment, capture `oc logs deployment/openshift-ci-final` and a health request such as `curl -i https://<route>/health`. The app reports its database status as `not-configured` unless `DATABASE_STATUS` is set; it does not connect to a database. Do not claim database connectivity without adding and configuring a database.
