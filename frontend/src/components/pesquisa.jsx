import React from "react";

const BarraPesquisa = () => {
  const getMediaPath = (path) => {
    return `${process.env.PUBLIC_URL || ""}/media/${path}`;
  };

  return (
    <div className="horizontal searchBar">
      <img
        src={getMediaPath("icon/search.svg")}
        alt="icone pesquisa"
        class="searchIcon"
      ></img>

      <form class="searchContainer">
        <input
          type="text"
          placeholder="Pesquisar"
          className="searchText s12"
        ></input>
      </form>
    </div>
  );
};

export default BarraPesquisa;
