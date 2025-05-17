import React from "react";
import Linechart from "../assets/linechart.png";
import Sparkles from "../assets/sparkles.png";
import Shield from "../assets/shield.png";
import Refresh from "../assets/refresh.png";
import Addfriends from "../assets/add-friends.png";

const ValueProposition = () => {
  return (
    <div className="py-20 px-23 flex flex-col gap-13">
      {/* header */}
      <div className="flex flex-col gap-3 justify-center items-center">
        <h1 className="text-4xl font-bold">Built For Smarter Money Moves</h1>
        <p className="text-lg">
          Everything you need to understand, grow, and manage your finances —
          powered by intelligent insights.
        </p>
      </div>
      {/* cards */}
      <div className="flex justify-center gap-18">
        {/* card 1 */}
        <div className="p-8 bg-surface max-w-2xs rounded-2xl shadow-xl flex flex-col gap-12 text-center items-center hover:shadow-2xl transition duration-150">
          <img src={Linechart} alt="linechart" className="w-20 mb-6" />

          <h1 className="text-xl font-semibold">Smart Insights</h1>

          <p className="text-base font-light text-dark-muted">
            Get real-time breakdowns of your income, spending, and investments —
            all powered by AI.
          </p>
        </div>
        {/* card 2 */}
        <div className="p-8 bg-surface max-w-2xs rounded-2xl shadow-xl flex flex-col gap-12 text-center items-center hover:shadow-2xl transition duration-150">
          <img src={Sparkles} alt="sparkles" className="w-20 mb-6" />

          <h1 className="text-xl font-semibold">Personalized Guidance</h1>

          <p className="text-base font-light text-dark-muted">
            NeuroVest learns from your habits to suggest smarter ways to save,
            invest, and grow.
          </p>
        </div>
        {/* card 3 */}
        <div className="p-8 bg-surface max-w-2xs rounded-2xl shadow-xl flex flex-col gap-12 text-center items-center hover:shadow-2xl transition duration-150">
          <img src={Shield} alt="shield" className="w-20 mb-6" />

          <h1 className="text-xl font-semibold">Security First</h1>

          <p className="text-base font-light text-dark-muted">
            Your data is end-to-end encrypted and fully private. You control
            what’s shared and when
          </p>
        </div>
        {/* card 4 */}
        <div className="p-8 bg-surface max-w-2xs rounded-2xl shadow-xl flex flex-col gap-12 text-center items-center hover:shadow-2xl transition duration-150">
          <img src={Refresh} alt="refresh" className="w-20 mb-6" />

          <h1 className="text-xl font-semibold">Always Updated</h1>

          <p className="text-base font-light text-dark-muted">
            See up-to-date balances, new transactions, and insights in real-time
            — no refresh needed.
          </p>
        </div>
      </div>

      {/* add friends */}
      <div className="flex justify-center items-center gap-8 px-6 lg:px-21 my-13">
        {/* left */}
        <div className="w-full lg:w-1/2 flex justify-center">
          <img src={Addfriends} alt="add friends" className="w-3/4 max-w-sm" />
        </div>
        {/* right */}
        <div className="w-full lg:w-1/2 flex flex-col gap-10 justify-center items-center">
          <h1 className="text-4xl font-bold text-secondary text-center">
            Join 10,000+ users who have mastered their finances with NeuroVest.
          </h1>
          <button className="mt-4 w-fit bg-accent hover:bg-hover-accent transition text-white px-6 py-3 rounded-xl">
            See it in Action
          </button>
        </div>
      </div>
    </div>
  );
};

export default ValueProposition;
