import React from "react";
import Dashboard from "../assets/dashboard.png";

const Hero = () => {
  return (
    <div className="px-8 py-16 flex flex-col lg:flex-row items-center justify-between gap-12 shadow-xl">
      {/* left side */}
      <div className="w-full lg:w-1/2 flex flex-col gap-6">
        <h1 className="text-4xl lg:text-5xl font-semibold leading-snug">
          <span className="text-accent">Manage</span>,{" "}
          <span className="text-[#8D94E0]">Track</span>, and{" "}
          <span className="text-secondary">Grow</span> Your Wealth Smarter — All
          in One Place
        </h1>
        <p className="text-lg text-black">
          NeuroVest brings your financial life together — from budgeting and
          expenses to personalized investment insights — so you can make
          confident, informed decisions every day.
        </p>
        <div className="flex gap-4 mt-4">
          <button className="bg-secondary text-white px-6 py-3 rounded-full hover:bg-hover-secondary transition">
            Start Managing Now
          </button>
          <button className="border border-accent text-accent px-6 py-3 rounded-full hover:bg-hover-accent hover:text-white transition">
            See How it Works
          </button>
        </div>
      </div>

      {/* right side */}
      <div className="w-full lg:w-1/2 flex justify-center">
        <img
          src={Dashboard}
          alt="dashboard"
          className="max-w-full h-auto rounded-2xl shadow-xl"
        />
      </div>
    </div>
  );
};

export default Hero;
