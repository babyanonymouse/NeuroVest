import React from "react";
import Arrowleft from "../assets/arrow-left.png";
import Arrowright from "../assets/arrow-right.png";

const Testimonials = () => {
  return (
    <div className="flex flex-col max-w-6xl mx-auto px-5 py-5 gap-5">
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

      {/* right- cards container */}
      <div className="flex gap-4 my-3 justify-center">
        {/* card 1 */}
        <div className="bg-surface flex flex-col p-8 gap-4 rounded-xl shadow-lg hover:shadow-2xl hover:cursor-pointer max-w-sm">
          <div className="flex justify-between gap-2">
            {/* avatar */}
            <img src="" alt="user-avatar" />
            {/* star rates */}
            <div className="flex">
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
            </div>
          </div>

          <div className="flex flex-col gap-3">
            <h2 className="text-xl font-medium">Floyd Miles</h2>
            <p className="font-light text-sm">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
              vel odio est fuga deleniti itaque quos nulla officia qui ex.
            </p>
          </div>
        </div>

        {/* card 2 */}
        <div className="bg-surface flex flex-col p-8 gap-4 rounded-xl shadow-lg hover:shadow-2xl hover:cursor-pointer max-w-sm">
          <div className="flex justify-between gap-2">
            {/* avatar */}
            <img src="" alt="user-avatar" />
            {/* star rates */}
            <div className="flex">
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
              <img src="" alt="star" />
            </div>
          </div>

          <div className="flex flex-col gap-3">
            <h2 className="text-xl font-medium">Floyd Miles</h2>
            <p className="font-light text-sm">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
              vel odio est fuga deleniti itaque quos nulla officia qui ex.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Testimonials;
