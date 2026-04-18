class ContaBancaria:
    def __init__(self, numero_conta, nome_pessoa, balanco_inicial):
        self.numero_conta = numero_conta
        self.nome_pessoa = nome_pessoa

        if balanco_inicial >= 0:
            self.__balanco = balanco_inicial
        else:
            self.__balanco = 0
            print("Saldo inicial inválido. Definido como saldo ZERO.")

    @property
    def balanco(self):
        return self.__balanco

    @balanco.setter
    def balanco(self, valor):
        self.__balanco = valor

    def deposito(self, qtd):
        if not isinstance(qtd, (int, float)):
            return "Erro: valor do depósito deve ser numérico."

        if qtd <= 0:
            return "Erro: valor do depósito deve ser positivo."

        self.__balanco += qtd
        return f"Depósito de R$ {qtd:.2f} realizado com sucesso."

    def saque(self, qtd):
        if not isinstance(qtd, (int, float)):
            return "Erro: valor do saque deve ser numérico."

        if qtd <= 0:
            return "Erro: valor do saque deve ser positivo."

        if qtd > self.__balanco:
            return "Erro: saldo insuficiente."

        self.__balanco -= qtd
        return f"Saque de R$ {qtd:.2f} realizado com sucesso."


# Classe filha Conta Corrente
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, nome_pessoa, balanco_inicial, limite):
        super().__init__(numero_conta, nome_pessoa, balanco_inicial)
        self.limite = limite

    def saque(self, qtd):
        if not isinstance(qtd, (int, float)):
            return "Erro"

        if qtd <= 0:
            return "Erro"

        if qtd <= self.balanco:
            self.balanco -= qtd
            return f"Saque de R$ {qtd:.2f} realizado"
    
        elif qtd <= self.balanco + self.limite:
            restante = qtd - self.balanco
            self.balanco = 0
            self.limite -= restante
            return f"Saque usando limite de R$ {restante:.2f}"
    
        else:
            return "Erro: saldo insuficiente"


# Classe filha Conta Poupança
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, nome_pessoa, balanco_inicial, taxa_juros):
        super().__init__(numero_conta, nome_pessoa, balanco_inicial)
        self.taxa_juros = taxa_juros

    def aplicar_rendimento(self):
        rendimento = self.balanco * self.taxa_juros
        self.deposito(rendimento)
        return f"Rendimento de R$ {rendimento:.2f} aplicado à poupança."


# Classe filha Conta Investimento
class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta, nome_pessoa, balanco_inicial, risco):
        super().__init__(numero_conta, nome_pessoa, balanco_inicial)
        self.risco = risco

    def exibir_info(self):
        return (
            f"Investimento ({self.risco}) - "
            f"Titular: {self.nome_pessoa} | "
            f"Saldo: R$ {self.balanco:.2f}"
        )


# Testes
if __name__ == "__main__":
    print("--- Teste Conta Corrente ---")
    cc = ContaCorrente(101, "Gabriel Franco", 500, 200)
    print(cc.saque(600))
    print(f"Saldo final CC: R$ {cc.balanco:.2f}")

    print("\n--- Teste Conta Poupança ---")
    cp = ContaPoupanca(202, "Maria Silva", 1000, 0.10)
    print(cp.aplicar_rendimento())
    print(f"Saldo final CP: R$ {cp.balanco:.2f}")

    print("\n--- Teste Conta Investimento ---")
    ci = ContaInvestimento(303, "Ana Souza", 5000, "Alto Risco")
    print(ci.exibir_info())