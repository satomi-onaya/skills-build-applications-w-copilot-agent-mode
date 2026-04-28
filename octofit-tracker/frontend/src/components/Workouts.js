import React, { useState, useEffect } from 'react';

const CODESPACE_NAME = process.env.REACT_APP_CODESPACE_NAME || 'localhost';
const API_URL = `https://${CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    console.log('Fetching workouts from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        console.log('Workouts data:', data);
        setWorkouts(data.results || data);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-3">Workouts</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Difficulty</th>
            <th>Duration (min)</th>
            <th>Target Muscle Groups</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, i) => (
            <tr key={i}>
              <td>{workout.name}</td>
              <td>{workout.difficulty}</td>
              <td>{workout.duration_minutes}</td>
              <td>{workout.target_muscle_groups}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;