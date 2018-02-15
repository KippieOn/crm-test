import * as actionType from "./types";

const authActions = {
  setLoginPending: isLoginPending => {
    return {
      type: actionType.SET_LOGIN_PENDING,
      isLoginPending
    };
  },
  setLoginSuccess: isLoginSuccess => {
    return {
      type: actionType.SET_LOGIN_SUCCESS,
      isLoginSuccess
    };
  },
  setLoginError: loginError => {
    return {
      type: actionType.SET_LOGIN_ERROR,
      loginError
    };
  },
  setLoginData: ({token, email}) => {
    return {
      type: actionType.SET_USER_LOGIN_DATA,
      token,
      email
    };
  },
};

export default authActions;
