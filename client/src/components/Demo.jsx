import { useState } from 'react';
import { copy, linkIcon, loader, tick, submit } from "../assets";
import { Link } from "react-router-dom";

const Demo = () => {
  const [option, setOption] = useState("Paste");
  const [showComboBox, setShowComboBox] = useState(false);

  return (
    <section className="mt-16 w-full max-w gap-2">
      {/* Show the input form */}
      <div className="flex flex-col w-full">
        <form
          className="relative flex justify-center items-center"
          onSubmit={() => {}}
        >
          <img
            src={linkIcon}
            alt="link_icon"
            className="absolute left-0 my-2 ml-3 w-5"
            onClick={() => setShowComboBox(prevShow => !prevShow)}
          />

          {showComboBox && (
            <select
              value={option}
              onChange={(e) => setOption(e.target.value)}
              className="absolute left-0 my-2 ml-3 w-5"
            >
              <option value="Paste">Paste</option>
              <option value="PDF">PDF</option>
            </select>
          )}

          {option === "Paste" ? (
            <input
              type="text"
              placeholder="Paste the article here!"
              value=""
              onChange={() => {}}
              required
              className="url_input peer"
            />
          ) : (
            <input
              type="file"
              accept=".pdf"
              onChange={() => {}}
              required
              className="url_input peer"
            />
          )}

          <button type="submit" className='submit_btn'>
            <img src={submit} alt="Submit" />
          </button>
        </form>
      </div>
    </section>
  );
};

export default Demo;