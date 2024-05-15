/* eslint-disable react/prop-types */
import { Link } from "react-router-dom";

function DropdownItem(props) {
  return (
    <Link to={props.link}>
      <button onClick={props.onClick}>
      <li className="dropdownItem">
        <img src={props.img} />
        <p>{props.text}</p>
      </li>
    </button>
    </Link>
    
  );
}

export default DropdownItem;
