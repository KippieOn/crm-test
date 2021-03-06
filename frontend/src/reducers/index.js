import { combineReducers } from 'redux';
import * as actionType from '../actions/types';
import auth from './auth';

const tokenInitialState = null;
const token = ( state = tokenInitialState, action ) => {
  switch(action.type) {
    case actionType.SET_TOKEN:
      return action.data;
    default:
      return state;
  }
}

const appReducer = combineReducers({
  token,
  auth,
})

const rootReducer = (state, action) => {
  return appReducer(state, action);
}

export default rootReducer;
