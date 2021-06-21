import re
from subprocess import run,PIPE,STDOUT

def executeCppCode(data):

    code = open(data['slug']+".cpp","w+")
    code.write(data['code'])
    code.close()


    programInput = data['customInput'].encode()
    output,verdict="","RE"
    
    expectedOutput = re.sub('\n', '',data['expectedOutput'])
    compilation = run(["g++", "-Wall","-w", "-o", data["slug"], data["slug"]+".cpp"], stdout=PIPE, stderr=STDOUT)
    if(compilation.returncode == 0):
        try:
            execution = run(["./"+data["slug"]],input=programInput, stdout=PIPE, stderr=STDOUT,timeout=5)
            output = execution.stdout.decode("utf-8")
            if(output.rstrip() == expectedOutput.rstrip()):
                verdict = "AC"
            else:
                verdict = "WA"
        except Exception:
            
            output,verdict = "Your program didn't execute in given time limit! Try to optimize your code","TLE"
        afterExecution = run(["rm",data['slug']])
    else:
        output = compilation.stdout.decode('utf-8')

    afterExecution = run(["rm",data['slug']+".cpp"])

    return output,verdict