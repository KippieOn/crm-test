import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import About from "./components/About";
import NotFound from "./components/NotFound";
import MainView from "./components/MainView";
import EnsureLoggedIn from "./components/Login/EnsureLoggedIn";
import Login from "./components/Login";
import { Redirect } from 'react-router-dom'
import AuthService from './service/auth';
import ForgotPassword from "./components/ForgotPassword";
import { Provider } from "react-redux";

import store from "./store";
import "./routes.css";

/* PrivateRoute component definition */
const PrivateRoute = ({component: Component, authed, ...rest}) => {
  console.log("AuthService.isLoggedIn()", AuthService.isLoggedIn())
  const isLoggedIn = AuthService.isLoggedIn();
  return (
    <Route
      {...rest}
      render={(props) => authed === true
        ? <Component {...props} />
        : <Redirect to={{pathname: '/login', state: {from: props.location}}} />} />
  )
}

const Routes = props => (
  <Provider store={store}>
    <Router {...props}>
      <Switch>
        <Route exact path="/login" component={Login} />
        <Route exact path="/resetpassword" component={ForgotPassword} />
        <Route exact path="/about" component={About} />
        <Route path="/" component={EnsureLoggedIn} >
          <Route exact path="home" component={ForgotPassword} />
        </Route>

        <Route path="*" component={NotFound} />
      </Switch>
    </Router>
  </Provider>
);

export default Routes;
