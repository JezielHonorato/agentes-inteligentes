# inspiração: https://www.kaggle.com/code/ngongochai/markov-chain-sherlock-holmes

# Precisa instalar o NLTK e baixar os recursos necessários (tokenizador e stopwords) para executar este código.
# import nltk
# nltk.download()


import os
import re
import random
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

# Define o caminho para os arquivos de texto
assets = "./assets/"


def read_text(assets, sentences=False):
    """Lê os arquivos de texto do diretório fornecido."""
    txt = []
    if not os.path.exists(assets):
        print(f"Aviso: O diretório '{assets}' não foi encontrado.")
        return txt

    # os.walk() retornar 3 valores, como não vou usá-los, por convenção, uso _ para indicar que não serão usados.
    # for root, dirs, files in os.walk(assets):
    for _, _, files in os.walk(assets):
        for file in files:
            with open(os.path.join(assets, file), "r", encoding="utf-8") as f:
                if sentences:
                    linhas_validas = []

                for line in f:
                    line = line.strip()

                    # Ignora linhas que começam com "#" (usei textos em .md e quero retirar titulos) ou vazias.
                    if line.startswith("#") or line == "":
                        continue

                    if sentences:
                        linhas_validas.append(line)
                    else:
                        txt.append(line)

                if sentences:
                    texto_completo = " ".join(linhas_validas)

                    # Quebra todo o bloco de texto em sentenças. Usei o nitk para isso pois ele sabe separar fim de frase de abreviações.
                    sentencas = sent_tokenize(texto_completo, language="portuguese")
                    txt.extend(sentencas)
    return txt


def clean_txt(txt):
    """Tokeniza o texto, remove pontuações e palavras que não são apenas letras."""
    cleaned_txt = []

    for line in txt:
        line = line.lower()

        # Remove pontuações
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)

        # Tokeniza avisando informando o idioma, inglês é default.
        tokens = word_tokenize(line, language="portuguese")

        for word in tokens:
            # Se for ma palavra, ou seja apenas letras e tamanho maior ou igual a 1
            if word.isalpha():
                cleaned_txt.append(word)

    return cleaned_txt


def make_markov_model(cleaned_txt, n_gram=2):
    """Cria o dicionário de probabilidades da Cadeia de Markov."""

    # dict = {token_atual: {next_token: count, next_token2: count2, ...}, token_atual2: {...}, ...}
    markov_model = defaultdict(lambda: defaultdict(int))

    # Estado atual (n palavras) + próximo estado (n palavras) = 2n palavras, então o limite seguro para o loop é len(cleaned_txt) - 2n + 1
    limite_range = len(cleaned_txt) - (n_gram * 2) + 1

    for part in cleaned_txt:
        limite_range = len(part) - (n_gram * 2) + 1

        # Ignora sentenças que são menores que o estado atual + próximo estado
        if limite_range < 1:
            continue

        # usa slicing para separar o estado atual e o próximo estado.
        for i in range(limite_range):
            token_atual = " ".join(part[i : i + n_gram])
            next_token = " ".join(part[i + n_gram : i + (n_gram * 2)])
            markov_model[token_atual][next_token] += 1

    # Novo dicionário para armazenar as probabilidades.
    prob_model = defaultdict(lambda: defaultdict(float))

    for token_atual, transitions in markov_model.items():
        total = sum(transitions.values())
        for next_token, count in transitions.items():
            probability = count / total
            prob_model[token_atual][next_token] = probability

    return prob_model


def generate_story(markov_model, limite=100, inicio="quando o"):
    """Gera texto novo com base nas probabilidades do modelo."""
    n = 0
    token_atual = inicio.lower()
    story = token_atual + " "

    # Se a palavra inicial não estiver no modelo, avisa e para.
    if token_atual not in markov_model:
        return f"Erro: O estado inicial '{inicio}' não existe no modelo treinado."

    while n < limite:
        # Sorteia o próximo estado baseado nas probabilidades indexadas.
        next_token_list = random.choices(
            list(markov_model[token_atual].keys()),
            weights=list(markov_model[token_atual].values()),
        )

        token_atual = next_token_list[0]
        story += token_atual + " "
        n += 1

    return story.strip()


text = read_text(assets, sentences=True)
print("numero de linhas = ", len(text))

cleaned_text = clean_txt(text)
print("numero de palavras = ", len(cleaned_text))

markov_model = make_markov_model(cleaned_text, n_gram=2)
print("numero de estados = ", len(markov_model.keys()))

print("\nGerando 20 histórias:\n" + "-" * 20)
for i in range(20):
    print(str(i + 1) + ". ", generate_story(markov_model, inicio="quando o", limite=8))
