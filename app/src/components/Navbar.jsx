import React from "react";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between px-7 p-4 bg-customBlue">
      <div className="text-[17px]">Logo</div>

      <div className="flex">
        <ul className="flex flex-row">
          <li className="px-4"><a className="text-[17px]" href="#main">Home</a></li>
          <li className="px-4"><a className="text-[17px]" href="#feature">Services</a></li>
          <li className="px-4"><a className="text-[17px]" href="#contact">Contact</a></li>
        </ul>
      </div>
    </nav>
  );
}
