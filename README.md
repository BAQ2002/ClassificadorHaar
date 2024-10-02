# ClassificadorHaar para identificação de laranjas.

Este repositório contém o processo de treinamento do classificado Haar para idenficação de laranjas.
O dataset está disponivel em: https://images.cv/dataset/orange-image-classification-dataset
O tutorial com código seguido para o treinamamento classificador está disponivel: https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf.
Nenhuma etapa de préprocessamento foi aplicada no dataset, a não ser a mudança de suas extenções de .jpeg para .bmp com a ajuda de ./transform.py. Foram selecioadnadas apenas 189 imagens aleatórias do dataset de laranjas de treino.
O resultado foi aplicado em algumas imagens de teste, disponiveis em: https://colab.research.google.com/drive/1jQR7ckUVhfSNtevU7U_g6uuSjwQ1aGx_?usp=sharing.

## Resultados:
O classificador não conseguiu identificar nenhuma das laranjas na pequena amostra de teste, mesmo variando os hiperparematros de vizinhos, fator de escala e tamanho da slinding windown. Mesmo de repetido o processo de treinamento e de anotação de imagens 4 vezes, o resultado continuou o mesmo, descartando a possibilidade de ser algum erro de execução ou má qualidade de anotação das imagens.

## Hipósteses:
Os resultados ruins podem ter sido obtidos pela quantidade pequena de imagens no treinamento.
O algoritmo pode não identificar laranjas muito bem.
O Haar Cascade depende de características simples (retângulos claros e escuros) para detectar objetos. Objetos com formas mais complexas ou variações nas texturas, como laranjas (superfície rugosa e detalhes sutis), podem não ser bem representados por essas características.
Ruído no Background das imagens selecionadas.


