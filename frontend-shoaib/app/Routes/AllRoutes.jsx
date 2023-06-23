import React from "react";
import { Route, Routes } from "react-router-dom";
import DLogin from "../Pages/Dashboard/Dashboard-Login/DLogin";

import Assign_Course from "../Pages/Dashboard/Main-Dashboard/AllPages/Admin/Assign_Course";
//import Add_Faculty from "../Pages/Dashboard/Main-Dashboard/AllPages/Admin/Add_Faculty";
import Add_Faculty from "../Pages/Dashboard/Main-Dashboard/AllPages/Admin/Add_Faculty";
import Offer_Course from "../Pages/Dashboard/Main-Dashboard/AllPages/Faculty/Offer_Course";
import Add_Course from "../Pages/Dashboard/Main-Dashboard/AllPages/Faculty/Add_Course";
import Faculty_Profile from "../Pages/Dashboard/Main-Dashboard/AllPages/Faculty/Faculty_Profile";
import Offered_Courses from "../Pages/Dashboard/Main-Dashboard/AllPages/Faculty/offered_Courses";
import { Admin } from "../Pages/Dashboard/Main-Dashboard/AllPages/backend";

import FrontPage from "../Pages/Dashboard/Main-Dashboard/GlobalFiles/FrontPage";
import Add_Admin from "../Pages/Dashboard/Main-Dashboard/AllPages/Admin/Add_Admin";
//import Add_Course2 from "../Pages/Dashboard/Main-Dashboard/AllPages/Admin/Add_Course2";




const AllRoutes = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<DLogin />} />
        <Route path="/dashboard" element={<FrontPage />} />
        <Route path="/assigncourse" element={<Assign_Course />} />
        <Route path="/addfaculty" element={<Add_Faculty />} /> 
        <Route path="/offeredcourses" element={<Offered_Courses />} /> 
        <Route path="/offercourse" element={<Offer_Course />} />
        <Route path="/addcourse" element={<Add_Course />} />
        <Route path="/facultyprofile" element={<Faculty_Profile />} />
        <Route path="/addadmin" element={<Add_Admin />} />
        

      </Routes>
    </>
  );
};

export default AllRoutes;
