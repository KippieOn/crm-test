import axios from 'axios';
import {API_ROOT} from '../constants';

function callLoginApi(email, password, callback) {
  axios.post(`${API_ROOT}/api/auth`, {
    username: email,
    password: password,
  })
  .then(function (response) {
    let result = {};
    let status = response.status;
    if (status == 200){
      result = {
        token: response.data.token,
        email,
      };
    } else {
      result = {
        error : response.data.non_field_errors[0]
      }
    }

    return callback(result);
  })
  .catch(function (error) {
    return callback({error});
  });
}

const logout = () => {

}

export {
  callLoginApi,
  logout,
}
