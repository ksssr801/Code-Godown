import React, { Component } from 'react';
import {Link} from 'react-router-dom';

export default class Home extends Component {
    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-10 mx-auto pt-5 text-center">
                        <h1>Welcome To </h1><h5><i>Dragable </i></h5><h4>And </h4><h3>Resizable !</h3>
                        <Link to="/view" className="ml-auto" title="View">
                            <h4><u>View Dashboard</u></h4>
                        </Link>
                        <Link to="/edit" className="ml-auto" title="Edit">
                            <h4><u>Edit Dashboard</u></h4>
                        </Link>
                        <Link to="/playground" className="ml-auto" title="PlayGround">
                            <h4><u>Play Ground</u></h4>
                        </Link>
                    </div>
                </div>
            </div>
        )
    }
}