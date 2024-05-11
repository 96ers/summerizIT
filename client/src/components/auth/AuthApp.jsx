import AuthHero from './AuthHero';
import Demo from '../Demo';

import { AuthDemo } from './AuthDemo';

import '../../App.css'

export const AuthApp = () => {
  // TODO: change login button to user logo with logout button

  return (
    <main>
      <div className="main">
        <div className="gradient" />
      </div>

      <div className="app">
        <AuthHero/>
        <Demo/>
      </div>
    </main>
  );
}
