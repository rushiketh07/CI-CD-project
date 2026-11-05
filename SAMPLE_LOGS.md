# Illustrative log formats (not captured execution evidence)

These examples show the requested output shape. They are not output from GitHub Actions or an OpenShift cluster. Replace them with captured logs after running the workflow and deploying the application.

## Task 5 — GitHub Actions

```text
2026-11-05T09:00:00.0000000Z ##[group]Set up job
2026-11-05T09:00:02.0000000Z ##[endgroup]
2026-11-05T09:00:03.0000000Z ##[group]Run actions/checkout@v3
2026-11-05T09:00:04.0000000Z Syncing repository
2026-11-05T09:00:05.0000000Z ##[endgroup]
2026-11-05T09:00:06.0000000Z ##[group]Set up Python environment
2026-11-05T09:00:08.0000000Z Python 3.12.x
2026-11-05T09:00:08.0000000Z ##[endgroup]
2026-11-05T09:00:09.0000000Z ##[group]Install dependencies
2026-11-05T09:00:15.0000000Z Successfully installed Flask gunicorn flake8 nose-py3 coverage
2026-11-05T09:00:15.0000000Z ##[endgroup]
2026-11-05T09:00:16.0000000Z ##[group]Run Lint check (flake8)
2026-11-05T09:00:17.0000000Z Process completed with exit code 0.
2026-11-05T09:00:17.0000000Z ##[endgroup]
2026-11-05T09:00:18.0000000Z ##[group]Run Unit tests (nosetests)
2026-11-05T09:00:19.0000000Z ..
2026-11-05T09:00:19.0000000Z Name     Stmts   Miss  Cover
2026-11-05T09:00:19.0000000Z app.py      14      0   100%
2026-11-05T09:00:19.0000000Z ----------------------------------------------------------------------
2026-11-05T09:00:19.0000000Z Ran 2 tests in 0.01s
2026-11-05T09:00:19.0000000Z OK
2026-11-05T09:00:19.0000000Z ##[endgroup]
2026-11-05T09:00:20.0000000Z ##[group]Complete job
2026-11-05T09:00:20.0000000Z Job succeeded (exit code 0)
2026-11-05T09:00:20.0000000Z ##[endgroup]
```

## Task 8 — OpenShift application logs

```text
$ oc logs deployment/openshift-ci-final
[2026-11-05 09:10:02 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2026-11-05 09:10:02 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
[2026-11-05 09:10:02 +0000] [1] [INFO] Using worker: sync
[2026-11-05 09:10:02 +0000] [7] [INFO] Booting worker with pid: 7
INFO:sample-service:Application configured; database status=not-configured
$ curl -i http://openshift-ci-final:8080/health
HTTP/1.1 200 OK
Content-Type: application/json
{"database":"not-configured","status":"ok"}
```
