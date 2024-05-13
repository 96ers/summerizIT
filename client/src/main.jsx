import Root from './Root'; // Import Root component
import { Provider } from 'react-redux';
import { store, persistor } from './redux/store';
import ReactDOM from 'react-dom/client';
import { PersistGate } from 'redux-persist/integration/react';
const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);

root.render(
    <Provider store={store}>
        <PersistGate loading={null} persistor={persistor}>
            <Root />
        </PersistGate>
    </Provider>
);