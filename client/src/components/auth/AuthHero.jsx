import { logo, user_logo, logout, app_history } from "../../assets";
import { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import DropdownItem from "./DropdownItem";
import { useDispatch, useSelector } from "react-redux";
import { logOut } from "../../redux/apiRequest";

const AuthHero = () => {
  // get the user logged from the store
  const user = useSelector((state) => state.auth.login.currentUser);
  const access_token = user?.access_token;
  const user_id = user?.id;
  const dispatch = useDispatch();
  const navigate = useNavigate();

  //logout 
  const handleLogout = () => {
    logOut(dispatch, navigate, access_token, user_id)
      .catch((err) => console.log(err));
  }

  // account menu
  let menuRef = useRef();
  const [open, setOpen] = useState(false);

  useEffect(() => {
    let handler = (e) => {
      if (!menuRef.current.contains(e.target)) {
        setOpen(false);
        console.log(menuRef.current);
      }
    };

    document.addEventListener("mousedown", handler);

    return () => {
      document.removeEventListener("mousedown", handler);
    };
  });




  return (
    <header className="w-full flex justify-center items-center flex-col">
      <nav
        style={{ backgroundColor: "transparent" }}
        className="flex justify-between items-center w-full mb-10 pt-3"
      >
        <img src={logo} alt="sumz_logo" className="w-28 object-contain" />
        {/*Add the username when logged in*/}

        <div className="menu-container" ref={menuRef}>
          <div
            className="menu-trigger"
            onClick={() => {
              setOpen(!open);
            }}
          >
            <img src={user_logo} alt="user_logo" />
          </div>

          <div className={`dropdown-menu ${open ? "active" : "inactive"}`}>
            <h3 className="name_tag"><span className="blue_gradient">Hello, </span>{user.username}</h3>

            <ul>
              <DropdownItem img={app_history} text="App History" link="/history" />
              <DropdownItem img={logout} text="Logout" onClick={handleLogout}/>
            </ul>
          </div>
        </div>
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
