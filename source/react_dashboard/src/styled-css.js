import styled from 'styled-components';
import Modal, { BaseModalBackground } from 'styled-react-modal';


export const BtnContainer = styled.button`
text-transform:capitalize;
font-size:1.4rem;
background: transparent;
border:0.04rem solid var(--lightBlue);
border-color: ${props => 
    props.cart ? "var(--mainYellow)" : 
    props.backToProd ? "var(--lightBlue)" : 
    props.clearCart ? "var(--mainRed)" : "var(--lightBlue)"};
color: ${props => 
    props.cart ? "var(--mainYellow)" : 
    props.backToProd ? "var(--lightBlue)" : 
    props.clearCart ? "var(--mainRed)" : "var(--lightBlue)"};
border-radius: 0.5rem;
padding: 0.2rem 0.5rem;
cursor: pointer;
margin: 0.2rem 0.5rem 0.2rem 0.5rem;
transition: all 0.5s ease-in-out;
&:hover{
    background: ${props => 
        props.cart ? "var(--mainYellow)" : 
        props.backToProd ? "var(--lightBlue)" : 
        props.clearCart ? "var(--mainRed)" : "var(--mainWhite)"};
    color: darkgreen;
    color: ${props => 
        props.cart ? "var(--mainDark)" : 
        props.backToProd ? "var(--mainBlue)" : 
        props.clearCart ? "var(--mainWhite)" : "darkgreen"};
}
&:focus{
    outline: none;
}
`;

export const NavWrapper = styled.nav`
background: #4f7d9b;
.nav-link{
    color: var(--mainWhite) !important;
    font-size: 1.3rem;
    text-transform:capitalize;
}
`;

export const ProductWrapper = styled.div`
.card{
    border-color: transparent;
    transition: all 0.5s linear;
}
.card-footer{
    background: transparent;
    border-top: transparent;
    transition: all 0.5s linear;
}
&:hover{
    .card{
        border:0.04rem solid rgba(0,0,0,0.2);
        box-shadow: 2px 2px 5px 0px rgba(0,0,0,0.02);
    }
    .card-footer{
        background: rgba(247, 247, 247);
    }
}
.img-container{
    position:relative;
    overflow:hidden;
}
.card-img-top{
    transition: all 0.5s linear
}
.img-container:hover .card-img-top{
    transform: scale(1.1);
}
.cart-btn{
    position: absolute;
    bottom: 0;
    right: 0;
    padding: 0.2rem 0.4rem;
    background: var(--lightBlue);
    border: none;
    color: var(--mainWhite);
    font-size: 1.4rem;
    border-radius: 0.5rem 0 0 0;
    transform: translate(100%,100%);
    transition: all 0.7s linear;
}
.img-container:hover .cart-btn{
    transform: translate(0,0);
}
.cart-btn:hover{
    color: var(--mainBlue);
    cursor: pointer;
}
`;

export const ModalContainer = styled.div`
width: 100%;
height: 100%;
position: fixed;
background: rgba(0,0,0,0.3);
top: 0%;
bottom: 0%;
left: 0%;
right: 0%;
display: flex;
align-items: center;
justify-content: center;
`;

export const PopUpDialogBox = styled.div`
width: 20rem;
height: 20rem;
display: flex;
align-items: center;
justify-content: center;
background-color: red;
opacity: 0;
transition: opacity ease 500ms;
`;

export const FadingBackground = styled(BaseModalBackground)`
  opacity: 0;
  transition: opacity ease 200ms;
`;
