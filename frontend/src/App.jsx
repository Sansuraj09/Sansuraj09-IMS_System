import { useEffect, useState } from "react";

function App() {
  const [signals, setSignals] = useState([]);
  const [error, setError] = useState(null); // Added to track errors

  useEffect(() => {
    fetch("http://15.206.149.43:8000/signals")
      .then(res => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then(data => {
        console.log("API DATA:", data);
        // Ensure we only set an array to state
        if (Array.isArray(data)) {
          setSignals(data);
        } else if (data && Array.isArray(data.signals)) {
          // Just in case your API wraps it like { signals: [...] }
          setSignals(data.signals);
        } else {
          throw new Error("API did not return an array");
        }
      })
      .catch(err => {
        console.error("FETCH ERROR:", err);
        setError(err.message);
      });
  }, []);

  return (
    <div>
      <h1>Signals</h1>
      
      {/* Display fetch errors if they occur */}
      {error && <p style={{color: 'red'}}>Error loading signals: {error}</p>}

      {/* Safely check if signals is an array and has length */}
      {!error && (!Array.isArray(signals) || signals.length === 0) ? (
        <p>No data</p>
      ) : (
        // Optional chaining (?.) as an extra safety net
        signals?.map((s, i) => (
          <div key={i}>
            {s.service} - {s.status}
          </div>
        ))
      )}
    </div>
  );
}

export default App;
