console.log("Trabalhando com listas");

// const salvador = `Salvador`;
// const saoPaulo = `São Paulo`;
// const rioDeJaneiro = `Rio de Janeiro`;

// Criando uma lista para armazenar as cidades
const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);


// Adicionando um novo elemento na lista
listaDeDestinos.push(`Curitiba`);
listaDeDestinos.push(`Recife`);
listaDeDestinos.push(`Belo Horizonte`);

// Lembrando que numa lista o indice começa em 0
listaDeDestinos.splice(1, 1); // Remove o elemento na posição 1 e 1 elemento

// Imprimindo a lista de destinos
console.log(listaDeDestinos);
console.log(listaDeDestinos[1]);