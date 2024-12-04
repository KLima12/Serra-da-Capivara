import React from "react";

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  const getMediaPath = (path) => {
    return `${process.env.PUBLIC_URL || ""}/media/${path}`;
  };

  return (
    <div class="footer">
      <hr class="footerLine"></hr>
      <div class="footerSections">
        <section>
          <h2>Central de Atendimento</h2>

          <br></br>

          <h4>
            Telefone para vendas:
            <br></br>
            <h5>(89) 98119-0133</h5>
          </h4>

          <br></br>

          <h4>
            Fábrica e Escritório:
            <br></br>
            <h5>(89) 99433-2021</h5>
          </h4>

          <br></br>

          <h4>
            Loja São Raimundo Nonato – PI:
            <br></br>
            <h5>(89) 3582-1949</h5>
          </h4>

          <br></br>

          <h4>
            Email:
            <br></br>
            <h5>vendas@ceramicacapivara.com</h5>
          </h4>
        </section>

        <section class="sectionInstagram">
          <h2>Siga-nos no Instagram!</h2>
          <a
            href="https://www.instagram.com/ceramicaserradacapivarapi/"
            target="blank"
          >
            <img
              src={getMediaPath("icon/instagram.png")}
              alt="logo instagram"
              class="logoInstagram"
            ></img>
          </a>
        </section>
      </div>

      <button class="footerButton" onClick={scrollToTop}>
        Voltar ao topo
      </button>
    </div>
  );
};

export default Footer;
