import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import App from './App'; // Import App component
import Login from './components/Login'; // Import Login component
import Register from './components/Register'; // Import Register component

const Root = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        {/* Đảm bảo rằng Route cho trang App được đặt cuối cùng */}
        
        <Route component={App} />
      </Switch>
    </Router>
  );
};

export default Root;
