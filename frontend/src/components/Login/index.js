// src/components/Login/index.js
import React, { Component } from 'react';
import { Form, Icon, Input, Button, Checkbox, Layout } from 'antd';
import { Row, Col, Spin } from 'antd'
import PropTypes from 'prop-types';
import { Redirect } from 'react-router-dom'
import classnames from 'classnames';
import AuthAction from '../../actions/auth';
import { connect } from 'react-redux';
import  AuthService from '../../service/auth';
import './style.css';

const { Content } = Layout;
const FormItem = Form.Item;

class LoginForm extends Component {

  constructor (props) {
    super(props)
    this.state = {};
    this.handleSubmit = this.handleSubmit.bind(this);

    this.updateEmail = this.updateEmail.bind(this)
    this.updatePassword = this.updatePassword.bind(this)
  }



  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.props.form);
    const form = this.props.form;
    this.props.form.validateFields((err, values) => {
      if (!err) {
        let { email, password } = this.state;
        const { dispatch } = this.props;
        dispatch(AuthAction.setLoginPending(true));
        dispatch(AuthAction.setLoginSuccess(false));
        dispatch(AuthAction.setLoginError(null));

        form.resetFields();
        AuthService.callLoginApi(email, password, result => {
          console.log("API result", result);
          dispatch(AuthAction.setLoginPending(false));
          if (!result.error) {
            dispatch(AuthAction.setLoginData(result));
            dispatch(AuthAction.setLoginSuccess(true));
          } else {
            dispatch(AuthAction.setLoginError(result));
          }
        });
      }
    });
  }

  render() {
    const { className, ...props } = this.props;
    const { getFieldDecorator } = this.props.form;
    console.log(this.props);
    let {isLoginPending, isLoginSuccess, loginError} = this.props;
    console.log("Is loggin success", isLoginSuccess);
    const { from } = this.props.location.state || { from: { pathname: '/' }}

    if(isLoginSuccess) {
      return <Redirect to="/" />
    }

    return (
      <Layout style={{ height: '100vh',display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <Content style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <Form onSubmit={this.handleSubmit} className="login-form">
          <FormItem>
            {getFieldDecorator('user', {
              rules: [{
                required: true, message: 'Please enter your username!',
              }],
            })(
              <Input prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />} value={this.state.email} onChange={this.updateEmail} placeholder="Email" />
            )}
          </FormItem>
          <FormItem>
            {getFieldDecorator('password', {
              rules: [{
                required: true, message: 'Please enter your password!',
              }],
            })(
              <Input prefix={<Icon type="lock" style={{ color: 'rgba(0,0,0,.25)' }} />} type="password" value={this.state.password} onChange={this.updatePassword} placeholder="Password" />
            )}
          </FormItem>
          { isLoginPending && <div>Please wait...</div> }
          { isLoginSuccess && <div>Success.</div> }
          { loginError && <div>{loginError.message}</div> }
          <FormItem>
            {getFieldDecorator('remember', {
              valuePropName: 'checked',
              initialValue: true,
            })(
              <Checkbox>Remember me</Checkbox>
            )}
            <a className="login-form-forgot" href="/resetpassword">Forgot password</a>
            <Button type="primary" htmlType="submit" className="login-form-button">
              { isLoginPending && <Spin size="small" /> }
              { !isLoginPending &&  "Log in" }
            </Button>
          </FormItem>
        </Form>
        </Content>
      </Layout>
    );
  }

  updateEmail (evt) {
    this.setState({
      email: evt.target.value
    });
  }
  updatePassword (evt) {
    this.setState({
      password: evt.target.value
    });
  }
}

const mapStateToProps = (state) => {
  return {
    isLoginPending: state.auth.isLoginPending,
    isLoginSuccess: state.auth.isLoginSuccess,
    loginError: state.auth.loginError
  };
}


export default connect(mapStateToProps)(Form.create()(LoginForm));
