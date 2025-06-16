import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess

class CompileHandler(PatternMatchingEventHandler):
    def __init__(self):
        super().__init__(patterns=["*.in"])

    def on_modified(self, event):
        if "base.in" in event.src_path:
            subprocess.run(["make", "compile-base"])
        elif "development.in" in event.src_path:
            subprocess.run(["make", "compile-dev"])
        elif "production.in" in event.src_path:
            subprocess.run(["make", "compile-prod"])

if __name__ == "__main__":
    path = "requirements"
    event_handler = CompileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print("📡 Watching .in files for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
