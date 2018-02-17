import React, { Component } from 'react'
import {Form, Input, Tooltip, Icon, Cascader, Select, Row, Col, Checkbox, Button, AutoComplete} from 'antd'
import PropTypes from 'prop-types'
import ApiClient form '../../util'

class ExtendedInfo extends Component {
    // this should update the db
    handleSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFieldsAndScroll((err, values) => {
          if (!err) {
            console.log('Received values of form: ', values);
            // call api client
          }
        });
    }

    render () {
        return (
            <Form onSubmit={this.handleSubmit} >
                <Form.Item {...props}>
                    {children}
                </Form.Item>
            </Form>
        )
    }
}

export default ExtendedInfo