import React from "react";
import BarraPesquisa from "./pesquisa";

const Header = () => {
  const getMediaPath = (path) => {
    return `${process.env.PUBLIC_URL || ""}/media/${path}`;
  };

  const currentPath = window.location.pathname;

  const isActive = (path) => {
    if (path === "/categorias/" && currentPath.startsWith("/produtos")) {
      return true;
    }
    if (path === "/categorias/" && currentPath.startsWith("/produto")) {
      return true;
    }
    return currentPath === path;
  };

  return (
    <div className="header">
      <div className="headerHorizontal">
        <img
          src={getMediaPath("icon/logo-pequena.png")}
          alt="logo capivara"
          className="logoCapivaraPequena"
        />

        <a href="/home/" className={`${isActive("/home/") ? "active" : ""}`}>
          <h2
            className={`textoHeader s20 ${isActive("/home/") ? "active" : ""}`}
          >
            Início
          </h2>
        </a>

        <a href="/categorias/">
          <h2
            className={`textoHeader s20 ${
              isActive("/categorias/") ? "active" : ""
            }`}
          >
            Nossos Produtos
          </h2>
        </a>

        <a
          href="https://www.pousadadaceramicaserradacapivara.com/"
          target="blank"
        >
          <h2 className="textoHeader s20">Albergue</h2>
        </a>

        <a
          href="/historia/"
          className={`${isActive("/historia/") ? "active" : ""}`}
        >
          <h2
            className={`textoHeader s20 ${
              isActive("/historia/") ? "active" : ""
            }`}
          >
            Nossa História
          </h2>
        </a>

        <a
          href="/reportagens/"
          className={`${isActive("/reportagens/") ? "active" : ""}`}
        >
          <h2
            className={`textoHeader s20 ${
              isActive("/reportagens/") ? "active" : ""
            }`}
          >
            Reportagens
          </h2>
        </a>

        <a
          href="/contatos/"
          className={`${isActive("/contatos/") ? "active" : ""}`}
        >
          <h2
            className={`textoHeader s20 ${
              isActive("/contatos/") ? "active" : ""
            }`}
          >
            Contatos
          </h2>
        </a>

        <BarraPesquisa />

        <a
          href="/carrinho/"
          className={`${isActive("/carrinho/") ? "active" : ""}`}
        >
          <img
            src={getMediaPath("icon/cart.svg")}
            alt="cart"
            className={`cartIcon ${isActive("/carrinho/") ? "active" : ""}`}
          />
        </a>
      </div>
    </div>
  );
};

export default Header;
