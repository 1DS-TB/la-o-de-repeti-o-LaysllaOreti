import random #importa a biblioteca de 'aleatório'

def menu():
    while True:
        print("\n*** Duelo de Heróis ***")
        
        print("(1) Iniciar jogo")
        print("(2) Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def iniciar_jogo():
    # Sorteio de atributos
    hp_inicial = random.randint(200, 1000)
    jogador = {
        "hp": hp_inicial,
        "atq": random.randint(1, 50),
        "def": random.randint(1, 50)
    }

    inimigo = {
        "hp": hp_inicial,
        "atq": random.randint(1, 50),
        "def": random.randint(1, 50)
    }

    turno = 1
    while jogador["hp"] > 0 and inimigo["hp"] > 0:
        print(f"\n=== Você ===\nHP: {jogador['hp']}  ATQ: {jogador['atq']}  DEF: {jogador['def']}")
        print(f"=== Inimigo ===\nHP: {inimigo['hp']}  ATQ: {inimigo['atq']}  DEF: {inimigo['def']}")
        print(f"\n--- Turno {turno} ---")
        print(f"Seu HP: {jogador['hp']} | Inimigo HP: {inimigo['hp']}")
        acao = input("Sua vez: (1) Atacar ou (2) Curar? ")

        # Jogador joga
        if acao == "1":
            dano = max(0, jogador["atq"] - inimigo["def"])
            inimigo["hp"] -= dano
            print(f"Você ataca! Inimigo perde {dano} HP.")
        elif acao == "2":
            cura = random.randint(10, 30)
            jogador["hp"] += cura
            print(f"Você se cura em {cura} HP!")
        else:
            print("Ação inválida. Você perdeu a vez.")

        # Verifica se o inimigo perdeu
        if inimigo["hp"] <= 0:
            print("\nVocê venceu! Inimigo derrotado com sucesso.")
            return

        # Inimigo joga
        acao_inimigo = random.choice(["atacar", "curar"])
        if acao_inimigo == "atacar":
            dano = max(0, inimigo["atq"] - jogador["def"])
            jogador["hp"] -= dano
            print(f"Inimigo ataca! Você perde {dano} HP.")
        else:
            cura = random.randint(10, 30)
            inimigo["hp"] += cura
            print(f"Inimigo se cura em {cura} HP!")

        # Verifica se o jogador perdeu
        if jogador["hp"] <= 0:
            print("\nVocê foi derrotado! Infelizmente, o inimigo venceu.")
            return

        turno += 1

# Inicia o menu principal
menu()
