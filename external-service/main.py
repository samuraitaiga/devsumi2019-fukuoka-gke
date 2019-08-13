from flask import Flask, jsonify, request
from datetime import datetime                           
app = Flask(__name__)                             

@app.route('/echo')
def echo():
    msg = request.args.get('msg')
    if not msg:
        msg = ''
    echo_msg = '[' + msg + '] ' + 'echo reply from external service'
    response = {'msg': echo_msg, 'timestamp': datetime.now().isoformat()}
    return jsonify(response)                         

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=8080, debug=True)