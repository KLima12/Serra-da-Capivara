import React from "react";
import BarraPesquisa from "./pesquisa";

const Header = () => {
  return (
    <div class="header">
      <div>
        <h2>Início</h2>
        <h2>Nossos Produtos</h2>
        <h2>Albergue</h2>
        <h2>Nossa História</h2>
        <h2>Reportagens</h2>
        <h2>Contatos</h2>
        <BarraPesquisa />
      </div>
    </div>
  );
};

export default Header;
