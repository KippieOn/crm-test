import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import AuthService from '../../service/auth';

class Logout extends Component {
  componentDidMount() {
    AuthService.logout();
  }

  render() {
    return <Redirect to="/" />
  }
}

export default Logout;
