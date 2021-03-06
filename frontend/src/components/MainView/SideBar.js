import React, { Component } from 'react'
import PropTypes from 'prop-types';
import { Menu, Icon, Button, Switch } from 'antd'
import classnames from 'classnames'
const SubMenu = Menu.SubMenu;

class SideBar extends Component {
  state = {
    collapsed: false,
    theme: 'dark',
    current: '1'
  }

  changeTheme = (value) => {
    this.setState({
      theme: value ? 'dark': 'light',
    })
  }

  handleClick = (e) => {
    this.setState({
      current: e.key,
    })
  }

  toggleCollapsed = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  }
  render() {
    const { className, ...props } = this.props;
    return (
      <div style={{ width: 256 }} className={classnames('SideBar', className)} {...props}>
        <Button type="primary" onClick={this.toggleCollapsed} style={{ marginBottom: 16 }}>
          <Icon type={this.state.collapsed ? 'menu-unfold' : 'menu-fold'} />
        </Button>
        <Menu
          defaultSelectedKeys={['1']}
          defaultOpenKeys={['sub1']}
          mode="inline"
          theme={this.state.theme}
          inlineCollapsed={this.state.collapsed}
        >
          <Menu.Item key="1">
            <Icon type="pie-chart" />
            <span>Option 1</span>
          </Menu.Item>
          <Menu.Item key="2">
            <Icon type="desktop" />
            <span>Option 2</span>
          </Menu.Item>
          <Menu.Item key="3">
            <Icon type="inbox" />
            <span>Option 3</span>
          </Menu.Item>
          <SubMenu key="sub1" title={<span><Icon type="mail" /><span>Navigation One</span></span>}>
            <Menu.Item key="5">Option 5</Menu.Item>
            <Menu.Item key="6">Option 6</Menu.Item>
            <Menu.Item key="7">Option 7</Menu.Item>
            <Menu.Item key="8">Option 8</Menu.Item>
          </SubMenu>
          <SubMenu key="sub2" title={<span><Icon type="appstore" /><span>Navigation Two</span></span>}>
            <Menu.Item key="9">Option 9</Menu.Item>
            <Menu.Item key="10">Option 10</Menu.Item>
            <SubMenu key="sub3" title="Submenu">
              <Menu.Item key="11">Option 11</Menu.Item>
              <Menu.Item key="12">Option 12</Menu.Item>
            </SubMenu>
          </SubMenu>
          <Switch
             checked={this.state.theme === 'dark'}
             onChange={this.changeTheme}
             checkedChildren="Dark"
             unCheckedChildren="Light"
           />
        </Menu>
      </div>
    );
  }
}

export default SideBar
