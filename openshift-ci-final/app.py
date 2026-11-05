"""Small Flask service used by the OpenShift CI/CD final project."""

import logging
import os

from flask import Flask, jsonify

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger("sample-service")


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(service="openshift-ci-final", status="ok")

    @app.get("/health")
    def health():
        database_status = os.getenv("DATABASE_STATUS", "not-configured")
        return jsonify(status="ok", database=database_status), 200

    return app


app = create_app()
logger.info(
    "Application configured; database status=%s",
    os.getenv("DATABASE_STATUS", "not-configured"),
)
