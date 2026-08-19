from flask import Flask
app = Flask(__name__)

#Retorna o Status da aplicação
@app.route('/status')
def status():
    return{'servico': 'OpsTrackAPI', 'status': 'online'}

@app.route('/sobre')
def sobre():
    return{'version':'OpsTrack API - Version: 1.0.0'}

@app.route('/tickets')
def tickets():
    return{'chamado':'Ana: 10:07:45 - Mouse sem funcionar',
           'chamado2':'Cassio: 11:37:86 - Impressora travada',
           'chamado3':'Roberto: 12:26:32 - Sem sinal de internet'}
if __name__ == '__main__':
    app.run(debug=True)