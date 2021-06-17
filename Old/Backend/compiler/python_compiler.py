import subprocess
import os
import sys
def executePythonCode(data):
    res = subprocess.run([sys.executable, "-c", data['code']],input=data['questionInput'], capture_output=True, text=True)
    result = {"stdout":res.stdout,"stderr":res.stderr}
    return result