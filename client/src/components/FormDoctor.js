import React, { useState } from 'react';
import axios from 'axios';

function FormDoctor() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    departmentID: '',
    schedule: '',
  });

  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

try {
  const response = await axios.post('/doctors', formData);

  if (response.status === 201) {
    setMessage('Doctor created successfully');
    // Clear the form
    setFormData({
      name: '',
      email: '',
      departmentID: '',
      schedule: '',
    });
  }
} catch (err) {
  if (err.response) {
    setError(err.response.data.error);
  } else {
    setError('An error occurred while creating the doctor.');
  }
}
  };

  const formStyle = {
    maxWidth: '400px',
    margin: '0 auto',
    padding: '20px',
    backgroundColor: '#f5f5f5',
    border: '1px solid #ccc',
    borderRadius: '5px',
  };

  const inputStyle = {
    width: '100%',
    padding: '10px',
    margin: '5px 0',
    border: '1px solid #ccc',
    borderRadius: '3px',
  };

  return (
    <div style={formStyle}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Create Doctor</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Input Names:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="departmentID">DepartmentID:</label>
          <input
            type="tel"
            id="departmentID"
            name="departmentID"
            value={formData.departmentID}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <div className="form-group">
          <label htmlFor="schedule">Schedule:</label>
          <input
            type="text"
            id="schedule"
            name="schedule"
            value={formData.schedule}
            onChange={handleChange}
            required
            style={inputStyle}
          />
        </div>
        <button type="submit" style={{ width: '100%', backgroundColor: '#007bff', color: '#fff', padding: '10px', border: 'none', borderRadius: '3px' }}>Create Doctor</button>
      </form>
      {message && <p>{message}</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default FormDoctor;