import axios from 'axios';
import _ from 'lodash'
import { URL as API_ROOT, LOGIN as LOGIN_URL } from '../config/constants';
const ACCESSTOKEN = 'accessToken';

export function InvalidCredentialsException(message) {
    this.message = message;
    this.name = 'InvalidCredentialsException';
}

const AuthService = {
  isLoggedIn: () =>  {
    if (window.localStorage.getItem(ACCESSTOKEN)){
      return true;
    } else {
      return false;
    }
  },
  callLoginApi: (email, password, callback) => {
    axios.post(`${API_ROOT}${LOGIN_URL}`, {
      username: email,
      password: password,
    })
    .then(function (response) {
      let result = {};
      let status = response.status;
      if (status === 200){
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
    })
    .catch(function (error) {
      // raise different exception if due to invalid credentials
      if (_.get(error, 'response.status') === 400) {
        throw new InvalidCredentialsException(error);
      }
      throw error;
    });
  },
  logout:() => {
    window.localStorage.removeItem(ACCESSTOKEN);
  }
};

export default AuthService;
