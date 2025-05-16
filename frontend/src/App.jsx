import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import ValueProposition from "./components/ValueProposition";

const App = () => {
  return (
    <main className="bg-background">
      <Navbar />
      <Hero/>
      <ValueProposition/>
    </main>
  );
};

export default App;
