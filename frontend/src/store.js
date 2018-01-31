import { compose, createStore, applyMiddleware } from 'redux';
import { createLogger } from 'redux-logger';
import { REHYDRATE, persistStore } from 'redux-persist';
import rootReducer from './reducers'

const store = createStore (
  rootReducer,
  compose(
    applyMiddleware(
      createLogger(),
    ),
  )
);
persistStore(store);
export default store;
