import React, { Component } from 'react'
import { Layout } from 'antd'
import SideBar from './Sidebar'
import DataTable from './TempData'

const { Sider, Content } = Layout;

class MainView extends Component {
  state = {
    collapsed: 'false',
  }

  componentWillMount = () => {

  }


  render () {
    return (
      <Layout>
        <Sider
           trigger={null}
           collapsible
           collapsed={this.state.collapsed}
         >
            <SideBar />
        </Sider>
        <Layout>
          <Content>
              <DataTable />
          </Content>
        </Layout>
    </Layout>
    )
  }
}

export default MainView
