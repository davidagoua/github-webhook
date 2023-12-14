from fastapi import FastAPI, HTTPException
from fastapi import Request
import subprocess
import os

app = FastAPI()

@app.post("/webhook")
async def github_webhook(request: Request):
    data = await request.json()

    # Vérifie que l'événement est un push et que la branche est master
    if request.headers.get('X-GitHub-Event') == 'push' and data['ref'] == 'refs/heads/master':
        # Remplacez 'your_repo_path' par le chemin absolu de votre référentiel local
        repo_path = '/repo'

        try:
            # Effectue un git pull dans le dossier du référentiel
            subprocess.run(["git", "pull","origin","master"], cwd=repo_path, check=True)
            return {"status": "success", "message": "Git pull réussi."}
        except subprocess.CalledProcessError as e:
            raise HTTPException(status_code=500, detail=f"Erreur lors de git pull: {e}")
    else:
        return {"status": "ignored", "message": "Événement ignoré."}
