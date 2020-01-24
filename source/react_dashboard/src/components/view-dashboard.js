import React, { Component } from 'react';
import ReactGridLayout from 'react-grid-layout';
import { BtnContainer } from '../styled-css';
import {Link} from 'react-router-dom';
import { ProductConsumer } from '../context';

export default class ViewDashboard extends Component {
    render() {
        return (
            <ProductConsumer>
                {(value) => {
                    var styleDict = {
                        'widget1' : {border: '0.1rem solid #dbd6d6', backgroundColor: 'red'},
                        'widget2' : {border: '0.1rem solid #dbd6d6', backgroundColor: 'blue'},
                        'widget3' : {border: '0.1rem solid #dbd6d6', backgroundColor: 'green'},
                    };
                    console.log('styleDict[widget]==>>',styleDict['widget1'])
                    var savedLayout = value.savedWidgets;
                    return(
                        <div>
                            <nav className="navbar navbar-expand-sm store-nav navbar-dark px-sm-5" style={{border: '0.1rem solid #dbd6d6'}}>
                                <Link to="/edit" className="ml-auto" title="Edit">
                                    <BtnContainer backToProd onClick={() => {value.editCurrLayout(savedLayout)}}><i className="fa fa-edit fa-1x"/>&nbsp;&nbsp;Edit</BtnContainer>
                                </Link>
                            </nav>                
                            <ReactGridLayout 
                                className="layout" 
                                layout={savedLayout} 
                                cols={12} 
                                rowHeight={100} 
                                width={1500} >
                                    {savedLayout.map(widget => {
                                        console.log('styleDict[widget]==>>',styleDict.widget)
                                        return <div style={{border: '0.1rem solid #dbd6d6', backgroundColor: 'yellow'}} key={widget.i}>
                                                    <center>
                                                        <table>
                                                            <tr>
                                                                <td>a</td>
                                                                <td>b</td>
                                                            </tr>
                                                            <tr>
                                                                <td>x</td>
                                                                <td>y</td>
                                                            </tr>
                                                        </table>
                                                        {widget.i}
                                                    </center>
                                                </div>
                                    })}
                            </ReactGridLayout>
                        </div>
                    )
                }}
            </ProductConsumer>
        )
    }
}