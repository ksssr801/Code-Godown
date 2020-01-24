import React, { Component } from 'react';
import { widgetList, savedWidgetList } from './data';

const ProductContext = React.createContext(); // Need to read about Context API

class ProductProvider extends Component {
    state = {
        widgets: [],
        savedWidgets: [],
        isOpen: false,
        opacity: 0,
    }
    // Need to read about componentDidMount()
    componentDidMount() {
        this.setWidgetList();
    }

    setWidgetList = () => {
        let tempWidList = [];
        let tempSavedWidList = [];
        widgetList.forEach(item => {
            const singleWidget = {...item};
            tempWidList = [...tempWidList, singleWidget]
        });
        savedWidgetList.forEach(item => {
            const singleWidget = {...item};
            tempSavedWidList = [...tempSavedWidList, singleWidget]
        });
        this.setState(() => {
            return {widgets: tempWidList, savedWidgets: tempSavedWidList};
        })
    }

    saveCurrLayout = (editedLayout) => {
        console.log('editedLayout==>>',editedLayout);
        let tempSavedLayout = [];
        editedLayout.forEach(widget => {
            const singleWidget = {...widget, static:true}
            tempSavedLayout = [...tempSavedLayout, singleWidget]
        });
        this.setState(() => {
            return {savedWidgets: tempSavedLayout};
        })
    }

    editCurrLayout = (savedLayout) => {
        let tempEditLayout = [];
        savedLayout.forEach(widget => {
            const singleWidget = {...widget, static:false}
            tempEditLayout = [...tempEditLayout, singleWidget]
        });
        this.setState(() => {
            return {widgets: tempEditLayout};
        })
    }

    toggleModal = () => {
        this.setState(() => {
            return {isOpen: !this.state.isOpen};
        });
    }
    
    afterOpen = () => {
        setTimeout(() => {
          this.setState({ opacity: 1 });
        });
    }
    
    beforeClose = () => {
        return new Promise(resolve => {
          this.setState({ opacity: 0 });
          setTimeout(resolve, 200);
        });
    }
    
    render(){
        return (
            <ProductContext.Provider value={{
                ...this.state,
                saveCurrLayout: this.saveCurrLayout,
                editCurrLayout: this.editCurrLayout,
                toggleModal: this.toggleModal,
                // afterOpen: this.afterOpen,
                // beforeClose: this.beforeClose,
            }}>
                {this.props.children}
            </ProductContext.Provider>
        )
    }
}

const ProductConsumer = ProductContext.Consumer;

export {ProductProvider,ProductConsumer};
