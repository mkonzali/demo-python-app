from __future__ import annotations
import os
from datetime import datetime
from flask import Flask, jsonify, render_template, request

def create_app() -> Flask:
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Build metadata injectée par la CI
    BUILD_INFO = {
        "VERSION": os.getenv("APP_VERSION", "0.1.0"),
        "GIT_SHA": os.getenv("GIT_SHA", "dev"),
        "BUILD_DATE": os.getenv("BUILD_DATE", datetime.utcnow().isoformat() + "Z"),
        "IMAGE": os.getenv("IMAGE", "local/demoapp"),
        "ENV": os.getenv("APP_ENV", "dev"),
    }

    @app.get("/healthz")
    def health():
        return jsonify(status="ok", time=datetime.utcnow().isoformat() + "Z")

    @app.get("/api/info")
    def info():
        return jsonify(
            name="Demo Python App",
            description="Training app for Tekton labs",
            build=BUILD_INFO,
            client=request.headers.get("User-Agent", "unknown"),
        )

    @app.get("/")
    def index():
        # Affiche les infos build côté UI
        return render_template("index.html", build=BUILD_INFO)

    # Endpoint pour simuler une erreur (utile pour tests de robustesse / retries)
    @app.get("/api/error")
    def boom():
        return jsonify(error="simulated"), 500

    return app

# Gunicorn cherchera "app:app"
app = create_app()

if __name__ == "__main__":
    # Pour exécution locale (python app/main.py)
    app.run(host="0.0.0.0", port=8080)
