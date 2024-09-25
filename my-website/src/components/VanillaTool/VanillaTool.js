import React from 'react';

function VanillaTool() {
  return (
    <div style={{ width: '100%', height: '100vh', border: 'none' }}>
      <iframe
        title="Vanilla Tool"
        src="/vanilla-tool/index.html"
        style={{ width: '100%', height: '100%', border: 'none' }}
      />
    </div>
  );
}

export default VanillaTool;
