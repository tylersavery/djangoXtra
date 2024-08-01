import AuthSignup from './pages/auth_signup.js';

class App {
    init = () => {
        this.handlePage();
    }

    handlePage = () => {

        if(!!(document.querySelector('main#auth-signup'))) {
            (new AuthSignup).init();
        }

    }


}




window.onload = () => {
      const app = new App();
      app.init();
}