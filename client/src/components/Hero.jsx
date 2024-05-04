import { logo } from "../assets";
import { Link } from "react-router-dom";

const Hero = () => {
  return (
    <header className="w-full flex justify-center items-center flex-col">
      <nav style={{ backgroundColor: 'transparent' }} className="flex justify-between items-center w-full mb-10 pt-3">
        <img src={logo} alt="sumz_logo" className="w-28 object-contain" />
        {/* Add the button: Sign in */}
        <Link to="/login" className="black_btn">Login</Link>
      </nav>

      <h1 className="head_text">
        Summarize Articles with <br className="max-md:hidden" />
        <span className="orange_gradient ">Our AI tool!</span>
      </h1>
      <h2 className="desc">
        Simplify your reading with <strong>SummazIT!</strong>, an article summarizer that
        transforms lengthy articles into clear and concise summaries
      </h2>
    </header>
  );
};

export default Hero;
