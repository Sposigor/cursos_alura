import React, { Component } from "react";

class FormularioCadastro extends Component {
  render() {
    return (
      <form>
        <input type="text" placeholder="Nome" />
        <input type="text" placeholder="Sobrenome" />
        <input type="email" placeholder="E-mail" />
        <input type="password" placeholder="Senha" />
        <button type="submit">Cadastrar</button>
      </form>
    );
  }
}
export default FormularioCadastro;