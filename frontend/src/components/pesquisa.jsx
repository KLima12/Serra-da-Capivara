import React, { useState } from "react";

const BarraPesquisa = () => {
  const [searchTerm, setSearchTerm] = useState("");

  const getMediaPath = (path) => {
    return `${process.env.PUBLIC_URL || ""}/media/${path}`;
  };

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleFormSubmit = (e) => {
    if (!searchTerm.trim()) {
      e.preventDefault();
      return;
    }
  };

  return (
    <div className="horizontal searchBar">
      <img
        src={getMediaPath("icon/search.svg")}
        alt="icone pesquisa"
        className="searchIcon"
      ></img>

      <form
        className="searchContainer"
        action={`/pesquisa/${encodeURIComponent(searchTerm)}`}
        method="GET"
        onSubmit={handleFormSubmit}
      >
        <input
          type="text"
          placeholder="Pesquisar"
          className="searchText s12"
          value={searchTerm}
          onChange={handleInputChange}
        ></input>
      </form>
    </div>
  );
};

export default BarraPesquisa;
