"use client";
import { Table } from "antd";
import { useEffect, useState } from "react";
import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import './CSS/Faculty_Profile.css'

import Sidebar from "../../GlobalFiles/Sidebar";
import { University } from "../backend";
import { faculty } from "../../../Dashboard-Login/DLogin";

const Offered_Courses = () => {
  const { data } = useSelector((store) => store.auth);
  //const id = data.user.ID;
  const disptach = useDispatch();
  const navigate = useNavigate();
  const columns = [
    { title: "Course Name", dataIndex: "courseName", key: "courseName" },
    { title: "Course Credit", dataIndex: "courseCredit", key: "courseCredit" },
    { title: "Resolve", dataIndex: "resolve", key: "resolve" },
  ];
  

 const [AllCourses, setApp] = useState([]); 
 const [opened, setop] = useState(true);
 const course = faculty.offerdCourses;
 const courseI = "CSE101";
 const courseN ="Intro to pc";

function toggle() {
  setop(!opened);
}


  const DeleteCrs = (id) => {
 
  };


  return (
    <>
      <div className="container">
        <Sidebar userType="faculty"/>
        <div className="AfterSideBar">
          <div className="Payment_Page">
            <h1 style={{ marginBottom: "1rem", textAlign : "center" }}>Course Panel</h1>
            <div className="patientBox">
              <table>
                <thead>
                  <tr>
                    <th>Course</th>
                    <th>Section</th>
                  </tr>
                </thead>
                <tbody>
                  {course?.map((ele) => {
                    return (
                      <tr style={{}} onClick={()=> toggle()}>
                        
                        <td  className=""><h1 >{ele.course.name}</h1></td>
                        <td><h1>{ele.number}</h1></td>
                        <td><div style={{width : "10%",float: "left"}}><button
                            style={{
                              border: "none",
                              color: "red",
                              outline: "none",
                              background: "transparent",
                              cursor: "pointer",
                            }}
                            onClick={() => DeleteCrs(ele.ID)}
                          >
                           Delete
                          </button></div></td>
                        
                       {/*} <td>
                          <button
                            style={{
                              border: "none",
                              color: "red",
                              outline: "none",
                              background: "transparent",
                              cursor: "pointer",
                            }}
                            onClick={() => DeleteCrs(ele.ID)}
                          >
                           Delete
                          </button>
                        </td>*/}
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Offered_Courses;
