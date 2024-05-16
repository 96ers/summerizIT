import { i,i2 } from "../assets";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

const Alert = ({ count }) => {
  return count > 0 ? (
    <div id="alert-additional-content-2" className="alert_box_yellow" role="alert">
      <div className="flex items-center">
        <img src={i2} alt="i" className="mr-2 h-auto w-auto" />
        <span className="sr-only">Info</span>
        <h3 className="text-lg font-medium">Your access is limited!</h3>
      </div>
      <div className="mt-0 mb-1 text-sm">
        <p>
          You have 10 free access to our service. To get unlimited access and
          get all history, please login or sign up!
        </p>
        <span>Number of free access left: {count}/10</span>
      </div>
      <div className="flex flex-row max-h-8">
      </div>
    </div>
  ) : (
    <div id="alert-additional-content-2" className="alert_box" role="alert">
      <div className="flex items-center">
        <img src={i} alt="i" className="mr-2 h-auto w-auto" />
        <span className="sr-only">Info</span>
        <h3 className="text-lg font-medium">Your access is over!</h3>
      </div>
      <div className="mt-0 mb-1 text-sm">
        <p>
          We give you 10 free acceses to our service. To get unlimited access and
          get all history, please login or sign up!
        </p>
      </div>
      <div className="flex flex-row max-h-8">
        <Link to="/login" className="alert_login">
          <button type="button">Login</button>
        </Link>

        <Link to="/register" className="alert_signup">
          <button type="button">Signup</button>
        </Link>
      </div>
    </div>
  );
};

Alert.propTypes = {
  count: PropTypes.number.isRequired,
};

export default Alert;
