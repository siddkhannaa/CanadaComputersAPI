import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import List from '../components/List';

const User = () => {
    let { id } = useParams();

    return <List />
}

export default User;