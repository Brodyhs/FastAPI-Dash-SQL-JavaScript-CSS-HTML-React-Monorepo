import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home/Home';
import EmptyLocations from './components/EmptyLocations/EmptyLocations';
import VanillaTool from './components/VanillaTool/VanillaTool';
import UserTool from './components/UserTool/UserTool';  // Import the UserTool component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/empty-locations" element={<EmptyLocations />} />
        <Route path="/vanilla-tool" element={<VanillaTool />} />  {/* Vanilla JS tool */}
        <Route path="/user-tool" element={<UserTool />} />  {/* Add route for UserTool */}
      </Routes>
    </Router>
  );
}

export default App;