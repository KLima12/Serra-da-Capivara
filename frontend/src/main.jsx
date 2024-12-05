import React from "react";
import ReactDOM from "react-dom/client";
import Header from "./components/header";
import Footer from "./components/footer";

const headerElement = document.getElementById("react-header");
const footerElement = document.getElementById("react-footer");

if (headerElement) {
  ReactDOM.createRoot(headerElement).render(<Header />);
}

if (footerElement) {
  ReactDOM.createRoot(footerElement).render(<Footer />);
}
