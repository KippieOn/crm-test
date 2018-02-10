import * as actionType from '../actions/types';

const initialState = {
  isLoggedIn: false,
  username: null,
  auth_token: null
}

const auth = (state = initialState, action) => {
  switch(action.type) {
    case actionType.LOGIN_SUCCESS:
      return {
        isLoggedIn: true,
        username: action.user,
        auth_token: action.auth_token,
      };
    case actionType.LOGIN_FAILED:
      return initialState;
    default:
      return state;
  }
}
