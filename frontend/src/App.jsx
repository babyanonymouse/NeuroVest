import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import ValueProposition from "./components/ValueProposition";
import HowItWorks from "./components/HowItWorks";
import Testimonials from "./components/Testimonials";
import Footer from "./components/Footer";

const App = () => {
  return (
    <main className="bg-background">
      <Navbar />
      <Hero/>
      <ValueProposition/>
      <HowItWorks/>
      <Testimonials/>
      <Footer/>
    </main>
  );
};

export default App;
