/* eslint-disable react/prop-types */

function DropdownItem(props) {
  return (
    <button onClick={props.onClick}>
      <li className="dropdownItem">
        <img src={props.img} />
        <p>{props.text}</p>
      </li>
    </button>
  );
}

export default DropdownItem;
