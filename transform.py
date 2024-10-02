import os
from PIL import Image

# Caminho da pasta com as imagens
caminho_pasta = 'caminho/para/sua/pasta'

# Verificar se o diretório existe
if not os.path.exists(caminho_pasta):
    print(f'O caminho {caminho_pasta} não existe.')
else:
    # Criar pasta de saída para as imagens convertidas
    caminho_saida = os.path.join(caminho_pasta, 'imagens_bmp')
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    # Percorrer todos os arquivos da pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

        # Tentar abrir a imagem
        try:
            with Image.open(caminho_completo) as img:
                # Converter para .bmp
                nome_base = os.path.splitext(nome_arquivo)[0]
                caminho_bmp = os.path.join(caminho_saida, f'{nome_base}.bmp')
                img.save(caminho_bmp)
                print(f'{nome_arquivo} convertido para {caminho_bmp}')
        except Exception as e:
            print(f'Erro ao processar {nome_arquivo}: {e}')
