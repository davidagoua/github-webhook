from flask import Flask, request, abort
import os
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.get_json()

        # Vérifier si l'événement est un push sur la branche master
        if 'ref' in payload and payload['ref'] == 'refs/heads/master':

            # Chemin vers le dossier où vous voulez effectuer le 'git pull'
            repo_path = '/repo'

            # Exécuter 'git pull'
            git_process = Popen(['git', 'pull'], cwd=repo_path, stdout=PIPE, stderr=PIPE)
            stdout, stderr = git_process.communicate()

            # Vérifier si 'git pull' a été effectué avec succès
            if git_process.returncode == 0:
                return 'Git pull réussi', 200
            else:
                return f'Erreur lors du git pull:\n{stdout.decode("utf-8")}\n{stderr.decode("utf-8")}', 500
        else:
            return 'Événement non traité', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
