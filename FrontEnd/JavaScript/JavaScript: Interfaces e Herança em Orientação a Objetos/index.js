import {Cliente} from "./Cliente.js";
import {Gerente} from "./Funcionario/Gerente.js"
import {Diretor} from "./Funcionario/Diretor.js"
import {SistemaAutenticacao} from "./SistemaAutenticacao.js"

const diretor =  new Diretor("Igor", 10000, 12345678900);
diretor.cadastrarSenha("123456")
const gerente =  new Gerente("Enzo",  5000, 12378945601);
gerente.cadastrarSenha("123");

const cliente = new Cliente("Esposito", 78945612379, "456");
const gerenteEstaLogado = SistemaAutenticacao.login(gerente, "123");
const diretorEstaLogado = SistemaAutenticacao.login(diretor, "123456");


const clienteEstaLogado = SistemaAutenticacao.login(cliente, "456");

console.log(gerenteEstaLogado, diretorEstaLogado, clienteEstaLogado);