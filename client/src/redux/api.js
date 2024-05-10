import axios from 'axios'

const X_API_KEY = 'd4Nh4Q5or8WkjMNqgYAM9AS2MebGCCxHrEY6HVZT';

const api = axios.create({
    baseURL: 'http://localhost:9999/api/v1/',
    headers: {
        'Content-Type': 'application/json',
        'x-api-key': `${X_API_KEY}`
    }
})

export default api