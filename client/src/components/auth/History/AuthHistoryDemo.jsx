import { useEffect, useState, useRef } from "react";
import { useSelector } from "react-redux";
import api from "../../../redux/api";

const AuthHistoryDemo = () => {
  const [copied, setCopied] = useState("");
  const [data, setData] = useState([]);
  const user = useSelector((state) => state.auth.login.currentUser);
  const access_token = user?.access_token;
  const user_id = user?.id;
  const [inputValue, setInputValue] = useState("");

  const textareaRef = useRef(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await api.get("summary", {
          headers: {
            "user-id": user_id,
            authorization: access_token,
          },
        });
        console.log(res.data);
        console.log(`Data before filtering: ${JSON.stringify(res.data)}`);

        // Lọc các object có đầy đủ thông tin và gán lại vào state
        const filteredData = res.data.filter(
          (item) =>
            item.id && item.source_text && item.summarized_text && item.time
        );
        setData(filteredData);

        console.log(`Data after filtering: ${JSON.stringify(filteredData)}`);
      } catch (err) {
        console.log(err);
      }
    };
    fetchData();
  }, [user_id, access_token]);

  const handleCopy = (text) => {
    navigator.clipboard.writeText(text);
    setCopied("Copied!");
    setTimeout(() => setCopied(""), 2000); // Reset the state after 2 seconds
  };

  const handleRowClick = (text) => {
    setInputValue(text);
  };

  const formatDate = (dateString) => {
    const options = { year: "numeric", month: "2-digit", day: "2-digit" };
    return new Date(dateString).toLocaleDateString("en-GB", options);
  };

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [inputValue]);

  return (
    <div className="container mx-auto mt-16 p-4 bg-white shadow-lg rounded-lg">
      <div className="mb-4">
        <h1 className="text-center text-2xl font-semibold mb-2 text-gray-800">
          Your Account History
        </h1>
        <h2 className="text-center text-xl font-semibold">
          Total: <span className="text-blue-500 font-bold">{data.length}</span>
        </h2>
      </div>
      <div className="flex flex-col md:flex-row">
        <div className="w-full md:w-3/4 md:pr-2 mb-4 md:mb-0 overflow-x-auto">
          <div className="border-2 border-dashed border-orange-500">
            <table className="w-full table-auto border-collapse">
              <thead>
                <tr>
                  <th className="py-3 px-2 text-center border border-gray-300 bg-gray-200 font-semibold">
                    <p className="text-black">Date</p>
                  </th>
                  <th className="py-3 px-2 text-center border border-gray-300 bg-gray-200 font-semibold">
                    <p className="blue_gradient">Your Article</p>
                  </th>
                  <th className="py-3 px-2 text-center border border-gray-300 bg-gray-200 font-semibold">
                    <p className="orange_gradient">Article Summarize</p>
                  </th>
                </tr>
              </thead>
              <tbody>
                {data.length > 0 &&
                  data.map((item, index) => (
                    <tr key={index} className="hover:bg-amber-50">
                      <td
                        className="px-2 py-3 border border-gray-100 text-center overflow-hidden text-ellipsis whitespace-nowrap max-w-[120px]"
                      >
                        {formatDate(item.time)}
                      </td>
                      <td
                        className="px-2 border border-gray-100 overflow-hidden text-ellipsis whitespace-nowrap max-w-[300px]"
                        onClick={() => handleRowClick(item.source_text)}
                      >
                        <div className="flex items-center">
                          <p className="truncate max-w-[250px] cursor-pointer">
                            {item.source_text}
                          </p>
                        </div>
                      </td>
                      <td
                        className="px-2 border border-gray-100 overflow-hidden text-ellipsis whitespace-nowrap max-w-[300px]"
                        onClick={() => handleRowClick(item.summarized_text)}
                      >
                        <div className="flex items-center">
                          <p className="truncate max-w-[250px] cursor-pointer">
                            {item.summarized_text}
                          </p>
                        </div>
                      </td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        </div>
        <div className="w-full md:w-1/4 md:pl-0">
          <textarea
            ref={textareaRef}
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            className="w-full p-2 border-2 border-blue-500 border-dashed rounded resize-none overflow-hidden cursor-auto focus:outline-none focus:border-blue-500"
            readOnly
            placeholder="Something here..."
          />
          <button
            onClick={() => handleCopy(inputValue)}
            className="bg-white hover:scale-105 py-2 px-4 mt-1 font-bold rounded text-blue-500 border-2 border-blue-600 border-dashed"
            
          >
            {copied ? copied : "Copy"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default AuthHistoryDemo;