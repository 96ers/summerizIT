import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { registerUser } from "../redux/apiRequest";


import { logo } from "../assets";
import { signup_img } from "../assets"; 


const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repassword, setRepassword] = useState("");

  const navigate = useNavigate();
  const dispatch = useDispatch();

  const [error, setError] = useState("");


  const handleSubmit = (e) => {
    e.preventDefault();
    if (password !== repassword) {
      setError("Passwords do not match");
      return;
    }
    const newUser = {
      email: email,
      password: password,
      username: username,
    };
    registerUser(newUser, dispatch, navigate)
      .catch((err) => setError(err));
  }

  

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="relative flex flex-col m-6 space-y-8 bg-white shadow-2xl rounded-2xl md:flex-row md:space-y-0">
        {/* right side */}
        <div className="relative">
          <img
            src={signup_img}
            alt="img"
            className="w-[450px] h-[700px] hidden rounded-l-2xl md:block object-cover"
          />
        </div>
        {/* left side */}
        <div className="flex flex-col justify-center p-8 md:p-14 flex-1">
        <Link to="/">
            <img src={logo} alt="sumz_logo" className="w-28 object-contain" />
          </Link>
          <span className="text-4xl font-bold mb-2">
            Welcome!
          </span>
          <span className="font-light text-gray-400 mb-8">
            Sign up now and join <strong>SummarIT!</strong>
          </span>
          <form onSubmit={handleSubmit}>
            <div className="py-2">
              <span className="mb-2 text-md">Username</span>
              <input
                type="text"
                className={`w-full p-2 border rounded-md placeholder-font-light placeholder-text-gray-500`}
                name="username"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="py-2">
              <span className="mb-2 text-md">Email</span>
              <input
                type="text"
                className={`w-full p-2 border rounded-md placeholder-font-light placeholder-text-gray-500`}
                name="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="py-2">
              <span className="mb-3 text-md">Password</span>
              <input
                type="password"
                name="password"
                id="password"
                className={`w-full p-2 border rounded-md placeholder-font-light placeholder-text-gray-500`}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <div className="py-2">
              <span className="mb-2 text-md">Confirm Password</span>
              <input
                type="password"
                name="repassword"
                id="repassword"
                className="w-full p-2 border border-gray-300 rounded-md placeholder-font-light placeholder-text-gray-500"
                value={repassword}
                onChange={(e) => setRepassword(e.target.value)}
                required
              />
              {error && <div className="text-red-500">{error}</div>}
            </div>
            <button
              type="submit"
              className="black_btn w-full mt-2 mb-6"
            >
              Sign up
            </button>
          </form>
          <div className="text-center text-gray-400">
            Already have an account? &nbsp;
            <span>
              <Link to="/login" className="font-bold text-black">
                Sign in here
              </Link>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;
