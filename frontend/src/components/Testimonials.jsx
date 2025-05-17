import React from "react";
import Arrowleft from "../assets/arrow-left.png";
import Arrowright from "../assets/arrow-right.png";

const Testimonials = () => {
  return (
    <div className="flex flex-col max-w-6xl mx-auto mt-5">
      {/* head container */}
      <div className="flex justify-between">
        {/* left text */}
        <div className="flex flex-col gap-2">
          <h1 className="text-4xl font-semibold">What Our Users Say</h1>
          <p className="font-light text-lg">
            Real stories from people managing money smarter
          </p>
        </div>
        {/* right buttons */}
        <div className="flex gap-5 items-center">
          <button className="py-2 px-2 rounded-lg border text-sm">
            <img src={Arrowleft} alt="Arrowleft" className="inline w-6" />
            Previous
          </button>
          <button className="px-2 py-2 rounded-lg border text-sm">
            Next
            <img src={Arrowright} alt="Arrowright" className="inline w-6" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default Testimonials;
