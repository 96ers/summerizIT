import { useSelector } from 'react-redux';

const useAuth = () => {
  const token = useSelector(state => state.auth.login.currentUser);

  if (!token) {
    // if token is not available
    return false;
  } else {
    // if token is available
    return true;
  }
};

export default useAuth;