import { useState, useEffect } from "react";
import {
  copy,
  linkIcon,
  loader,
  tick,
  submit,
  book,
  delete_btn,
} from "../assets";
import api from "../redux/api";
import Alert from "./Alert";

const Demo = () => {
  const [inputType, setInputType] = useState("text");
  const [fileUploaded, setFileUploaded] = useState(false);
  const [showTranslate, setShowTranslate] = useState(false);
  const [copied, setCopied] = useState(false);
  const [inputValue, setInputValue] = useState("");
  const [article, setArticle] = useState({
    input: "",
    summary: "",
    translated_summary: "",
  });
  // set access limit counter to 10 
  const [counter, setCounter] = useState(() => {
    const savedCounter = sessionStorage.getItem("counter");
    return savedCounter ? JSON.parse(savedCounter) : 10;
  });
  //get api state
  const [isFetching, setIsFetching] = useState(false);
  // get all articles
  const [allArticles, setAllArticles] = useState([]); 
  // loading session storage on mount
  useEffect(() => {
    const articlesSessionStorage = JSON.parse(
      sessionStorage.getItem("articles")
    );

    if (articlesSessionStorage) {
      setAllArticles(articlesSessionStorage);
    }
  }, []);

  // get the counter from local storage
  useEffect(() => {
    sessionStorage.setItem('counter', JSON.stringify(counter));
  }, [counter]);


  // handle: upload a pdf file
  const handleInputChange = (event) => {
    event.preventDefault();
    // check if a file is uploaded
    if (inputType === 'text') {
      setArticle({ ...article, input: event.target.value });
      setInputValue(event.target.value);
    } else if (inputType === 'file') {
      const file = event.target.files[0];
      if (file) {
        setFileUploaded(true);
      }
    }
  };

  const handleFileUploadClick = (event) => {
    event.preventDefault();
    // handle change in input file
    if (fileUploaded) {
      setInputType("text");
      setFileUploaded(false);
    } else {
      setInputType("file");
    }
  };

  // handle form submit
  const handleFormSubmit = async (e) => {
    e.preventDefault();
    const existingArticle = allArticles.find(
      (item) => item.input === article.input
    );
    if (existingArticle) {
      return setArticle(existingArticle);
    }
    if (inputType === "text") {
      console.log(`Input value: ${inputValue}`);
      const response = [];
      setIsFetching(true);
      try {
        const res = await api.post(
          "summary-free",
          { source_text: inputValue },
        );
        console.log(res);
        if (res.data?.summarized_text) {
          const response_summary = res.data.summarized_text;
          response.push(response_summary);
          console.log(`let response_summary: ${response_summary}`);
          try {
            const res = await api.post(
              "translate-free",
              { source_text: response_summary },
              
            );
            console.log(`translate response: ${JSON.stringify(res.data)}`);
            if (res.data?.translated_text) {
              const translated_summary = res.data.translated_text;
              response.push(translated_summary);
              console.log(`translated_summary: ${translated_summary}`);
            }
          } catch (error) {
            console.log(error);
          }
        }
      } catch (error) {
        console.log(error);
      } finally {
        setIsFetching(false);
        const newArticle = {
          ...article,
          input: inputValue,
          summary: response[0],
          translated_summary: response[1],
        };
        console.log(`New Article: ${JSON.stringify(newArticle)}`);
        setArticle(newArticle);
        const updatedAllArticles = [...allArticles, newArticle];
        setAllArticles(updatedAllArticles);
        // save to local storage
        sessionStorage.setItem("articles", JSON.stringify(updatedAllArticles));
        setCounter(counter - 1);
      }
    }
    console.log(`Article: ${JSON.stringify(allArticles)}`);
  }

  // handle copy
  const handleCopy = (text) => {
    setCopied(text);
    navigator.clipboard.writeText(text);
    setTimeout(() => setCopied(false),  3000);
  }

  // handle show translate
  const handleShowTranslate = () => {
    setShowTranslate(!showTranslate);
  }

  return (
    <section className="mt-16 w-full max-w gap-2 max-w-xl">
      {/* Show the input form */}
      <div className="flex flex-col w-full">
        <form
          className="relative flex justify-center items-center"
          onSubmit={handleFormSubmit}
        >
          <img
            src={book}
            alt="book"
            className="absolute left-0 my-2 ml-3 w-5 cursor-pointer"
            onClick={() => setInputType("text")}
            title="Enter the text"
          />
          <input
            type={inputType}
            accept={inputType === "file" ? ".pdf" : ""}
            placeholder="Enter the text or upload a PDF file"
            className="url_input peer"
            value={article.input}
            onChange={handleInputChange}
            onKeyDown={(e) => e.key === "Enter" && handleFormSubmit(e)}
            required
          />

          <button
            className="link_btn"
            onClick={handleFileUploadClick}
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
      {/* Show the limited time alert */}
      <Alert count={counter}/>
      {/* Show the history */}
      <div className="flex flex-col gap-1 max-h-60 overflow-y-auto mt-4">
        {allArticles.slice().reverse().map((item, index) => (
          <div key={`link-${index}`} onClick={() => setArticle(item)} className="link_card">
            <div className="copy_btn" onClick={() => handleCopy(item.input)}>
              <img 
                src={copied === item.input ? tick : copy} 
                alt={copied === item.input ? "tick_icon" : "copy_icon"}
                className='w-[40%] h-[40%] object-contain'
                title={copied === item.input ? "copied" : "copy"}/>
            </div>
            <p className="history_item">
              {item.input}
            </p>
          </div>
        ))}
      </div>
      {/* Show the summary */}
      <div className="my-10 max-w-full flex justify-center items-center">
        {isFetching ? (
          <img src={loader} alt="loader" className="w-20 h-20 object-contain" />
        ) : (
          article.summary &&
          article.translated_summary && (
            <div className="flex flex-col gap-3">
              {!showTranslate ? (
                <h2 className="font-satoshi font-bold tex-gray-600 text-xl">
                  Article <span className="blue_gradient"> Summarized{""}</span>
                  . Click{" "}
                  <span
                    className="orange_gradient cursor-pointer"
                    onClick={handleShowTranslate}
                  >
                    {" "}
                    Translate{" "}
                  </span>
                  to VietNamese <span>🇻🇳</span>
                </h2>
              ) : (
                <h2 className="font-satoshi font-bold tex-gray-600 text-xl">
                  Translated to{" "}
                  <span className="orange_gradient "> VietNamese{""}</span>.
                  Back to{" "}
                  <span
                    className="blue_gradient cursor-pointer"
                    onClick={handleShowTranslate}
                  >
                    {" "}
                    Summary{" "}
                  </span>
                </h2>
              )}
              {!showTranslate ? (
                <div className="summary_box">
                  <p className="font-inter font-medium text-sm text-gray-700">
                    {article.summary}
                  </p>
                </div>
              ) : (
                <div className="translate_box">
                  <p className="font-inter font-medium text-sm text-gray-700">
                    {article.translated_summary}
                  </p>
                </div>
              )}
            </div>
          )
        )}
      </div>
    </section>
  );
};

export default Demo;
