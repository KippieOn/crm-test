import axios from 'axios';
import {API_ROOT} from '../constants';
const ACCESSTOKEN = 'accessToken';

const AuthService = {
  isLoggedIn: () =>  {
    if (window.localStorage.getItem(ACCESSTOKEN)){
      return true;
    } else {
      return false;
    }
  },
  callLoginApi: (email, password, callback) => {
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
        window.localStorage.setItem(ACCESSTOKEN, result.token);
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
  },
  logout:() => {
    window.localStorage.removeItem(ACCESSTOKEN);
  }
};

export default AuthService;
