import React from "react";
import Account from "../assets/undraw_account.png";
import AddInfo from "../assets/add-information.png";
import Visualization from "../assets/visualization.png";

const HowItWorks = () => {
  return (
    <div className="flex flex-col gap-16 py-20 px-6 lg:px-20">
      {/* Header */}
      <div className="flex flex-col gap-6 text-center max-w-5xl mx-auto">
        <h1 className="text-4xl lg:text-5xl font-bold">How It Works</h1>
        <p className="text-lg lg:text-2xl font-normal">
          Get started in minutes. NeuroVest simplifies your financial life by
          helping you track your income, spending, goals, and investments — all
          in one secure dashboard. <br className="hidden md:block" />
          Here’s how to get going:
        </p>
      </div>

      {/* Content */}
      <div className="flex flex-col lg:flex-row items-center gap-12 max-w-7xl mx-auto">
        {/* Left - Image */}
        <div className="w-full lg:w-1/2 flex justify-center">
          <img src={Account} alt="Set up account" className="w-full max-w-md" />
        </div>

        {/* Right - Text */}
        <div className="w-full lg:w-1/2 flex flex-col gap-6">
          <h2 className="text-3xl lg:text-4xl font-semibold">
            Set Up Your Profile
          </h2>
          <p className="text-base lg:text-xl font-light text-dark-muted">
            Create your account and tell us a bit about your finances — from
            income sources to savings goals. No complicated forms.
          </p>
        </div>
      </div>

      {/* Content 2 */}
      <div className="flex flex-col lg:flex-row items-center gap-12 max-w-7xl mx-auto">
        {/* Left - Text */}
        <div className="w-full lg:w-1/2 flex flex-col gap-6">
          <h2 className="text-3xl lg:text-4xl font-semibold">
            Input your Finances
          </h2>
          <p className="text-base lg:text-xl font-light text-dark-muted">
            Log your income, expenses, debts, and investments manually. Stay
            fully in control of your financial data.
          </p>
        </div>
        {/* Right - Image */}
        <div className="w-full lg:w-1/2 flex justify-center">
          <img
            src={AddInfo}
            alt="input your finances"
            className="w-full max-w-md"
          />
        </div>
      </div>

      {/* Content 3*/}
      <div className="flex flex-col lg:flex-row items-center gap-12 max-w-7xl mx-auto">
        {/* Left - Image */}
        <div className="w-full lg:w-1/2 flex justify-center">
          <img
            src={Visualization}
            alt="visualization"
            className="w-full max-w-md"
          />
        </div>

        {/* Right - Text */}
        <div className="w-full lg:w-1/2 flex flex-col gap-6">
          <h2 className="text-3xl lg:text-4xl font-semibold">
            Visualize Your Progress
          </h2>
          <p className="text-base lg:text-xl font-light text-dark-muted">
            See your data come to life. NeuroVest builds charts and dashboards
            that show where your money is going — and how to grow it.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HowItWorks;
