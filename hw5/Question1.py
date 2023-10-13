import subprocess 
comando = "pipenv --version"
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


if resultado.returncode == 0:
    # A saída do comando está em resultado.stdout
    print("Saída do comando:")
    print(resultado.stdout)
else:
    # O comando falhou, a mensagem de erro está em resultado.stderr
    print("Erro ao executar o comando:")
    print(resultado.stderr)