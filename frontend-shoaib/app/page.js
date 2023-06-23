"use client";
import "./globals.css";
import AllRoutes from "./Routes/AllRoutes";
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";


export default function Home() {
  return (
    <main>
      <BrowserRouter>
      <AllRoutes />
  </BrowserRouter>
    </main>
  );
}



//const root = ReactDOM.createRoot(document.getElementById("root"));
/*root.render(
  <BrowserRouter>
    <Provider store={store}>
      <Home />
    </Provider>
  </BrowserRouter>
);
*/