import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignInPage from "./SignInPage.tsx"
import HomePage from "./HomePage.tsx" // You'll need to create this component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signin" element={<SignInPage />} />
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  )
}

export default App