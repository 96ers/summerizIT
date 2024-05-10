import { logo, user_logo } from "../../assets";


import { Link } from "react-router-dom";

import { useSelector } from "react-redux";

const AuthHero = () => {

  const user = useSelector((state) => state.auth.login.currentUser);

  return (
    <header className="w-full flex justify-center items-center flex-col">
      <nav
        style={{ backgroundColor: "transparent" }}
        className="flex justify-between items-center w-full mb-10 pt-3"
      >
        <img src={logo} alt="sumz_logo" className="w-28 object-contain" />
        {/*Add the username when logged in*/}
        <h2 className="font-satoshi font-bold text-gray-600 text-xl">
          <span className="blue_gradient" >Hello, </span>
          {user.username}
        </h2>
        {/* Add user logo */}
        <img src={user_logo} alt="user_logo" />

      </nav>

      <h1 className="head_text">
        Summarize Articles with <br className="max-md:hidden" />
        <span className="orange_gradient ">Our AI tool!</span>
      </h1>
      <h2 className="desc">
        Simplify your reading with <strong>SummazIT!</strong>, an article
        summarizer that transforms lengthy articles into clear and concise
        summaries
      </h2>
    </header>
  );
};

export default AuthHero;
