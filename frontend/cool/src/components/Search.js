import React, { Component } from 'react';
import  { Redirect } from 'react-router'
import '../App.css';

class Search extends Component {

    render() {
        return (
            <form>
                <input type="text" name="query" palceholder="Search.." />
                <button type="submit">Search</button>
            </form>
        );
    }
}

export default Search;