import React from 'react';
import {
  BrowserRouter as Router,
} from 'react-router-dom';
import { Layout } from 'antd';
import Header from "./app/Header";
import Routes from './app/Routes';
import Footer from "./app/Footer";

function App() {
  return (
    <div className="App">
      <Layout className="layout">
        <Router>
          <div>
            <Header />
            <Routes />
          </div>
        </Router>
        <Footer />
      </Layout>
    </div>
  );
}

export default App;
