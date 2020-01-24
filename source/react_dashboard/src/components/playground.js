import React, { Component } from 'react';
import './playground.css';

// import ReactGridLayout from 'react-grid-layout';
// import { BtnContainer } from '../styled-css';
// import {Link} from 'react-router-dom';
import { ProductConsumer } from '../context';

export default class PlayGround extends Component {
    render() {
        return (
            <ProductConsumer>
                {(value) => {
                    return (
                        <div style={{padding: '4rem'}}>
                            <div style={{border: '0.07rem solid red'}}>
                                Going to open modal
                                <button onClick={() => {value.toggleModal()}}>Open modal</button>
                                <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12" style={{padding: '1.5rem'}}>
                                    <label>Choose Widget</label>
                                    <div className="row">
                                        <div className="col-lg-2 col-md-2 col-sm-2 col-xs-2 wid-select-div1">Types of widgets</div>
                                        <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div1">Widget list with icon and name - will have widget search bar also</div>
                                        <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div2">Preview of widget</div>
                                    </div>
                                    {/* <button className="pull-right" onClick={() => {value.toggleModal()}}>Cancel</button> */}
                                </div>
                            </div>
                        </div>                                
                    )
                }}
            </ProductConsumer>
        )
    }
}