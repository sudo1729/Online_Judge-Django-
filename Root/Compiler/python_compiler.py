import subprocess
import os
import sys
def executePythonCode(data):
    try:
        res = subprocess.run([sys.executable, "-c", data['code']],input=data['customInput'], capture_output=True, text=True,timeout=5)
        print(data['expectedOutput'])
        if(res.stderr):
            verdict = "RE"
        elif(str(res.stdout) == str(data['expectedOutput'])):
            verdict = "AC"
        else:
            verdict = "WA"
        if(res.stderr):
            result = res.stderr
        else:
            result = res.stdout
        return result,verdict
    except Exception:
        return "Your Program did not execute in given time limit!","TLE"
