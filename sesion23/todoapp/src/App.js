import "./App.css";
import React, { useEffect } from "react";
import NewItemModal from "./components/modals";
import axios from "axios";

function App() {
  const todoItemsData = [
    {
      id: 1,
      title: "Tarea de prueba 1",
      user_id: 1,
      status: 1,
    },
  ];

  const [todoItems, setTodoItems] = React.useState(todoItemsData);
  const [modal, setModal] = React.useState(false);
  const [newTask, setNewTask] = React.useState("");

  function dimissModal() {
    setModal(false);
  }

  function onChangeInput(value) {
    setNewTask(value);
  }

  function checkHandler(value, id) {
    let final_url = "http://localhost:8000/task/" + id;
    axios
      .put(
        final_url,
        { status: value },
        {
          headers: {
            Authorization: "Token 2a23a070d98969c9c926c25d8209cb5360d8ee36",
          },
        }
      )
      .then((res) => refresh())
      .catch((err) => console.log(err));
  }

  function addTask() {
    axios
      .post(
        "http://localhost:8000/tasks/",
        {
          title: newTask,
        },
        {
          headers: {
            Authorization: "Token 2a23a070d98969c9c926c25d8209cb5360d8ee36",
          },
        }
      )
      .then((res) => refresh())
      .catch((err) => console.log(err));
  }

  function deleteTask(id) {
    let final_url = "http://localhost:8000/task/" + id;
    axios
      .delete(final_url, {
        headers: {
          Authorization: "Token 2a23a070d98969c9c926c25d8209cb5360d8ee36",
        },
      })
      .then((res) => refresh())
      .catch((err) => console.log(err));
  }

  function refresh() {
    axios
      .get("http://localhost:8000/tasks/", {
        headers: {
          Authorization: "Token 2a23a070d98969c9c926c25d8209cb5360d8ee36",
        },
      })
      .then((res) => setTodoItems(res.data))
      .catch((err) => console.error(err));
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div className="App">
      <div className="container">
        <h1>ToDo App</h1>
        <div className="row mb-3">
          <div className="col-md-9">
            <input
              className="form-control"
              value={newTask}
              onChange={(e) => onChangeInput(e.target.value)}
            />
            <span>{newTask}</span>
          </div>
          <div className="col-md-3">
            <button className="btn btn-success" onClick={addTask}>
              Agregar Tarea
            </button>
             
          </div>
        </div>
        <div className="row">
          <table className="table table-striped table-bordered">
            <thead>
              <tr>
                <th>Estado</th>
                <th>#</th>
                <th>Tarea</th>
                <th>Acciones</th>
              </tr>
            </thead>
            {todoItems.map((item) => {
              return (
                <tbody>
                  <tr>
                    <td>
                      <input
                        type="checkbox"
                        className="form-control"
                        onChange={(e) => {
                          checkHandler(e.target.checked, item["id"]);
                        }}
                        checked={item["status"]}
                      />
                    </td>
                    <td>{item["id"]}</td>
                    <td>{item["title"]}</td>
                    <td>
                      <button className="btn btn-sm btn-info">Editar</button> 
                      <button
                        className="btn btn-sm btn-danger"
                        onClick={(e) => deleteTask(item["id"])}
                      >
                        Eliminar
                      </button>
                    </td>
                  </tr>
                </tbody>
              );
            })}
          </table>
        </div>
      </div>

      {modal ? <NewItemModal cancelCallback={dimissModal} /> : null}
    </div>
  );
}

export default App;
