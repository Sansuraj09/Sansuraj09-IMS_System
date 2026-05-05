import { useState, useEffect } from 'react';
import './App.css'; // Make sure you have some basic CSS here

function App() {
  const [incidents, setIncidents] = useState([]);
  const [loading, setLoading] = useState(true);

  // Poll the backend every 5 seconds for live data
  useEffect(() => {
    const fetchIncidents = async () => {
      try {
        // Replace with your actual FastAPI endpoint
        const response = await fetch('http://13.203.160.157:8000/work-items'); 
        if (response.ok) {
          const data = await response.json();
          // Sort P0 -> P1 -> P2 etc.
          const sortedData = data.sort((a, b) => a.severity.localeCompare(b.severity));
          setIncidents(sortedData);
        }
      } catch (error) {
        console.error("Failed to fetch incidents from API:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchIncidents(); // Initial fetch
    const intervalId = setInterval(fetchIncidents, 5000); // Poll every 5s
    
    return () => clearInterval(intervalId); // Cleanup
  }, []);

  if (loading) return <h2>Loading Incident Dashboard...</h2>;

  return (
    <div className="App">
      <header>
        <h1>Mission-Critical IMS Dashboard</h1>
      </header>
      
      <main>
        <h2>Active Incidents Feed</h2>
        <div className="incident-grid">
          {incidents.length === 0 ? (
            <p>No active incidents. Systems are green.</p>
          ) : (
            incidents.map(incident => (
              <div key={incident.id} className={`incident-card ${incident.severity}`}>
                <div className="card-header">
                  <span className="severity-badge">{incident.severity}</span>
                  <h3>{incident.component_id}</h3>
                </div>
                <div className="card-body">
                  <p><strong>Status:</strong> {incident.status}</p>
                  <p><strong>Started:</strong> {new Date(incident.start_time).toLocaleTimeString()}</p>
                </div>
                <button onClick={() => alert(`Open RCA form for ${incident.id}`)}>
                  View / Manage RCA
                </button>
              </div>
            ))
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
