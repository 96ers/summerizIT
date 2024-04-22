import Root from './Root'; // Import Root component
import { Provider } from 'react-redux';
import store from './redux/store';
import ReactDom from 'react-dom';
// Sử dụng createRoot() thay vì ReactDOM.render()

ReactDom.render(
    <Provider store={store}>
        <Root />
    </Provider>,
    document.getElementById('root')
)
