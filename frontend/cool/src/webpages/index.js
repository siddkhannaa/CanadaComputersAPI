import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
//   Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Home from './home';
import User from './user';

const Webpages = () => {
    return(
        <Router>
            <Routes>
                <Route exact path="/" element={<Home />}></Route>
                <Route path="/user/:id" element={<User />}></Route>
            </Routes>
        </Router>
    );
};
export default Webpages;