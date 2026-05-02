import { useEffect, useState } from "react";

function App() {
  const [signals, setSignals] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/signals")
      .then(res => res.json())
      .then(data => {
        console.log("API DATA:", data);
        setSignals(data);
      })
      .catch(err => console.error("FETCH ERROR:", err));
  }, []);

  return (
    <div>
      <h1>Signals</h1>

      {signals.length === 0 ? (
        <p>No data</p>
      ) : (
        signals.map((s, i) => (
          <div key={i}>
            {s.service} - {s.status}
          </div>
        ))
      )}
    </div>
  );
}

export default App;
