// // search using searchbar then post request api with the search_string
// // return the json that the api spits out of the first 12 items
import React, { setIsLoaded } from 'react';
import Table from 'react-bootstrap/Table';
import '../App.css'

class List extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            results: []
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:5000/search/" + this.props.query)
            .then(res => res.json())
            .then(
                (data) => {
                    console.log(data);
                    this.setState({
                        isLoaded: true,
                        results: data.products
                    });
                }
        )
    }
    
    render() {
        const { error, isLoaded, results } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <>
            
            <table>
                <thead>
                    <tr>
                        <th>Product Name</th>
                        <th>Price</th>
                        <th>Item Code</th>
                        <th>Availability</th>
                    </tr>
                </thead>

                <tbody>

                    <td>
                        {results.map(result => (
                            <tr>{result.title}</tr>
                        ))}
                    </td>
                    
                    <td>
                        {results.map(result => (
                            <tr>{result.price}</tr>
                        ))}
                    </td>

                    <td>
                        {results.map(result => (
                            <tr>{result.item_code}</tr>
                        ))}

                        
                    </td>
                    <td>
                        {results.map(result => (
                            <tr>{result.availability}</tr>
                        ))}
                    </td>
                </tbody>
            </table>
            </>
            );
        }
    }
}

export default List;