"use client";
import { Table } from "antd";
import React from "react";
import { MdPersonAdd } from "react-icons/md";
import { FaUserNurse } from "react-icons/fa";
import { RiEmpathizeLine } from "react-icons/ri";
import { FaBed } from "react-icons/fa";
import { MdOutlineBedroomParent } from "react-icons/md";
import { FaAmbulance } from "react-icons/fa";
import { BsFillBookmarkCheckFill } from "react-icons/bs";
import { MdPayment } from "react-icons/md";
import { RiAdminLine } from "react-icons/ri";
import Sidebar from "./Sidebar";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { GetAllData } from "../../../../Redux/Datas/action";
import TextArea from "antd/es/input/TextArea";

const FrontPage = () => {
 

  const {
    dashboard: { data },
  } = useSelector((store) => store.data);

  console.log(data);

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(GetAllData());
  }, []);

  return (
    <div className="container">
      <Sidebar userType="admin"/>
      <div className="AfterSideBar">
        <h1 style={{ color: "rgb(184 191 234)" }}>Overview</h1>
        <div className="maindiv">
          <div className="one commondiv">
            <div>
              <h1>{data?.doctor}</h1>
              <p>Faculty</p>
            </div>
            <MdPersonAdd className="overviewIcon" />
          </div>
          
          <div className="six commondiv">
            {" "}
            <div>
              <h1>{data?.admin}</h1>
              <p>Admin</p>
            </div>
            <RiAdminLine className="overviewIcon" />
          </div>
         

        
          <div className="six commondiv">
            {" "}
            <div>
              <h1>{data?.report}</h1>
              <p>Course Count</p>
            </div>
            <MdPayment className="overviewIcon" />
          </div>
          <div className="six commondiv">
            {" "}
            <div>
              <h1>{data?.appointment}</h1>
              <p>Offered Course</p>
            </div>
            < BsFillBookmarkCheckFill className="overviewIcon" />
          </div>
        </div>
        {/* ************************************* */}
        <div className="patientDetails">
          <h1>Corse List</h1>
          <div className="patientBox">
            <TextArea value={"Notices"}></TextArea>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FrontPage;
