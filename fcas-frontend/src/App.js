import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [courses, setCourses] = useState([]);
  const [faculties, setFaculties] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [newCourse, setNewCourse] = useState({
    title: '',
    facultyId: '',
  });

  useEffect(() => {
    fetchCourses();
    fetchFaculties();
  }, []);

  const fetchCourses = async () => {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
      setCourses(response.data);
    } catch (error) {
      console.error('Error fetching courses:', error);
    }
  };

  const fetchFaculties = async () => {
    try {
      const response = await axios.get('https://jsonplaceholder.typicode.com/users');
      setFaculties(response.data);
    } catch (error) {
      console.error('Error fetching faculties:', error);
    }
  };

  const addCourse = async () => {
    try {
      const response = await axios.post('https://jsonplaceholder.typicode.com/posts', newCourse);
      setCourses([...courses, response.data]);
      setNewCourse({ title: '', facultyId: '' });
    } catch (error) {
      console.error('Error adding course:', error);
    }
  };

  const deleteCourse = async (courseId) => {
    try {
      await axios.delete(`https://jsonplaceholder.typicode.com/posts/${courseId}`);
      setCourses(courses.filter((course) => course.id !== courseId));
    } catch (error) {
      console.error('Error deleting course:', error);
    }
  };

  const editCourse = async (courseId) => {
    try {
      const response = await axios.put(
        `https://jsonplaceholder.typicode.com/posts/${courseId}`,
        selectedCourse
      );
      const updatedCourses = courses.map((course) =>
        course.id === courseId ? response.data : course
      );
      setCourses(updatedCourses);
      setSelectedCourse(null);
    } catch (error) {
      console.error('Error editing course:', error);
    }
  };

  const assignCourse = async (courseId, facultyId) => {
    try {
      const response = await axios.put(`https://jsonplaceholder.typicode.com/posts/${courseId}`, {
        ...selectedCourse,
        facultyId,
      });
      const updatedCourses = courses.map((course) =>
        course.id === courseId ? response.data : course
      );
      setCourses(updatedCourses);
    } catch (error) {
      console.error('Error assigning course:', error);
    }
  };

  const handleCourseInputChange = (e) => {
    setNewCourse({ ...newCourse, [e.target.name]: e.target.value });
  };

  const handleCourseEditChange = (e) => {
    setSelectedCourse({ ...selectedCourse, [e.target.name]: e.target.value });
  };

  const selectCourseForEdit = (course) => {
    setSelectedCourse(course);
  };

  return (
    <div className="container">
      <h1 className="mt-4">Course Management</h1>

      <div className="card my-4">
        <div className="card-body">
          <h2>Add Course</h2>
          <div className="form-group">
            <input
              type="text"
              name="title"
              value={newCourse.title}
              className="form-control"
              placeholder="Course Title"
              onChange={handleCourseInputChange}
            />
          </div>
          <div className="form-group">
            <select
              name="facultyId"
              value={newCourse.facultyId}
              className="form-control"
              onChange={handleCourseInputChange}
            >
              <option value="">Assign Faculty</option>
              {faculties.map((faculty) => (
                <option key={faculty.id} value={faculty.id}>
                  {faculty.name}
                </option>
              ))}
            </select>
          </div>
          <button className="btn btn-primary" onClick={addCourse}>Add</button>
        </div>
      </div>

      <div className="card my-4">
        <div className="card-body">
          <h2>Edit Course</h2>
          {selectedCourse && (
            <div className="form-group">
              <input
                type="text"
                name="title"
                value={selectedCourse.title}
                className="form-control"
                placeholder="Course Title"
                onChange={handleCourseEditChange}
              />
              <button className="btn btn-primary mt-2" onClick={() => editCourse(selectedCourse.id)}>Save</button>
            </div>
          )}
        </div>
      </div>

      <div className="card">
        <div className="card-body">
          <h2>Courses</h2>
          <ul className="list-group">
            {courses.map((course) => (
              <li key={course.id} className="list-group-item d-flex justify-content-between align-items-center">
                <span>{course.title} - Faculty: {course.facultyId ? course.facultyId : 'Not assigned'}</span>
                <div>
                  <button className="btn btn-primary mr-2" onClick={() => selectCourseForEdit(course)}>Edit</button>
                  <button className="btn btn-danger" onClick={() => deleteCourse(course.id)}>Delete</button>
                  <select
                    value={course.facultyId}
                    className="form-control mt-2"
                    onChange={(e) => assignCourse(course.id, e.target.value)}
                  >
                    <option value="">Assign Faculty</option>
                    {faculties.map((faculty) => (
                      <option key={faculty.id} value={faculty.id}>
                        {faculty.name}
                      </option>
                    ))}
                  </select>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;
