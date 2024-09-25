import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home/Home';
import EmptyLocations from './components/EmptyLocations/EmptyLocations';
import VanillaTool from './components/VanillaTool/VanillaTool';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/empty-locations" element={<EmptyLocations />} />
        <Route path="/vanilla-tool" element={<VanillaTool />} />  {/* Vanilla JS tool */}
      </Routes>
    </Router>
  );
}

export default App;
