import subprocess
import os
import sys
from pathlib import Path

def executeCppCode(data):
    code = open(str(Path.cwd())+"/code.cpp","w+")
    code.write(data['code'])
    code.close()


    dataX, temp = os.pipe()
  
    # write to STDIN as a byte object(convert string
    # to bytes with encoding utf8)
    os.write(temp, bytes(data['questionInput'], "utf-8"));
    os.close(temp)
  
    # store output of the program as a byte string in s
    try:
        s = subprocess.check_output("g++ "+str(Path.cwd())+"/code.cpp"+" -o out",stderr=subprocess.PIPE, shell = True)
        try:
            t = subprocess.check_output(str(Path.cwd())+"./out",stderr=subprocess.PIPE, stdin = dataX,shell = True)
            return {'stdout':t.decode("utf-8"),'stderr':''}
        except subprocess.CalledProcessError as err:
            print('exit code: {}'.format(err.returncode))
            print('stdout: {}'.format(err.output.decode(sys.getfilesystemencoding())))
            error = err.stderr.decode('utf-8')
            print('stderr: {}'.format(err.stderr.decode(sys.getfilesystemencoding())))
            return {'stdout':"","stderr":error}

    except subprocess.CalledProcessError as e:
        #print('exit code: {}'.format(e.returncode))
        #print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
        error = e.stderr.decode('utf-8')
        #print('stderr: {}'.format(e.stderr.decode(sys.getfilesystemencoding())))
        return {'stdout':"","stderr":error}
  
    # decode s to a normal string
    
    return {'stdout':'',"stderr":""}