# Classe Mãe
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Função para ligar o veículo
    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado.")

    # Função para desligar o veículo
    def desligar(self):
        print(f"{self.marca} {self.modelo} está desligado.")

    # Função para mover o veículo
    def mover(self):
        print(f"{self.marca} {self.modelo} está se movendo.")

# Primeira Classe Filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    # Função para abrir o porta-malas
    def abrir_porta_malas(self):
        print(f"O porta-malas do {self.marca} {self.modelo} está aberto.")

    # Função específica de carro para mover
    def mover(self):
        print(f"O carro {self.marca} {self.modelo} está dirigindo.")

# Segunda Classe Filha
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    # Função para dar um grau na moto
    def dar_um_grau(self):
        print(f"A moto {self.marca} {self.modelo} está empinando.")

    # Função específica de moto para mover
    def mover(self):
        print(f"A moto {self.marca} {self.modelo} está acelerando.")

# Exemplo de uso
if __name__ == "__main__":
    carro = Carro("Toyota", "Corolla", 2020, 4)
    moto = Moto("Honda", "CBR", 2021, "Esportiva")

    # Chamando métodos do objeto carro
    carro.ligar()
    carro.mover()
    carro.abrir_porta_malas()
    carro.desligar()

    # Chamando métodos do objeto moto
    moto.ligar()
    moto.mover()
    moto.dar_um_grau()
    moto.desligar()
