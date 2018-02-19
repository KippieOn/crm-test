// src/components/Login/EnsureLoggedIn.js
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Route, Switch, Redirect, withRouter } from 'react-router-dom';
import AuthService from '../../service/auth';
import AuthAction from '../../actions/auth';
import MainView from '../MainView';
import Forgot from '../ForgotPassword';

class EnsureLoggedInContainer extends Component {

  componentDidMount() {
    if(!AuthService.isLoggedIn()){
      this.props.history.replace('login');
    }
  }


  render() {
		return (
			<Switch>
				<Route exact path="/" component={MainView}/>
        <Route exact path="/home" component={Forgot}/>
			</Switch>
		)
  }
}

export default withRouter(EnsureLoggedInContainer);
