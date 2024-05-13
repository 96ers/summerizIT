import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import App from './App'; // Import App component
import Login from './components/Login'; // Import Login component
import Register from './components/Register'; // Import Register component
import { AuthApp } from './components/auth/AuthApp'; // Import AuthApp component
import PrivateRoute from './components/auth/PrivateRoute';
import AuthHistory from './components/auth/AuthHistory';

// TODO:temporary route for testing



const Root = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/history"
          element={
            <PrivateRoute>
              <AuthHistory />
            </PrivateRoute>
          }>
        </Route>
        <Route 
          path='/auth'
          element={
            <PrivateRoute>
              <AuthApp/>
            </PrivateRoute>
          }>
        </Route>
      </Routes>
    </Router>
  );
};

export default Root;