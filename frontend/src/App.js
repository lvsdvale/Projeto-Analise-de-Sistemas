import React, { useContext, useEffect, useState } from "react";

import Register from "./components/Register";


const App = () => {
  const [message, setMessage] = useState("");


  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("http://127.0.0.1:8000/", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <>
      <div className="columns">
        <div className="column"></div>
        <div className="column m-5 is-two-thirds">
            <div className="columns">
              <Register /> 
            </div>
        </div>
        <div className="column"></div>
      </div>
    </>
  );
};

export default App;
