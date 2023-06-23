"use client";
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from "react-router-dom";

import Sidebar from "../../GlobalFiles/Sidebar";
import "react-toastify/dist/ReactToastify.css";
import { toast, ToastContainer } from "react-toastify";
import "./CSS/Faculty_Profile.css"
import { University, Admin } from "../backend";
import { admin } from "../../../Dashboard-Login/DLogin";



const notify = (text) => toast(text);



const Add_Course = () => {


  const [loading, setLoading] = useState(false);
  const [AddedCourses, setAddedC] =useState(University.courses);

  const dispatch = useDispatch();


  const InitData = {
    courseName: "",
    courseCredit:"",
    courseDepartment:"",
    courseDetails:"",
    courseInitial:""
  };
  const OfferCourse = ()=>{};
  const [ReportValue, setReportValue] = useState(InitData);

  const HandleReportChange = (e) => {
    setReportValue({ ...ReportValue, [e.target.name]: e.target.value });
  };

 

  const HandleReportSubmit = (e) => {
    //e.preventDefault();
    let data = {
      ...ReportValue,
    };
    try {
      setLoading(true);
  
     admin.createCourse(data.courseName, data.courseCredit);
     setAddedC(University.courses);
     notify("Course Created Sucessfully");
          setLoading(false);
          setReportValue(InitData);
    } catch (error) {
      console.log(error);
    }
  };

  console.log(AddedCourses);
  return (
    <>
      <ToastContainer />
      <div className="container">
      <Sidebar userType="admin"/>
        <div className="AfterSideBar">
          <div className="Main_Add_Doctor_div">
            <h1>Add Course</h1>
            <form>
              <div>
                <label>Course Name</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="Course Name"
                    name="courseName"
                    value={ReportValue.courseName}
                    onChange={HandleReportChange}
                    required
                  />
                </div>
              </div>
                       
              <div>
                <label>Course Initial</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="Initial"
                    name="courseInitial"
                    value={ReportValue.courseInitial}
                    onChange={HandleReportChange}
                    required
                  />
                </div>
              </div>
              <div>
                <label>Course Credit</label>
                <div className="inputdiv">
                  <input
                    type="number"
                    placeholder="Credit"
                    name="courseCredit"
                    value={ReportValue.courseCredit}
                    onChange={HandleReportChange}
                    required
                  />
                </div>
              </div>
              <div>
                <label>Course Details</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="Details"
                    name="courseDetails"
                    value={ReportValue.courseDetails}
                    onChange={HandleReportChange}
                    required
                  />
                </div>
              </div>
             
              <div>
                <label>Department</label>
                <div className="inputdiv">
                  <select
                    name="courseDepartment"
                    value={ReportValue.courseDepartment}
                    onChange={HandleReportChange}
                  >
                    <option value="Choose Dept">Choose Department</option>
                    <option value="CSE">CSE</option>
                    <option value="EEE">EEE</option>
                    <option value="Archi">Archi</option>
                  </select>
                </div>
              </div>
             
            </form>
            <div className="rightside2">
            <button type="submit" onClick={HandleReportSubmit}>{loading ? "Loading..." : "ADD"}</button>
            </div>
            <div className="Payment_Page">
            <h1 style={{ marginBottom: "2rem" }}>Added Courses</h1>
            <div className="patientBox">
              <table>
                <thead>
                  <tr>
                    <th>Course Name</th>
                    <th>Course Credit</th>
                    <th>Resolve</th>
                  </tr>
                </thead>
                <tbody>
                  {AddedCourses?.map((ele) => {
                    return (
                      <tr onClick={""}>
                        <td>{ele.name}</td>
                        <td>{ele.credit}</td>
                        <td>
                          <button
                            style={{
                              border: "none",
                              color: "red",
                              outline: "none",
                              background: "transparent",
                              cursor: "pointer",
                            }}
                            onClick={() => OfferCourse(ele.courseInitial)}
                          >
                            Offer
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Add_Course;
