import React, { useContext } from "react";
import { Context } from "../store/appContext";
import ROUTINENATION from "../../img/ROUTINE NATION 2.png";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="container-fluid ms-auto row-3 bg-black">
      <div className="d-flex justify-content-end">
        <img src={ROUTINENATION} width={1000} height={700} alt="..." />
      </div>
      <div className="alert alert-info">
        {store.message ||
          "Loading message from the backend (make sure your python backend is running)..."}
      </div>
      <p>
        This boilerplate comes with lots of documentation:{" "}
        <a href="https://github.com/4GeeksAcademy/react-flask-hello/tree/95e0540bd1422249c3004f149825285118594325/docs">
          Read documentation
        </a>
      </p>
    </div>
  );
};
