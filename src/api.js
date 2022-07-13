import axios from "./boot/axios";
import { api } from "./boot/axios";
import { Loading, QSpinnerBars, Notify } from "quasar";
let token = sessionStorage.getItem("token");

function getToken() {
  let user = JSON.parse(sessionStorage.getItem("user"));
  let formData = new FormData();
  formData.append("email", user.email);
  api
    .post("refresh-token/", formData)
    .then((res) => {
      sessionStorage.setItem("token", res.data.token);
      get();
    })
    .catch((error) => {
      console.error(error);
    });
}
function get(url, params) {
  Loading.show({
    spinner: QSpinnerBars,
    spinnerColor: "positive",
    message: "Cargando...",
  });
  return api
    .get(url, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((res) => {
      Loading.hide();
      return res;
    })
    .catch((error) => {
      Loading.hide();
      if (error.response.data.expired == true) {
        getToken();
      }
      if (error.message == "Network Error") {
        Notify.create({
          type: "negative",
          position: "top-right",
          message:
            "No se pudo conectar con el servidor, revisa tu conexión a internet o intentalo de nuevo mas tarde",
        });
      } else if (error.response.status >= 400) {
        if (error.response.status === 401) {
          Notify.create({
            type: "negative",
            position: "top-right",
            message: error.response,
          });
        } else {
          Notify.create({
            type: "negative",
            position: "top-right",
            message: "Ocurrió un error desconocido",
          });
        }
        console.log(error.message + " " + error.response.data.message + "");
      } else {
        Notify.create({
          type: "negative",
          position: "top-right",
          message: "El servidor envió una respuesta inválida",
        });
      }
      return error;
    });
}
export default {
  get,
};
