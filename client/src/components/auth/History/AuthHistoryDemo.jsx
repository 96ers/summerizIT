import { useEffect, useState } from "react";
import { tick, copy } from "../../../assets";
import { useSelector } from "react-redux";
import api from "../../../redux/api";

const AuthHistoryDemo = () => {
  const [copied, setCopied] = useState("");
  const [data, setData] = useState([]);
  const user = useSelector((state) => state.auth.login.currentUser);
  const access_token = user?.access_token;
  const user_id = user?.id;

  // call the API to get all the articles when the component is loaded
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
        item =>
          item.id &&
          item.source_text &&
          item.summarized_text &&
          item.time
      );
      setData(filteredData);

      console.log(`Data after filtering: ${JSON.stringify(filteredData)}`);
      } catch (err) {
        console.log(err);
      }
    };
    fetchData();
  }, [user_id, access_token]);

  const handleCopy = (id, text) => {
    navigator.clipboard.writeText(text);
    setCopied(id + text);
    setTimeout(() => setCopied(""), 2000); // Reset the state after 2 seconds
  };

  const formatDate = (dateString) => {
    const options = { year: "numeric", month: "2-digit", day: "2-digit" };
    return new Date(dateString).toLocaleDateString("en-GB", options);
  };

  return (
    <div className="container mx-auto mt-16 p-4 bg-white shadow-lg rounded-lg overflow-x-auto">
      <h1 className="text-center text-2xl font-semibold mb-2 text-gray-800">
        Your Account History
      </h1>
      <h2 className="text-center text-xl font semibold ">
        Total: <span className="text-blue-500 font-bold">{data.length}</span> 
      </h2>
      <div className="border-2 border-dashed border-orange-500">
        <table className="w-full border-gray-300">
          <thead>
            <tr>
              <th className="py-3 px-2 text-center border-gray-300 bg-gray-200 font-semibold">
                <p className="text-black">Date</p>
              </th>
              <th className="py-3 px-2 text-center border-gray-300 bg-gray-200 font-semibold">
                <p className="blue_gradient">Your Article</p>
              </th>
              <th className="py-3 px-2 text-center border-gray-300 bg-gray-200 font-semibold">
                <p className="orange_gradient">Article Summarize</p>
              </th>
            </tr>
          </thead>
          <tbody>
            {data.length > 0 &&
              data.map((item, index) => (
                <tr key={index} className="hover:bg-amber-50">
                  <td className="px-2 py-3 border-l-0 border border-gray-100 text-center overflow-hidden text-ellipsis whitespace-nowrap max-w-[120px]">
                    {formatDate(item.time)}
                  </td>
                  <td className="px-2 border border-gray-100 overflow-hidden text-ellipsis whitespace-nowrap max-w-[300px]">
                    <div className="flex items-center">
                      <div
                        className="copy_btn mr-2 flex-shrink-0"
                        onClick={() => handleCopy(item.id, item.source_text)}
                        title={
                          copied === item.id + item.source_text
                            ? "Copied"
                            : "Copy"
                        }
                      >
                        <img
                          src={
                            copied === item.id + item.source_text ? tick : copy
                          }
                          alt={
                            copied === item.id + item.source_text
                              ? "tick_icon"
                              : "copy_icon"
                          }
                          className="w-4 h-4 object-contain"
                        />
                      </div>
                      <p className="overflow-hidden text-ellipsis whitespace-nowrap">
                        {item.source_text}
                      </p>
                    </div>
                  </td>
                  <td className="px-2 border border-gray-100 overflow-hidden text-ellipsis whitespace-nowrap max-w-[300px]">
                    <div className="flex items-center">
                      <div
                        className="copy_btn mr-2 flex-shrink-0"
                        onClick={() =>
                          handleCopy(item.id, item.summarized_text)
                        }
                        title={
                          copied === item.id + item.summarized_text
                            ? "Copied"
                            : "Copy"
                        }
                      >
                        <img
                          src={
                            copied === item.id + item.summarized_text
                              ? tick
                              : copy
                          }
                          alt={
                            copied === item.id + item.summarized_text
                              ? "tick_icon"
                              : "copy_icon"
                          }
                          className="w-4 h-4 object-contain"
                        />
                      </div>
                      <p className="overflow-hidden text-ellipsis whitespace-nowrap">
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
  );
};

export default AuthHistoryDemo;
