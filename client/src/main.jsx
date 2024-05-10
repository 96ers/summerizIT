import Root from './Root'; // Import Root component
import { Provider } from 'react-redux';
import store from './redux/store';
import ReactDOM from 'react-dom/client';

const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);

root.render(
    <Provider store={store}>
        <Root />
    </Provider>
);