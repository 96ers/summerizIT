import AuthHistoryHero from "./AuthHistoryHero"
import AuthHistoryDemo from "./AuthHistoryDemo"
const AuthHistory = () => {
  return (
    <main>
      <div className="main">
        <div className="gradient"></div>
      </div>

      <div className="app">
        <AuthHistoryHero/>
        <AuthHistoryDemo/>
      </div>
    </main>
  )
}

export default AuthHistory