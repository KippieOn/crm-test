import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import About from './components/About';
import NotFound from './components/NotFound';
import MainView from './components/MainView';
import Login from './components/Login';
import ForgotPassword from './components/ForgotPassword';
import './routes.css'

const Routes = (props) => (
  <Router {...props}>
    <Switch>
      <Route exact path="/" component={MainView} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/resetpassword" component={ForgotPassword} />
      <Route exact path="/about" component={About} />
      <Route path="*" component={NotFound} />
    </Switch>
  </Router>
);

export default Routes
