import React from "react";
import Logo from "../assets/logo.png";

const Navbar = () => {
  return (
    <nav className="px-16 py-5 flex items-center justify-between font-medium">
      {/* logo */}
      <a href="/">
        <img src={Logo} alt="logo" className="w-42" />
      </a>

      {/* navItems */}
      <ul className="flex gap-9">
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">Features</a>
        </li>
        <li>
          <a href="#">Pricing</a>
        </li>
        <li>
          <a href="#">Contact</a>
        </li>
      </ul>

      {/* buttons */}
      <ul className=" flex gap-[18px]">
        <li>
          <a
            href="#"
            className="px-6 py-3 bg-secondary hover:bg-hover-secondary transition text-white rounded-full"
          >
            Login
          </a>
        </li>
        <li>
          <a href="#" className="hover:text-hover-secondary">Learn More</a>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
