// Login.jsx
import { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import { login_img } from "../assets";
import { loginUser } from "../redux/apiRequest";
import { useDispatch } from "react-redux";

import { logo } from "../assets";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();
  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const newuser = {
      email: email,
      password: password,
    };
    loginUser(newuser, dispatch, history);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100 ">
      <div
        className="relative flex flex-col m-6 space-y-8 bg-white shadow-2xl rounded-2xl md:flex-row md:space-y-0"
        style={{ fontFamily: "Inter, sans-serif" }}
      >
        {/* left side */}
        <div className="flex flex-col justify-center p-8 md:p-14 flex-1">
          <Link to="/">
            <img src={logo} alt="sumz_logo" className="w-28 object-contain" />
          </Link>
          <span
            className="orangae_gradient text-4xl font-bold mb-2"
            style={{ fontFamily: "Satoshi, sans-serif" }}
          >
            Welcome back!
          </span>
          <span className="font-light text-gray-400 mb-8">
            Sign in to have unlimited access to <strong>SummarIT!</strong>
          </span>
          <form onSubmit={handleSubmit}>
            <div className="py-4">
              <span className="mb-2 text-md">Email</span>
              <input
                type="text"
                className="w-full p-2 border border-gray-300 rounded-md placeholder-font-light placeholder-text-gray-500"
                name="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="py-4">
              <span className="mb-2 text-md">Password</span>
              <input
                type="password"
                name="pass"
                id="pass"
                className="w-full p-2 border border-gray-300 rounded-md placeholder-font-light placeholder-text-gray-500"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>

            <div className="flex justify-between w-full py-4">
              <div className="mr-24">
                <input type="checkbox" name="ch" id="ch" className="mr-2" />
                <span className="text-md">Remember me</span>
              </div>
              <span className="font-bold text-md">Forgot password</span>
            </div>
            <button type="submit" className="black_btn w-full p-2 mb-6 ">
              Sign in
            </button>
          </form>
          <div className="text-center text-gray-400">
            Don't have an account? &nbsp;
            <span>
              <Link to="/register" className="font-bold text-black">
                Sign up for free
              </Link>
            </span>
          </div>
        </div>
        {/* right side */}
        <div className="relative">
          <img
            src={login_img}
            alt="img"
            className="w-[450px] h-[700px] hidden rounded-r-2xl md:block object-cover"
          />
        </div>
      </div>
    </div>
  );
};

export default Login;
