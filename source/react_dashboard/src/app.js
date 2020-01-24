import React, { Component } from 'react';
import {Switch, Route} from 'react-router-dom';
import './app.css';
import './react-grid-layout.css';
import './react-resizable.css';
import './bootstrap.min.css';
import { NavBar } from './components/nav-footer';
import Home from './components/home';
import EditDashboard from './components/edit-dashboard';
import ViewDashboard from './components/view-dashboard';
import PlayGround from './components/playground';
import Default from './components/default';
// import { ModalProvider } from 'styled-react-modal';
// import { FadingBackground } from './styled-css';
import StyledDailogBox from './components/dailog-box';


// Need to read about Switch, Route
class App extends Component {
    render() {
        return (
            <React.Fragment>
                <NavBar />
                <Switch>
                  <Route exact path="/" component={Home} />
                  <Route path="/edit" component={EditDashboard} />
                  <Route path="/view" component={ViewDashboard} />
                  <Route path="/playground" component={PlayGround} />
                  <Route component={Default} />
                </Switch>
                <StyledDailogBox />

            </React.Fragment>
        );
    }
}

export default App;