import React, { useEffect } from "react";
import { useInView } from "react-intersection-observer";
import "./Main.css";

const YourComponent = () => {
  const { ref: ref1, inView: inView1 } = useInView({ triggerOnce: true });
  const { ref: ref2, inView: inView2 } = useInView({ triggerOnce: true });
  const { ref: ref3, inView: inView3 } = useInView({ triggerOnce: true });
  const { ref: ref4, inView: inView4 } = useInView({ triggerOnce: true });

  return (
    <main
      id="main"
      className="flex flex-col py-32 px-4 pb-[219px] justify-center items-center bg-customBlue overflow-hidden relative"
    >
      <div className="flex flex-col gap-12 w-[80%] z-10 lg:w-[80%]">
        <div className="flex flex-col text-center mb-14 lg:pl-40">
          <div className="text-center lg:text-center w-full max-w-4xl">
            <h2 className="font-bold ml-16 pl-12 text-4xl text-textBlack">
              Unlocking the Future of Dementia Detection
            </h2>
            <p className="mt-2 text-lg">Welcome to Our Research Hub!</p>
          </div>
        </div>
      </div>
      <div className="flex flex-col gap-12 w-[80%] z-10 lg:w-[80%]">
        {/* Left-Aligned Box with Left Slide-In Animation */}
        <div
          ref={ref1}
          className={`box bg-white shadow-lg rounded-lg p-8 pl-10 pr-10 text-left w-full lg:w-[90%] mx-auto h-56 ${
            inView1 ? "animate-slide-in-left" : ""
          }`}
        >
          <h2 className="font-bold text-3xl text-textBlue">Why It Matters</h2>
          <p className="mt-10 text-xl">
            Imagine a world where advanced technology empowers us to detect
            dementia in its earliest stages—where individuals and families
            receive the support they need when it matters most. That’s our
            mission!
          </p>
        </div>

        {/* Right-Aligned Box with Right Slide-In Animation */}
        <div
          ref={ref2}
          className={`box bg-white shadow-lg rounded-lg p-8 pl-10 pr-10 text-left w-full lg:w-[90%] mx-auto h-56 ${
            inView2 ? "animate-slide-in-right" : ""
          }`}
        >
          <h2 className="font-bold text-3xl text-textBlue">
            Our Innovative Approach
          </h2>
          <p className="mt-10 text-xl">
            We harness deep learning and machine learning techniques to
            revolutionize dementia detection using a specialized Convolutional
            Neural Network (CNN) powered by TensorFlow and Keras.
          </p>
        </div>

        {/* Left-Aligned Box with Left Slide-In Animation */}
        <div
          ref={ref3}
          className={`box bg-white shadow-lg rounded-lg p-8 pl-10 pr-10 text-left w-full lg:w-[90%] mx-auto h-56 ${
            inView3 ? "animate-slide-in-left" : ""
          }`}
        >
          <h2 className="font-bold text-3xl text-textBlue">
            Our Continued Commitment
          </h2>
          <p className="mt-10 text-xl">
            Our research continually adapts and grows, leveraging new findings
            to improve detection methods and patient outcomes.
          </p>
        </div>

        {/* Right-Aligned Box with Right Slide-In Animation */}
        <div
          ref={ref4}
          className={`box bg-white shadow-lg rounded-lg p-8 pl-10 pr-10 text-left w-full lg:w-[90%] mx-auto h-56 ${
            inView4 ? "animate-slide-in-right" : ""
          }`}
        >
          <h2 className="font-bold text-3xl text-textBlue">
            Join Us on This Journey!
          </h2>
          <p className="mt-10 text-xl">
            Explore our findings, learn about our methodology and engage with
            our community. Together, we can make significant strides in
            addressing the global challenge of dementia.
          </p>
        </div>
      </div>

      <div className="z-10 mt-10">
        <img
          className="h-[300px] w-[300px] mx-auto"
          src="/brain.png"
          alt="Brain Image"
        />
      </div>
      <div className="mt-6">
        <a
          className="self-center lg:self-start bg-textBlue text-white font-bold w-52 p-6 rounded-xl text-center hover:bg-sky-700 ease-in-out duration-500 text-lg "
          href="/#feature"
        >
          Get Started
        </a>
      </div>
      <div className="primary-color-border primary-color-[100] absolute -left-56 top-20 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100"></div>
      <div className="primary-color-border primary-color-[100] absolute -right-56 top-60 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100"></div>
    </main>
  );
};

export default YourComponent;
