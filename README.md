# ClassificadorHaar para identificação de laranjas.

Este repositório contém o processo de treinamento do classificado Haar para idenficação de laranjas.

O dataset está disponivel em: https://images.cv/dataset/orange-image-classification-dataset

O tutorial com código seguido para o treinamamento classificador está disponivel: https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf.

Nenhuma etapa de préprocessamento foi aplicada no dataset, a não ser a mudança de suas extenções de .jpeg para .bmp com a ajuda de ./transform.py. Foram selecionadas apenas 189 imagens aleatórias do dataset de laranjas de treino.

O resultado foi aplicado em algumas imagens de teste, disponiveis em: https://colab.research.google.com/drive/1jQR7ckUVhfSNtevU7U_g6uuSjwQ1aGx_?usp=sharing.

## Resultados:
O classificador não conseguiu identificar nenhuma das laranjas na pequena amostra de teste, mesmo variando os hiperparematros de vizinhos, fator de escala e tamanho da slinding windown. Mesmo de repetido o processo de treinamento e de anotação de imagens 4 vezes, o resultado continuou o mesmo, descartando a possibilidade de ser algum erro de execução ou má qualidade de anotação das imagens.

## Hipósteses:
Os resultados ruins podem ter sido obtidos pela quantidade pequena de imagens no treinamento.

O algoritmo pode não identificar laranjas muito bem. O Haar Cascade depende de características simples (retângulos claros e escuros) para detectar objetos. Objetos com formas mais complexas ou variações nas texturas, como laranjas (superfície rugosa e detalhes sutis), podem não ser bem representados por essas características.

Ruído no Background das imagens selecionadas.

## Constatações:
A fruta laranja pode ser um objeto desafiador para o treinamento de um classificador Haar, especialmente por alguns motivos relacionados à sua forma e textura visual:

### Pontos Positivos:

#### Formato simples e regular: 
A laranja tem um formato aproximadamente esférico, o que pode facilitar a detecção se o classificador estiver focado apenas em formas geométricas básicas.

#### Contraste de cor: 
Se for usada em um contexto onde o fundo é claro ou muito diferente da cor da laranja (exemplo, fundo branco ou azul), o contraste pode ajudar na detecção.

### Pontos Negativos:

#### Poucas bordas claras: 
Classificadores Haar são melhores em detectar objetos com bordas nítidas e contrastes marcantes. Como a laranja tem uma textura suave e relativamente uniforme, não possui muitas bordas de alto contraste que possam ser capturadas de forma eficaz por um classificador Haar.

#### Dependência de iluminação: 
A cor e a textura da laranja podem mudar significativamente dependendo da iluminação. Sombras ou reflexos na casca podem afetar a detecção, criando variações difíceis de lidar para o classificador.

#### Textura suave: 
A superfície da laranja não apresenta características internas marcantes (como olhos ou nariz em um rosto), o que torna a diferenciação de outras frutas ou objetos arredondados mais difícil.

### Conclusão:
Uma laranja não é o melhor objeto para treinar um classificador Haar, porque ela não tem bordas nítidas ou contrastes que o classificador pode explorar com facilidade. No entanto, se você estiver interessado em detectar formas esféricas em um fundo de cor contrastante, a laranja pode ser um caso interessante, mas um classificador Haar pode não ser a ferramenta mais adequada para isso.

Se o foco for detectar frutas como a laranja, modelos baseados em aprendizado profundo (como redes neurais convolucionais) costumam ser mais eficazes, pois conseguem capturar características mais sutis e complexas de textura e cor.


