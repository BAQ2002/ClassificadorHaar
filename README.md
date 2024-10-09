# ClassificadorHaar para identificação de laranjas.

Este repositório contém o processo de treinamento do classificado Haar para idenficação de laranjas.

O dataset está disponivel em: https://images.cv/dataset/orange-image-classification-dataset : mais imagens foram coletadas por outras fontes como bing images

O tutorial com código seguido para o treinamamento classificador está disponivel: https://github.com/felipecbarelli/livro-visao-computacional/blob/master/tutoriais/creating-a-cascade-of-haar-like-classifiers.pdf.

Nenhuma etapa de préprocessamento foi aplicada no dataset, a não ser a mudança de suas extenções de .jpeg para .bmp com a ajuda de ./transform.py. Foram selecionadas 274 imagens aleatórias de laranjas para o treino e 338 imagens negativas.

O resultado foi aplicado em algumas imagens de teste, disponiveis em: https://colab.research.google.com/drive/1jQR7ckUVhfSNtevU7U_g6uuSjwQ1aGx_?usp=sharing.

## Resultados Atualizados:
O classificador foi capaz de identificar as laranjas na pequena amostra de teste, variando os hiperparematros de vizinhos, fator de escala e tamanho da slinding windown. A partir dos resultandos anteriores onde o classificador não foi capaz de intentificar as laranjas, foram necessarias algumas medidas nas amostras de imagens positivas e principalmente das imagens negativas, como : adição de objetos com a forma esférica semelhante ao objeto alvo, cenários em que o objeto pode ser encotrado, como geladeiras, arvores e supermercados.

## Constatações:
A fruta laranja pé um objeto desafiador para o treinamento de um classificador Haar, especialmente por alguns motivos relacionados à sua forma e textura visual:

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


