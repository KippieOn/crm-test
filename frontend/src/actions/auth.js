import * as actionType from './types';

export const login = (data) => {
  return {
    type: actionType.DO_LOGIN,
    data,
  }
}

export const loginSuccess = (data) => {
  return {
    type: action.LOGIN_SUCCESS,
    data,
  }
}

export const loginFailed = (data) => {
  return {
    type: action.LOGIN_FAILED,
    data,
  }
}
