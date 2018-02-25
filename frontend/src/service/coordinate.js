import axios from "axios";
import { URL as API_ROOT } from '../config/constants';

const CoordinateService = {
  read: (id, auth_token, callback) => {
    axios
      .get(`${API_ROOT}/api/coordinates/${id}/`)
      .then(function(response) {
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  update: (id, data ,auth_token, callback) => {
    axios
      .put(`${API_ROOT}/api/coordinates/${id}/`,{
        username: email,
        password: password,
      })
      .then(function(response) {
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  updatePartial: (id, data ,auth_token, callback) => {
    axios
      .patch(`${API_ROOT}/api/coordinates/${id}/`,{
        username: email,
        password: password,
      })
      .then(function(response) {
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  delete: (id, callback) => {
    axios
      .delete(`${API_ROOT}/api/coordinates/${id}/`)
      .then(function(response) {
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      });
  }

};
