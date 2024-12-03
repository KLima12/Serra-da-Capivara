import React from "react";
import ReactDOM from "react-dom/client";
import Footer from "./components/footer";

const footerElement = document.getElementById("react-footer");

if (footerElement) {
  ReactDOM.createRoot(footerElement).render(<Footer />);
}
