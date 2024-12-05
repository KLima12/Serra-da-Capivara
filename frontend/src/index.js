import React from "react";
import ReactDOM from "react-dom";
import Footer from "/components/Footer.js";

const footerElement = document.getElementById("react-footer");
if (footerElement) {
  ReactDOM.render(<Footer />, footerElement);
}
