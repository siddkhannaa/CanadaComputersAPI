import React from 'react';
import { useLocation } from "react-router-dom";


import Search from '../components/Search.js'
import List from '../components/List.js'
import '../App.css'

const Home = () => {
  var search_string = new URLSearchParams(useLocation().search).get("query");
return(
    <>
      <div class="header" >
        <h1>Canada Computers Unofficial API</h1>
      </div>

      <div class="search">
        <Search />
        
      </div>

      <div class="list" >
        <h3>list of things</h3>
        <List query={search_string} />
      </div>
    </>
    );
}
export default Home;