from flask import Flask
app = Flask(__name__)

#Retorna o Status da aplicação
@app.route('/status')
def status():
    return{'servico': 'OpsTrackAPI', 'status': 'online'}

@app.route('/sobre')
def sobre():
    return{'OpsTrack API - Version: 1.0.0'}

@app.route('/tickets')
def tickets():
    return{'Ana: 10:07:45 - Mouse sem funcionar\n'
           'Cassio: 11:37:86 - Impressora travada\n'
           'Roberto: 12:26:32 - Sem sinal de internet'}
if __name__ == '__main__':
    app.run(debug=True)