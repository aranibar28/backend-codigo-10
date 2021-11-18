import axios from "axios";
import { useEffect, useState } from "react";

export default function Main() {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  function getCurrentUserData() {
    setLoading(true);
    let getCurrentUserUrl = "http://localhost:8000/api/user/me";
    axios
      .get(getCurrentUserUrl, {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("token"),
        },
      })
      .then((response) => {
        setCurrentUser(response.data);
        console.log(response);
        setLoading(false);
      })
      .catch((error) => {
        console.log(error);
        setLoading(false);
      });
  }

  useEffect(() => {
    getCurrentUserData();
  }, []);

  function logOut() {
    localStorage.removeItem("token");
  }

  return (
    <div className="form vh-100 row m-0 align-items-center justify-content-center">
      <div className="col-md-4">
        <div className="row">
          <h1>Home</h1>
          {loading ? (
            <span>Loading...</span>
          ) : (
            <p>
              Welcome {currentUser.first_name} {currentUser.last_name}
            </p>
          )}
        </div>
        <div>
          <button className="btn btn-primary" onClick={logOut}>
            Logout
          </button>
        </div>
      </div>
    </div>
  );
}
