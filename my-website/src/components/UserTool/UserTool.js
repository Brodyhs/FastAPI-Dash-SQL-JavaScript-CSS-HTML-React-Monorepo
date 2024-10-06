import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserTool() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState('');
  const [age, setAge] = useState('');

  // Fetch all users from the backend API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/users')
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
      });
  }, []);

  // Handle adding a new user
  const addUser = () => {
    if (name && age) {
      axios.post('http://127.0.0.1:8000/users', { name, age: parseInt(age) })
        .then(() => {
          setUsers([...users, { name, age: parseInt(age) }]);
          setName('');
          setAge('');
        })
        .catch(error => {
          console.error('Error adding user:', error);
        });
    }
  };

  return (
    <div>
      <h1>User Management</h1>
      <div>
        <input 
          type="text" 
          placeholder="Name" 
          value={name} 
          onChange={(e) => setName(e.target.value)} 
        />
        <input 
          type="number" 
          placeholder="Age" 
          value={age} 
          onChange={(e) => setAge(e.target.value)} 
        />
        <button onClick={addUser}>Add User</button>
      </div>
      <h2>All Users</h2>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user.name} - Age: {user.age}</li>
        ))}
      </ul>
    </div>
  );
}

export default UserTool;