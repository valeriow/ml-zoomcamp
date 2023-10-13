import json
with open("Pipfile.lock", 'r') as arquivo:
        dados = json.load(arquivo)
print(dados['default']['scikit-learn']['hashes'][0])