import React, { Component } from 'react';
// import {Link} from 'react-router-dom';
import {NavWrapper} from '../styled-css';

class NavBar extends Component {
    render() {
        return (
            <div>
                <NavWrapper className="navbar navbar-expand-sm store-nav navbar-dark px-sm-5">
                    <i className="fa fa-camera-retro fa-3x" title="D&R" />
                    <ul className="navbar-nav align-items-center">
                        <li className="nav-item ml-5">
                            <h3 className="home-style">Dragable And Resizable</h3>
                        </li>
                    </ul>
                </NavWrapper>                
            </div>
        )
    }
}

export { NavBar };