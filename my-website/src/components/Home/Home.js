import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <h1>Welcome to the Warehouse Manager</h1>
      <p>Click a button below to navigate.</p>
      
      {/* Link to Empty Locations */}
      <Link to="/empty-locations">
        <button className="btn">Go to Empty Locations</button>
      </Link>
      
      {/* Link to Vanilla Tool */}
      <Link to="/vanilla-tool">
        <button className="btn">Go to Vanilla Tool</button>
      </Link>
      
      {/* Direct link to the Dash tool (outside of React Router) */}
      <a href="http://127.0.0.1:8000/dash-tool">
        <button className="btn">Go to Dash Tool</button>
      </a>
      
      {/* Link to User Tool */}
      <Link to="/user-tool">
        <button className="btn">Go to User Tool</button>
      </Link>
    </div>
  );
}

export default Home;
