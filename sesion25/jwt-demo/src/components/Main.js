export default function Main() {

  function logOut() {
    localStorage.removeItem("token");
  }

  return (
    <div className="form vh-100 row m-0 align-items-center justify-content-center">
      <div className="col-md-4">
        <div className="row">
          <h1>Home</h1>
          <p>Welcome!!</p>
        </div>
        <div>
          <button className="btn btn-primary" onClick={logOut}>Logout</button>
        </div>
      </div>
    </div>
  );
}
