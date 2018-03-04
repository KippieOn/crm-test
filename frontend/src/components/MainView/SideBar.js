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

  renderMenu = () => {
    // get saved data and construct a list

    // for ( in len(data)) {
    //   menuList.append()
    // '<Menu.Item key='' > $NAME <Menu.Item>
    // }
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

        </Menu>
      </div>
    );
  }
}

export default SideBar
