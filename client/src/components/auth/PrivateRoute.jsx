import { Navigate } from "react-router-dom";
import useAuth from "../../redux/useAuth";

// eslint-disable-next-line react/prop-types
function PrivateRoute( {children, redirectTo = '/login'}) {
    const isAuthenticated = useAuth(); 
  
    return (
      isAuthenticated ? children : <Navigate to={redirectTo} />
    );
  }

export default PrivateRoute;