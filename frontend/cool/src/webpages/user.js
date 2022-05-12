import React, { useState, useEffect } from 'react';
const User = () => {//(props) => {
    // var id = props.match.params.id
    var id = 1;
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [meme, setMeme] = useState([]);
    
    useEffect(() => {
        fetch("http://127.0.0.1:5000")
            .then(res => res.json())
            .then(
                (data) => {
                    console.log(data);
                    setMeme(data.meme);
                }//,
                // (error) => {
                //     setIsLoaded(true);
                //     setError(error);
                // }
            )
    })
    // if (error) {
    //     return <div>Error: {error.message}</div>;
    // }
    // if (!isLoaded) {
    //     return <div>Loading...</div>;
    // }  
    
    if (meme) {
        return (
            <div>
                <h1>{meme}</h1>
          </div>
        );
    }
}
export default User;