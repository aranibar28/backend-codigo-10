import { useState } from "react";
import axios from "axios";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState("");

  function doLogin() {
    let auth_url = "http://localhost:8000/jwt_login/";
    axios
      .post(auth_url, {
        email: email,
        password: password,
      })
      .then((response) => {
        console.log("ok");
        console.log(response.data.token);
        localStorage.setItem("token", response.data.token);
        window.location.reload(true);
      })
      .catch((error) => {
        console.log("ERROR");
        console.log(error);
        setErrors(error.response.data.status);
      });
  }

  return (
    <div className="form vh-100 row m-0 align-items-center justify-content-center">
      <div className="col-md-4">
        <div className="row">
          <h1>Login</h1>
        </div>
        {errors !== "" ? (
        <div className="alert alert-danger" role="alert">
          {errors}
        </div>) : null}

        <div className="row mb-4">
          <div className="form-group">
            <input
              placeholder="Email"
              className="form-control mb-2"
              type="text"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
            />
          </div>
          <div className="form-group">
            <input
              placeholder="Password"
              className="form-control mb-2"
              type="password"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
              }}
            />
          </div>
        </div>
        <div className="row">
          <button className="btn btn-info" onClick={doLogin}>
            Login
          </button>
        </div>
        <div className="p-4"></div>
      </div>
    </div>
  );
}
