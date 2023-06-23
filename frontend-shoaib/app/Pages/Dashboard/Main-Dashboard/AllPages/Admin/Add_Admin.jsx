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
const notify = (text) => toast(text);

const Add_Admin = () => {
 
  console.log(1);

 

  const [loading, setLoading] = useState(false);

  const initData = {
    adminName: "", 
    adminEmail: "",
    adminGender: "",
    adminAddress: "",
    adminEducation: "",
    adminDepartment: "",
    adminID: "",
    adminPassword: "",
    adminInitial :"",
    details: "",
  };
  const [FacultyValue, setFacultyValue] = useState(initData);

  const HandleFacultyChange = (e) => {
    setFacultyValue({ ...FacultyValue, [e.target.name]: e.target.value });
  };

  const HandleFacultySubmit = (e) => {
    e.preventDefault();
    setLoading(true);
 
     
  };


  return (
    <>
      <ToastContainer />
      <div className="container">
      <Sidebar userType="admin"/>
        <div className="AfterSideBar">
          <div className="Main_Add_Faculty_div">
            </div>
        </div>
      </div>
    </>
  );
};

export default Add_Admin;
