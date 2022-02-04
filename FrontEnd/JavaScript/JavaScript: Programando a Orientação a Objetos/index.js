import {Cliente} from "./Cliente.js"
import {ContaCorrente} from "./ContaCorrente.js"

const cliente1 = new Cliente("Igor", 11122233309);


const contaCorrenteIgor = new ContaCorrente(1001, cliente1);
contaCorrenteIgor.depositar(500);
contaCorrenteIgor.sacar(100);


console.log(contaCorrenteIgor);