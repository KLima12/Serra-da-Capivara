import React from "react";
import ReactDOM from "react-dom/client";
import Footer from "./components/teste";

const footerElement = document.getElementById("react-footer");
console.log(footerElement);

if (footerElement) {
  ReactDOM.createRoot(footerElement).render(<Footer />);
}
