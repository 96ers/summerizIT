import { useState } from "react";
import {
  copy,
  linkIcon,
  loader,
  tick,
  submit,
  book,
  delete_btn,
} from "../assets";
import { Link } from "react-router-dom";

const Demo = () => {
  const [inputType, setInputType] = useState("text");
  const [fileUploaded, setFileUploaded] = useState(false);

  // handle: upload a pdf file
  const handleInputChange = (event) => {
    // check if a file is uploaded
    const file = event.target.files[0];
    if (file) {
      setFileUploaded(true);
    }
  };

  const handleClick = (event) => {
    event.preventDefault();
    // handle change in input file
    if (fileUploaded) {
      setInputType("text");
      setFileUploaded(false);
    } else {
      setInputType("file");
    }
  };
  return (
    <section className="mt-16 w-full max-w gap-2">
      {/* Show the input form */}
      <div className="flex flex-col w-full">
        <form
          className="relative flex justify-center items-center"
          onSubmit={() => {}}
        >
          <img
            src={book}
            alt="book"
            className="absolute left-0 my-2 ml-3 w-5"
          />
          <input
            type={inputType}
            accept={inputType === "file" ? ".pdf" : undefined}
            placeholder="Enter the text or upload a PDF file"
            className="url_input peer"
            onChange={handleInputChange}
          />

          <button
            className="link_btn"
            onClick={handleClick}
            title={!fileUploaded ? "Upload a file" : "Delete this file"}
          >
            <img
              src={fileUploaded ? delete_btn : linkIcon}
              alt="Upload a pdf file"
            />
          </button>

          <button type="submit" className="submit_btn" title="Go!">
            <img src={submit} alt="Submit" />
          </button>
        </form>
      </div>
    </section>
  );
};

export default Demo;
