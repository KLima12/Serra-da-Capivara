import React, { useState, useEffect } from "react";

const getMediaPath = (path) => {
  return `${process.env.PUBLIC_URL || ""}/media/${path}`;
};

const img1 = getMediaPath("banners/banner-1.webp");
const img2 = getMediaPath("banners/banner-2.webp");
const img3 = getMediaPath("banners/banner-3.webp");

const images = [
  getMediaPath("banners/banner-1.webp"),
  getMediaPath("banners/banner-2.webp"),
  getMediaPath("banners/banner-3.webp"),
];

const Carrossel = () => {
  const [index, setIndex] = useState(0);
  const [timer, setTimer] = useState(null);

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
    if (timer) clearInterval(timer);
    const newTimer = setInterval(() => moveSlide(1), 5000);
    setTimer(newTimer);
  };

  useEffect(() => {
    restartInterval();
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="carousel">
      {images.map((src, i) => (
        <img
          key={i}
          src={src}
          alt={`Slide ${i}`}
          className={`carouselItem banner${i + 1} ${i === index ? "active" : ""}`}
        />
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
