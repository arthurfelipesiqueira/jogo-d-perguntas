print ("bom diaaaaaaaaaaaaaa....")

#descrição
print (" jogo das palavras ")

#perguntas
nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")
print("Meu nome é", nome, "e minha idade é", idade, "anos")

# --- Primeira Parte do Jogo ---
resposta_letras = input("Quantas letras tem o seu nome? ")

letras_nome_correto = len(nome)

if int(resposta_letras) == letras_nome_correto:
    print("Parabéns, você acertou a quantidade de letras do seu nome!")
else:
    print(f"Ops, você errou. Seu nome tem {letras_nome_correto} letras.")

# --- Segunda Parte do Jogo ---
print("Agora, vamos para a próxima pergunta:")
resposta_soma = input("Você sabe quanto é a sua idade mais a quantidade de letras do seu nome? Digite o valor: ")

# 1. Calcular a resposta correta para a soma
soma_total_correta = int(idade) + letras_nome_correto

# 2. Verificar se o usuário acertou a soma
if int(resposta_soma) == soma_total_correta:
    print("Incrível! Você acertou a soma também!")
else:
    print(f"Você errou novamente. A resposta correta era {soma_total_correta}.")

# --- Nova Funcionalidade ---
# Verificar se a soma total é menor ou maior que 15
if soma_total_correta < 15:
    print(f"O número de letras no seu nome junto a sua idade é bem pequeno.")
elif soma_total_correta > 15:
    print(f"Os números das letras do seu nome mais a sua idade é bem alto.")

print("Acabo")
