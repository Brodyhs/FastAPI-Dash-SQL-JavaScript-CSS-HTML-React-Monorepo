import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './EmptyLocations.css';

function EmptyLocations() {
  const [locations, setLocations] = useState([]);
  const [allLocations, setAllLocations] = useState([]);
  const [newLocation, setNewLocation] = useState({ location_id: "", status: "empty" });

  // Fetch all locations
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/all-locations')
      .then(response => {
        console.log('All Locations:', response.data);  // Debugging
        setAllLocations(response.data);
      })
      .catch(error => {
        console.error('Error fetching all locations:', error);
      });

    axios.get('http://127.0.0.1:8000/empty-locations')
      .then(response => {
        console.log('Empty Locations:', response.data);  // Debugging
        setLocations(response.data);
      })
      .catch(error => {
        console.error('Error fetching empty locations:', error);
      });
  }, []);

  // Add new location
  const addLocation = () => {
    if (newLocation.location_id === "") {
      alert("Location ID cannot be empty.");
      return;
    }
    axios.post('http://127.0.0.1:8000/empty-locations', newLocation)
      .then(() => {
        setAllLocations([...allLocations, newLocation]);
        if (newLocation.status === 'empty') {
          setLocations([...locations, newLocation]);
        }
        setNewLocation({ location_id: "", status: "empty" });
      })
      .catch(error => {
        console.error('Error adding new location:', error);
      });
  };

  // Delete location
  const deleteLocation = (location_id) => {
    axios.delete(`http://127.0.0.1:8000/empty-locations/${location_id}`)
      .then(() => {
        setAllLocations(allLocations.filter(loc => loc.location_id !== location_id));
        setLocations(locations.filter(loc => loc.location_id !== location_id));
      })
      .catch(error => {
        console.error('Error deleting location:', error);
      });
  };

  // Update location status
  const updateLocation = (location_id, status) => {
    axios.put(`http://127.0.0.1:8000/empty-locations/${location_id}`, { location_id, status })
      .then(() => {
        setAllLocations(allLocations.map(loc => 
          loc.location_id === location_id ? { ...loc, status } : loc));
        if (status === "empty") {
          setLocations([...locations, { location_id, status }]);
        } else {
          setLocations(locations.filter(loc => loc.location_id !== location_id));
        }
      })
      .catch(error => {
        console.error('Error updating location status:', error);
      });
  };

  return (
    <div className="container">
      <h1>Location Manager</h1>
      <div className="add-location">
        <input
          type="text"
          placeholder="Location ID"
          value={newLocation.location_id}
          onChange={(e) => setNewLocation({ ...newLocation, location_id: e.target.value })}
        />
        <select
          value={newLocation.status}
          onChange={(e) => setNewLocation({ ...newLocation, status: e.target.value })}
        >
          <option value="empty">Empty</option>
          <option value="occupied">Occupied</option>
        </select>
        <button onClick={addLocation}>Add Location</button>
      </div>
      <h2>All Locations</h2>
      <table>
        <thead>
          <tr>
            <th>Location ID</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {allLocations.map((location, index) => (
            <tr key={index}>
              <td>{location.location_id}</td>
              <td>{location.status}</td>
              <td>
                <button onClick={() => updateLocation(location.location_id, location.status === 'empty' ? 'occupied' : 'empty')}>
                  {location.status === 'empty' ? 'Occupy' : 'Empty'}
                </button>
                <button onClick={() => deleteLocation(location.location_id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Empty Locations</h2>
      <ul>
        {locations.map((location, index) => (
          <li key={index}>{location.location_id}</li>
        ))}
      </ul>
    </div>
  );
}

export default EmptyLocations;
