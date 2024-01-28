from flask import Flask, request
app = Flask(__name__)
import socket, subprocess

seed_value=0

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def route():
    global seed_value
    ret = 'SUCCESS'
    if request.method == 'POST':

       content = request.json
       if 'num' in content:
           seed_value = content['num']

       command = 'python3 stress_cpu.py ' + str(seed_value)

       try : 
          result = subprocess.Popen(['/home/ubuntu/MP2/stress_cpu.py', str(seed_value)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)        
       except Exception as e:
          print("An exception occurred:", str(e))
          return str(e)

       return ret 


    if request.method == 'GET':
           return socket.gethostname()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
