import React, { useState, useEffect, useRef } from "react";

const getMediaPath = (path) => {
  return `${process.env.PUBLIC_URL || ""}/media/${path}`;
};

const images = [
  {
    src: getMediaPath("banners/banner-1.webp"),
    title: "Parque Nacional Serra da Capivara",
    description:
      'Os melhores períodos para visitar o Parque Nacional da Serra da Capivara são fevereiro e março, julho e agosto, e dezembro e janeiro. "Estas épocas são ótimas para passeios e trilhas. Recebemos turistas de diversos lugares e, para aqueles que se hospedam no nosso albergue, facilitamos o contato com guias turísticos, que também são das proximidades do parque", explica Girleide Oliveira. \n\nOs visitantes do parque podem explorar, além da riqueza cultural e histórica, trilhas preparadas para diferentes níveis de dificuldade, oferecendo uma variedade de atividades que atendem às expectativas e possibilidades de cada pessoa.',
  },
  {
    src: getMediaPath("banners/banner-2.webp"),
    title: "Albergue Serra da Capivara",
    description: "Albergue bem bonito",
  },
  {
    src: getMediaPath("banners/banner-3.webp"),
    title: "Restaurante Serra da Capivara",
    description: "Restaurante cheio de coisas gostosas",
  },
];

const Carrossel = () => {
  const [index, setIndex] = useState(0);
  const timerRef = useRef(null);

  const moveSlide = (direction) => {
    setIndex((prevIndex) => {
      let newIndex = prevIndex + direction;
      if (newIndex < 0) return images.length - 1;
      if (newIndex >= images.length) return 0;
      return newIndex;
    });

    restartInterval();
  };

  const restartInterval = () => {
    if (timerRef.current) clearInterval(timerRef.current);
    timerRef.current = setInterval(() => moveSlide(1), 5000);
  };

  useEffect(() => {
    restartInterval();
    return () => clearInterval(timerRef.current);
  }, []);

  return (
    <div className="carousel">
      {images.map((image, i) => (
        <div key={i} className={`carouselSlide ${i === index ? "active" : ""}`}>
          <img
            src={image.src}
            alt={`Slide ${i}`}
            className={`carouselItem banner${i + 1}`}
          />
          <div className="carousel-txt-container">
            <h2>{image.title}</h2>
            <p>
              {image.description.split("\n").map((line, index) => (
                <React.Fragment key={index}>
                  {line}
                  <br />
                </React.Fragment>
              ))}
            </p>
          </div>
        </div>
      ))}

      <div className="carousel-btn-container">
        <button className="prev btn-carousel" onClick={() => moveSlide(-1)}>
          ❮
        </button>
        <button className="next btn-carousel" onClick={() => moveSlide(1)}>
          ❯
        </button>
      </div>
    </div>
  );
};

export default Carrossel;
