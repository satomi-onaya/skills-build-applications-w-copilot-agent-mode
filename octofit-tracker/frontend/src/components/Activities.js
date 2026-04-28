import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const codespaceBase = process.env.REACT_APP_CODESPACE_NAME || 'localhost:8000';
        const apiUrl = codespaceBase.includes('http')
          ? `${codespaceBase}/api/activities/`
          : `https://${codespaceBase}-8000.app.github.dev/api/activities/`;

        console.log('API URL:', apiUrl);

        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Fetched Activities Data:', data);

        // Handle both paginated and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching activities:', error);
        setError(error.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="loading">Loading activities...</div>;
  if (error) return <div className="error">Error: {error}</div>;

  return (
    <div className="table-container">
      <h2>Activities</h2>
      <table className="data-table table table-striped table-hover">
        <thead>
          <tr>
            <th>User</th>
            <th>Activity Type</th>
            <th>Duration (min)</th>
            <th>Calories Burned</th>
          </tr>
        </thead>
        <tbody>
          {activities.length > 0 ? (
            activities.map((activity, index) => (
              <tr key={index}>
                <td>{activity.user?.name || activity.user || 'N/A'}</td>
                <td>
                  <span className="badge bg-info">{activity.activity_type}</span>
                </td>
                <td>{activity.duration_minutes}</td>
                <td>
                  <span className="badge bg-success">{activity.calories_burned}</span>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" className="text-center">
                No activities found
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
