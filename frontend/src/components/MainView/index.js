import React, { Component } from 'react'
import { Layout, Menu, Icon, Switch } from 'antd'
import SideBar from './SideBar'
import DataTable from './TempData'
import './style.css'

const { Header, Sider, Content, Footer } = Layout;
const SubMenu = Menu.SubMenu;


class MainView extends Component {
  state = {
    collapsed: 'false',
    theme: 'dark',
  }

  componentWillMount = () => {}

  onCollapse = (collapsed) => {
    this.setState({ collapsed });
  }

  changeTheme = (value) => {
    this.setState({
      theme: value ? 'dark': 'light',
    })
  }


  render () {
    return (
      <Layout>
        <Sider
          collapsible
          collapsed={this.state.collapsed}
          onCollapse={this.onCollapse}
          theme={this.state.theme}
         >
           <Menu theme={this.state.theme} defaultSelectedKeys={['1']} mode="inline">
             <Menu.Item key="1">
               <Icon type="pie-chart" />
               <span>Option 1</span>
             </Menu.Item>
             <Menu.Item key="2">
               <Icon type="desktop" />
               <span>Option 2</span>
             </Menu.Item>
             <SubMenu
               key="sub1"
               title={<span><Icon type="user" /><span>User</span></span>}
             >
               <Menu.Item key="3">Tom</Menu.Item>
               <Menu.Item key="4">Bill</Menu.Item>
               <Menu.Item key="5">Alex</Menu.Item>
             </SubMenu>
             <SubMenu
               key="sub2"
               title={<span><Icon type="team" /><span>Team</span></span>}
             >
               <Menu.Item key="6">Team 1</Menu.Item>
               <Menu.Item key="8">Team 2</Menu.Item>
             </SubMenu>
             <Menu.Item key="9">
               <Icon type="file" />
               <span>File</span>
             </Menu.Item>
            </Menu>
            <Switch
               checked={this.state.theme === 'dark'}
               onChange={this.changeTheme}
               checkedChildren="Dark"
               unCheckedChildren="Light"
               className="bottom-switch"
             />
        </Sider>
        <Layout>
         <Header style={{ background: '#fff', padding: 0 }} />
          <Content className="padding-data minimum-height">
              <DataTable />
          </Content>

        </Layout>
    </Layout>
    )
  }
}

export default MainView
