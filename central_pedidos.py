import threading
import time # servidores simulados

principal = {
    "online": True,
    "estoque": 10,
    
}

replica = {
    "online": True,
    "estoque": 10
}

#Controle de concorrencia

MAXIMO_SIMULTANEO = 2

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
    replica["estoque"] = principal["estoque"]

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
    MAXIMO_SIMULTANEO
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


nome, estoque = consultar_estoque

print(
    "consulta apos falha:",
    nome,
    estoque
)
