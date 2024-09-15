import os
import time
from git import Repo
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configura estos valores
REPO_PATH = '/ruta/a/tu/repositorio'
COMMIT_MESSAGE = 'Auto-commit: Actualización de código'
GITHUB_REMOTE = 'origin'
BRANCH_NAME = 'main'

repo = Repo(REPO_PATH)

class GitAutoCommit(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.py'):
            print(f"Archivo modificado: {event.src_path}")
            self.stage_commit_and_push()

    def stage_commit_and_push(self):
        try:
            # Stage all changes
            repo.git.add(A=True)
            
            # Commit
            repo.index.commit(COMMIT_MESSAGE)
            
            # Push
            origin = repo.remote(name=GITHUB_REMOTE)
            origin.push(BRANCH_NAME)
            
            print("Cambios subidos a GitHub exitosamente.")
        except Exception as e:
            print(f"Error al subir cambios: {str(e)}")

if __name__ == "__main__":
    event_handler = GitAutoCommit()
    observer = Observer()
    observer.schedule(event_handler, path=REPO_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
