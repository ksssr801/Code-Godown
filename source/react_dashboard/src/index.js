import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './app';
import {BrowserRouter as Router} from 'react-router-dom';
import { ProductProvider } from './context';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

ReactDOM.render(
    <ProductProvider>
        <Router>
            <App />
        </Router>
    </ProductProvider>,
    document.getElementById('root')
  );
  