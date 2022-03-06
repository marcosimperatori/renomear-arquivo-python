import os
import shutil

pasta = r'C:\\Users\\marco\\Pictures\\'
posicaoInicial = 10

# Esta função tem a responsabilidade de extrair parte do nome do arquivo, considerando para isso a partir da posição
# informada na constatne posicaoInicial e até o final do nome do arquivo informado
def renomearArquivo(file):
    return file[posicaoInicial:]

# Para cada arquivo recebido esta função se encarrega de renomeá-lo
def tratarArquivo(file):
    novoArquivo = renomearArquivo(file)
    nomeAntigo  = os.path.join(pasta,file)
    novoNome    = os.path.join(pasta,novoArquivo)

    print(f'Renomeando "{file}" para "{novoArquivo}"')
    shutil.move(nomeAntigo,novoNome)

# Esta função tem a responsabilidade de varrer o diretório apontado na constante pasta, então
# para cada arquivo que encontrar ele chamará a função responsável por tratar o nome do arquivo '''
def loop_principal():
    for nomeArquivo in os.listdir(pasta):
        tratarArquivo(nomeArquivo)

if __name__ == '__main__':
    loop_principal()