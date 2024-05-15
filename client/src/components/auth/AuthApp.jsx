import AuthHero from './AuthHero';
import { AuthDemo } from './AuthDemo';

import '../../App.css'

export const AuthApp = () => {
  // TODO: implement account menu

  return (
    <main>
      <div className="main">
        <div className="gradient" />
      </div>

      <div className="app">
        <AuthHero/>
        <AuthDemo/>
      </div>
    </main>
  );
}
