import React from "react";
import Logo from "../assets/logo.png";

const Footer = () => {
  return (
    <div className="flex bg-hover-secondary justify-center px-9 py-7 gap-32 text-muted">
      {/* logo */}
      <div>
        <img src={Logo} alt="logo" className="w-42" />
      </div>

      {/* learn more */}
      <div>
        <h1 className="font-medium">Learn More</h1>
        <ul className="font-light">
          <li>About us</li>
          <li>How It Works</li>
          <li>Features</li>
          <li>Blog</li>
          <li>Pricing</li>
        </ul>
      </div>

      {/* contact us */}
      <div>
        <h1 className="font-medium">Contact Us</h1>
        <ul className="font-light">
          <li>About us</li>
          <li>How It Works</li>
        </ul>
      </div>
      {/* social */}
      <div>
        <h1 className="font-medium">Social</h1>
        <ul className="font-light">
          <li>Facebook</li>
          <li>Instagram</li>
          <li>Twitter</li>
        </ul>
      </div>
    </div>
  );
};

export default Footer;
