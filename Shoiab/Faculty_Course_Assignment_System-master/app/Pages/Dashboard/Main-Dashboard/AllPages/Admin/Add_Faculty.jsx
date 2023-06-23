"use client";
import React, { useState } from "react";
import "./CSS/Add_Faculty.css";
import doctor from "../../../../../img/doctoravatar.png";
import { useDispatch, useSelector } from "react-redux";
import Sidebar from "../../GlobalFiles/Sidebar";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Navigate } from "react-router-dom";
import Image from "next/image";
import { admin } from "../../../Dashboard-Login/DLogin";
import { University } from "../backend";
const notify = (text) => toast(text);

const Add_Faculty = () => {
 
  console.log(1);

  const dispatch = useDispatch();

  const [loading, setLoading] = useState(false);

  const initData = {
    id: "",
    name: "",
    address: "",
    gender: "",
    email: "",
    department: "",
    password: "",
  };
  const [FacultyValue, setFacultyValue] = useState(initData);

  const HandleFacultyChange = (e) => {
    setFacultyValue({ ...FacultyValue, [e.target.name]: e.target.value });
  };

  const HandleFacultySubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    admin.addFaculty(FacultyValue); 
    console.log(University.faculties);
    setFacultyValue(initData);
    notify("New faculty added")
    setLoading(false);
  };


  return (
    <>
      <ToastContainer />
      <div className="container">
      <Sidebar userType="admin"/>
        <div className="AfterSideBar">
          <div className="Main_Add_Faculty_div">
            <h1>Add Faculty</h1>
            <Image src={doctor} alt="doctor" className="avatarimg" />
            <form onSubmit={HandleFacultySubmit}>
              <div>
                <label>Faculty Name</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="Full Name"
                    name="name"
                    value={FacultyValue.name}
                    onChange={HandleFacultyChange}
                    required
                  />
                </div>
              </div>
            
          
              <div>
                <label>Email</label>
                <div className="inputdiv">
                  <input
                    type="email"
                    placeholder="abc@abc.com"
                    name="email"
                    value={FacultyValue.email}
                    onChange={HandleFacultyChange}
                    required
                  />
                </div>
              </div>
              <div>
                <label>Gender</label>
                <div className="inputdiv">
                  <select
                    name="gender"
                    value={FacultyValue.gender}
                    onChange={HandleFacultyChange}
                    required
                  >
                    <option value="Choose Gender">Choose Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Others">Others</option>
                  </select>
                </div>
              </div>
             
              <div>
                <label>Address</label>
                <div className="inputdiv adressdiv">
                  <input
                    type="text"
                    placeholder="Address"
                    name="address"
                    value={FacultyValue.address}
                    onChange={HandleFacultyChange}
                    required
                  />
                </div>
              </div>
              
              
              <div>
                <label>Department</label>
                <div className="inputdiv">
                  <select
                    name="department"
                    value={FacultyValue.department}
                    onChange={HandleFacultyChange}
                    required
                  >
                    <option value="General">Select</option>
                    <option value="CSE">CSE</option>
                    <option value="EEE">EEE</option>
                    <option value="ETE">ETE</option>
                    <option value="Math & Physics">Math & Physics</option>
                    <option value="BBA">BBA</option>
                    <option value="Archi">Archi</option>
                    <option value="Mechanical">Mechanical</option>
                    <option value="Pharmacy">Pharmacy</option>
                  </select>
                </div>
              </div>
              <div>
                <label>ID</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="ID"
                    name="id"
                    value={FacultyValue.id}
                    onChange={HandleFacultyChange}
                    required
                  />
                </div>
              </div>
              <div>
                <label>Password</label>
                <div className="inputdiv">
                  <input
                    type="text"
                    placeholder="Password"
                    name="password"
                    value={FacultyValue.password}
                    onChange={HandleFacultyChange}
                    required
                  />
                </div>
              </div>
           
              <button type="submit" className="formsubmitbutton">
                {loading ? "Loading..." : "Submit"}
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Add_Faculty;
