import React from "react";
import ReactDOM from "react-dom/client";
import Header from "./components/header";
import Footer from "./components/footer";
import Carrossel from "./components/carrossel";
import NossaHistoria from "./components/nossaHistoria";

const headerElement = document.getElementById("react-header");
const footerElement = document.getElementById("react-footer");
const carouselElement = document.getElementById("react-carousel");
const nossaHistoriaElement = document.getElementById("nossa-historia");

if (headerElement) {
  ReactDOM.createRoot(headerElement).render(<Header />);
}

if (footerElement) {
  ReactDOM.createRoot(footerElement).render(<Footer />);
}

if (carouselElement) {
  ReactDOM.createRoot(carouselElement).render(<Carrossel />);
}

if (nossaHistoriaElement) {
  ReactDOM.createRoot(nossaHistoriaElement).render(<NossaHistoria />);
}
