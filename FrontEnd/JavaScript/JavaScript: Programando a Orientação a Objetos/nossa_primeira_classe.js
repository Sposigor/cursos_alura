class Cliente {
    nome;
    cpf;
}

class ContaConrrente {
    agencia;
    #saldo;

    sacar(valor) {
        if (this.#saldo >= valor) {
            this.#saldo -= valor;
        }
    }

    depositar(valor) {
        if (valor > 0) {
            this.#saldo += valor;
        }
    }
}

const cliente1 = new Cliente();

cliente1.nome = "Igor";
cliente1.cpf = 50589002453;

const conta1 = new ContaConrrente();
conta1.agencia = 6699;
conta1.saldo = 150;
conta1.sacar(100);
console.log(conta1);

conta1.depositar(500);


console.log(cliente1);
console.log(conta1);