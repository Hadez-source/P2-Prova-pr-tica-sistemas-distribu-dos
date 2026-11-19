# P2-Prova-pr-tica-sistemas-distribu-dos
Erick da Silva rodrigues
18/11/16
professora Simone Tatiane do Canto

Código bruto sem Nenhuma alteração:

import threading
import time # servidores simulados

principal = {
    "online": True,
    "estoque": 10

}

replica = {
    "online": True,
    "estoque": 10
}

#Controle de concorrencia

MAXIMO_SIMULTANEO = 3

semaforo = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()

pedidos_confirmados = []

def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)

        with trava:
            if principal["estoque"] > 0:
                principal["estoque"] -= 1

                pedidos_confirmados.append(numero)


def sincronizar():
    replica["estoque"] = replica ["estoque"]

    def consultar_estoque():
        if principal["online"]:
            return (
                "PRINCIPAL",
                principal["estoque"]

            )

    if principal["online"]:
        return (
            "REPLICA"

        )

    return "INDISPONIVEL", None


print("=== CENTRAL DE PEDIDOS ===")

print(
    "Limite Simultaneo:",
    principal["estoque"]
)

trabalhadores = [
    threading.Thread(
        target=processar_pedido,
        args=(numero,)
    )
    for numero in [101, 102, 103]
]

for trabalhador in trabalhadores:
    trabalhador.start()

for trabalhador in trabalhadores:
    trabalhador.join()

print(
    "pedidos confirmados:",
    sorted(pedidos_confirmados)

)

print(
    "Pedidos confirmados:",
    sorted(pedidos_confirmados)

)

print(
    "Replica antes:",
    replica["estoque"]

)

sincronizar()

print(
    "Replica depois:",
    replica["estoque"]

)

#Simulacao de falha
principal["online"] = False

nome, estoque = consultar_estoque()

print(
    "consulta apos falha:",
    nome,
    estoque
)




Resposta do Sistema:

=== CENTRAL DE PEDIDOS ===
Limite Simultaneo: 10
pedidos confirmados: [101, 102, 103]
Pedidos confirmados: [101, 102, 103]
Replica antes: 10
Replica depois: 10
Traceback (most recent call last):
  File "c:\Users\aluno\Downloads\Simulado_distribuidos\central_pedidos.py", line 106, in <module>
    nome, estoque = consultar_estoque
                    ^^^^^^^^^^^^^^^^^

Dá um erro no consultar estoque
