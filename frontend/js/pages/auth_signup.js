



export default class AuthSignup {
    init = () => {
        console.log("heoolll!!!")

        const emailField = document.getElementById("id_email")

        emailField.appendElement("")

        emailField.addEventListener('blur',  async ()  => {
            const value = emailField.value;
           const response  = await fetch(`/api/auth/validate-email?email=${value}`);
           const data = await response.json()
           console.log(data)

           if(response.ok) {

           } else {
            alert("NOO")
           }

        })
    }
}