from flask import Flask, jsonify, request,render_template
from datetime import datetime 
import os
import requests
import json
app = Flask(__name__)                             

PRD_EXTERNAL_SRV = 'http://external-service.gcp-demo.samuraitaiga.io/echo'
DEV_EXTERNAL_SRV = 'http://localhost:8081/echo'

myapp_env = os.environ.get('MYAPP_ENV')
if myapp_env == 'prd':
    external_service = PRD_EXTERNAL_SRV
else:
    external_service = DEV_EXTERNAL_SRV

@app.route('/')                        
def index():
    msg = request.args.get('msg')
    notice_msg = 'send ?msg=xxx to get echo reply from external_service'

    if msg:
        r = requests.get(external_service + '?msg=' + msg)
        payload = json.loads(r.content)
        notice_msg = payload['msg']

    return render_template('index.html', notice_msg=notice_msg)
 
if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=8080, debug=True)