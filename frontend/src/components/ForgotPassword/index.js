// src/components/Login/index.js
import React, { Component } from 'react';
import { Form, Icon, Input, Button, Checkbox, Layout } from 'antd';
import PropTypes from 'prop-types';
import classnames from 'classnames';
import './style.css';

const { Content } = Layout;
const FormItem = Form.Item;

class ForgotPassword extends Component {

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.form.validateFields((err, values) => {
      if (!err) {
        console.log('Received values of form: ', values);
      }
    });
  }

  render() {
    const { className, ...props } = this.props;
    const { getFieldDecorator } = this.props.form;
    return (
      <Layout style={{ height: '100vh',display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
        <Content style={{display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
        <Form onSubmit={this.handleSubmit} className="reset-password-form">
        <FormItem>
          {getFieldDecorator('email', {
            rules: [{
              type: 'email', message: 'The email is not valid!',
            }, {
              required: true, message: 'Please enter your Email!',
            }],
          })(
            <Input prefix={<Icon type="user" style={{ color: 'rgba(0,0,0,.25)' }} />} placeholder="Email" />
          )}
        </FormItem>

        <FormItem>
          <Button type="primary" htmlType="submit" className="reset-form-button">
            Reset password
          </Button>
        </FormItem>
      </Form>
      </Content>
    </Layout>
    );
  }
}

export default Form.create()(ForgotPassword);
