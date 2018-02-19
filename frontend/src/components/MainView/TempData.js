import React, { Component } from 'react';
import { Table, Icon, Switch, Radio, Form, Divider, Col, Row } from 'antd';
import Chance from 'chance'
import ExtendedInfo from '../ExtendedInfo'

const FormItem = Form.Item;

const columns = [{
  title: 'Name',
  dataIndex: 'name',
  key: 'name',
  width: 130,
  render: text => <a href="#">{text}</a>,
}, {
  title: 'Last name',
  dataIndex: 'lastName',
  key: 'lastName',
  width: 130,
  render: text => <a href="#">{text}</a>,
}, {
  title: 'Company name',
  dataIndex: 'company',
  key: 'company',
  width: 150,
  render: text => <a href="#">{text}</a>,
}, {
  title: 'Email',
  dataIndex: 'email',
  key: 'email',
  width: 350,
}, {
  title: 'Phone number',
  dataIndex: 'phone',
  key: 'phone',
  width: 150,
},{
  title: 'Last Contacted',
  dataIndex: 'lastContacted',
  key: 'lastContacted',
}, {
  title: 'Action',
  key: 'action',
  width: 260,
  fixed: 'right',
  render: (text, record) => (
    <span>
      <a href="#">Contact</a>
      <Divider type="vertical" />
      <a href="#">Delete</a>
      <Divider type="vertical" />
      <a href="#" className="ant-dropdown-link">
        More actions <Icon type="down" />
      </a>
    </span>
  ),
}];

const data = [];
const chance = new Chance
for (let i = 1; i <= 10; i++) {
  data.push({
    key: i,
    name: 'Ramona',
    lastName: 'Heil',
    email: `${chance.email()}`,
    phone: `${chance.phone({ country: 'uk'})}`,
    lastContacted: `${new Date().toLocaleString()}`,
    newAction: `My name is John Brown, I am ${i}2 years old, living in New York No. ${i} Lake Park.`,
  });
}

const expandedRowRender = record => <ExtendedInfo />;
// this should be the name of the list
const title = () => 'Here is title';
const showHeader = true;
const footer = () => 'Here is footer';
const scroll = { y: 240 };

class TempData extends Component {
  state = {
    bordered: false,
    loading: false,
    pagination: true,
    size: 'default',
    expandedRowRender,
    title,
    showHeader,
    footer,
    rowSelection: {},
    scroll: undefined,
  }

  handleToggle = (prop) => {
    return (enable) => {
      this.setState({ [prop]: enable });
    };
  }

  handleSizeChange = (e) => {
    this.setState({ size: e.target.value });
  }

  handleExpandChange = (enable) => {
    this.setState({ expandedRowRender: enable ? expandedRowRender : undefined });
  }

  handleTitleChange = (enable) => {
    this.setState({ title: enable ? title : undefined });
  }

  handleHeaderChange = (enable) => {
    this.setState({ showHeader: enable ? showHeader : false });
  }

  handleFooterChange = (enable) => {
    this.setState({ footer: enable ? footer : undefined });
  }

  handleRowSelectionChange = (enable) => {
    this.setState({ rowSelection: enable ? {} : undefined });
  }

  handleScollChange = (enable) => {
    this.setState({ scroll: enable ? scroll : undefined });
  }

  render() {
    const state = this.state;
    return (
      <div>
        <div className="components-table-demo-control-bar">
          <Row>
            <Form layout="inline" fixed="right">
              <Col span={24} style={{ textAlign: 'right' }}>
                <FormItem label="Size">
                  <Radio.Group size="default" value={state.size} onChange={this.handleSizeChange}>
                    <Radio.Button value="default">Default</Radio.Button>
                    <Radio.Button value="middle">Middle</Radio.Button>
                    <Radio.Button value="small">Small</Radio.Button>
                  </Radio.Group>
                </FormItem>
              </Col>
            </Form>
          </Row>
        </div>
        <Table {...this.state} columns={columns} dataSource={data} />
      </div>
    );
  }
}

export default TempData
