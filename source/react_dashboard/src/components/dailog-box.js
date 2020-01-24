import React, { Component } from 'react';
import { ProductConsumer } from '../context';
import { PopUpDialogBox, ModalContainer } from '../styled-css';
import './dialog-box.css';

export default class StyledDailogBox extends Component {
    render() {
        return (
            <ProductConsumer>
                {(value) => {
                    const {isOpen, toggleModal, opacity} = value;
                    console.log('isOpen, toggleModal, opacity==>>',isOpen, toggleModal, opacity)
                    if (!isOpen){
                        return null;
                    }
                    else {
                        return (
                            <ModalContainer>
                                <center>
                                    <div style={{backgroundColor: 'white', height: '33rem', width: '70rem'}}>
                                        <div style={{border: '0.1rem solid lightblue', height: '33rem', width: '70rem', overflow:'scroll'}}>
                                            <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                                                <label>Choose Widget</label>
                                                <button onClick={() => {value.toggleModal()}}>Cancel</button>
                                                <div className="row">
                                                    <div className="col-lg-2 col-md-2 col-sm-2 col-xs-2 wid-select-div1">Types of widgets</div>
                                                    <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div1">Widget list with icon and name - will have widget search bar also</div>
                                                    <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div2">Preview of widget</div>
                                                </div>
                                                {/* <button className="pull-right" onClick={() => {value.toggleModal()}}>Cancel</button> */}
                                            </div>
                                        </div>
                                    </div>
                                </center>
                                {/* <div style={{padding: '4rem'}}>
                                    <div style={{border: '0.07rem solid red'}}> */}
                                        {/* Going to open modal
                                        <button onClick={() => {value.toggleModal()}}>Open modal</button> */}
                                        {/* <div className="col-lg-12 col-md-12 col-sm-12 col-xs-12" style={{padding: '1.5rem', height: '80%', width: '85%'}}>
                                            <label>Choose Widget</label>
                                            <div className="row">
                                                <div className="col-lg-2 col-md-2 col-sm-2 col-xs-2 wid-select-div1">Types of widgets</div>
                                                <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div1">Widget list with icon and name - will have widget search bar also</div>
                                                <div className="col-lg-5 col-md-5 col-sm-5 col-xs-5 wid-select-div2">Preview of widget</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>                                 */}
                                {/* isOpen={isOpen}
                                afterOpen={() => {afterOpen()}}
                                beforeClose={() => {beforeClose()}}
                                onBackgroundClick={() => {toggleModal()}}
                                onEscapeKeydown={() => {toggleModal()}}
                                opacity={opacity}> */}
                                {/* <div className="col-lg-10 col-md-10 col-sm-10 col-xs-10" style={{padding: '1.5rem'}}>
                                    <div className="row">
                                        <span>
                                            <label>Choose Widget</label>
                                            <button onClick={() => {toggleModal()}}>Close me</button>
                                        </span>
                                        <div className="col-lg-2 col-md-2 col-sm-2 col-xs-2 wid-select-div1">Types of widgets</div>
                                        <div className="col-lg-4 col-md-4 col-sm-4 col-xs-4 wid-select-div1">Widget list with icon and name - will have widget search bar also</div>
                                        <div className="col-lg-4 col-md-4 col-sm-4 col-xs-4 wid-select-div2">Preview of widget</div>
                                    </div>
                                </div> */}
                                    {/* <span>I am a modal!</span> */}
                            </ModalContainer>
                        )
                    }
                }}
            </ProductConsumer>
        )
    }
}

// constructor(props) {
//     super(props);

//     this.state = {
//       isOpen: false,
//       opacity: 0
//     };

//     this.toggleModal = this.toggleModal.bind(this);
//     this.afterOpen = this.afterOpen.bind(this);
//     this.beforeClose = this.beforeClose.bind(this);
//   }

//   toggleModal(e) {
//     this.setState({ isOpen: !this.state.isOpen });
//   }

//   afterOpen() {
//     setTimeout(() => {
//       this.setState({ opacity: 1 });
//     });
//   }

//   beforeClose() {
//     return new Promise(resolve => {
//       this.setState({ opacity: 0 });
//       setTimeout(resolve, 200);
//     });
//   }

//   render() {
//     return (
//       <div>
//         <button onClick={this.toggleModal}>Open modal</button>
//         <StyledModal
//           isOpen={this.state.isOpen}
//           afterOpen={this.afterOpen}
//           beforeClose={this.beforeClose}
//           onBackgroundClick={this.toggleModal}
//           onEscapeKeydown={this.toggleModal}
//           opacity={this.state.opacity}
//           backgroundProps={{ opacity: this.state.opacity }}
//         >
//           <span>I am a modal!</span>
//           <button onClick={this.toggleModal}>Close me</button>
//         </StyledModal>
//       </div>
//     );
//   }
// }

// function App() {
//   return (
//     <ModalProvider backgroundComponent={FadingBackground}>
//       <div className="App">
//         <h1>Hello styled-react-modal</h1>
//         <h2>Start editing to see some magic happen!</h2>
//         <FancyModalButton />
//       </div>
//     </ModalProvider>
//   );
// }

// const rootElement = document.getElementById("root");
// ReactDOM.render(<App />, rootElement);
